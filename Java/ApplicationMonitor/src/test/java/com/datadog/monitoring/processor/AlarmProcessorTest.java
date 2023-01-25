package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Metric;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.sql.Date;
import java.time.Duration;
import java.time.Instant;

import static org.junit.jupiter.api.Assertions.*;

class AlarmProcessorTest {
    private ByteArrayOutputStream out;
    private PrintStream ps;

    @BeforeEach
    void setUp() {
        out = new ByteArrayOutputStream();
        ps = new PrintStream(out);
    }

    private String[] logLines() {
        String log = out.toString();
        if (log.length()==0) return new String[0];
        return log.split("\n");
    }

    @Test
    void testAlarmOnOnlyOnConsecutiveBreaches() {
        AlarmProcessor alarmProcessor = new AlarmProcessor("blahAlarm", 5, 3, 2, minutes(1), ps);
        // 4 breaches but not consecutive
        alarmProcessor.accept(new Metric(6, Instant.now()));
        alarmProcessor.accept(new Metric(6, Instant.now()));
        alarmProcessor.accept(new Metric(5, Instant.now()));
        alarmProcessor.accept(new Metric(6, Instant.now()));
        alarmProcessor.accept(new Metric(6, Instant.now()));
        assertFalse(alarmProcessor.inAlarm());
        assertEquals(0, logLines().length); // nothing to log
    }

    @Test
    void testAlarmOnConsecutiveBreaches() {
        AlarmProcessor alarmProcessor = new AlarmProcessor("blahAlarm", 5, 3, 3, minutes(1), ps);
        Instant start = Instant.now();
        alarmProcessor.accept(new Metric(6, start));
        alarmProcessor.accept(new Metric(7, start.plus(minutes(1))));
        alarmProcessor.accept(new Metric(8, start.plus(minutes(2))));
        assertTrue(alarmProcessor.inAlarm());
        alarmProcessor.accept(new Metric(9, start.plus(minutes(3))));
        alarmProcessor.accept(new Metric(9, start.plus(minutes(4))));
        alarmProcessor.accept(new Metric(9, start.plus(minutes(5))));
        alarmProcessor.accept(new Metric(4, start.plus(minutes(6))));
        alarmProcessor.accept(new Metric(4, start.plus(minutes(7))));
        assertTrue(alarmProcessor.inAlarm());
        String expectedLog = "Alarm 'blahAlarm' triggered at time " +
                             Config.TIMEFORMAT.format(Date.from(start.plus(minutes(3)))) +
                             ". Datapoints: [6.0, 7.0, 8.0]";
        String [] logLines = logLines();
        assertEquals(1, logLines.length);
        assertEquals(expectedLog, logLines[0]);
    }

    private static Duration minutes(int minutes) {
        return Duration.ofMinutes(minutes);
    }

    @Test
    void testAlarmFollowedByRecovery() {
        AlarmProcessor alarmProcessor = new AlarmProcessor("blahAlarm", 10, 2, 3, minutes(1), ps);
        Instant start = Instant.now();
        alarmProcessor.accept(new Metric(10,start));
        alarmProcessor.accept(new Metric(11,start.plus(minutes(1))));
        alarmProcessor.accept(new Metric(12,start.plus(minutes(2))));
        assertTrue(alarmProcessor.inAlarm());
        alarmProcessor.accept(new Metric(10,start.plus(minutes(3))));
        alarmProcessor.accept(new Metric(9,start.plus(minutes(4))));
        alarmProcessor.accept(new Metric(11,start.plus(minutes(5))));
        alarmProcessor.accept(new Metric(10,start.plus(minutes(6))));
        assertTrue(alarmProcessor.inAlarm()); // still in alarm
        alarmProcessor.accept(new Metric(10,start.plus(minutes(7))));
        alarmProcessor.accept(new Metric(9,start.plus(minutes(8)))); //recovery
        assertFalse(alarmProcessor.inAlarm());
        String [] logLines = logLines();
        assertEquals(2, logLines.length);
        String alarmLog = "Alarm 'blahAlarm' triggered at time " +
                             Config.TIMEFORMAT.format(Date.from(start.plus(minutes(3)))) +
                             ". Datapoints: [11.0, 12.0]";
        assertEquals(alarmLog, logLines[0]);
        String recoveryLog = "Alarm 'blahAlarm' recovered at time " +
                          Config.TIMEFORMAT.format(Date.from(start.plus(minutes(9)))) +
                          ". Datapoints: [10.0, 10.0, 9.0]";
        assertEquals(recoveryLog, logLines[1]);
    }
}