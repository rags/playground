package com.datadog.monitoring.processor;

import org.apache.commons.csv.CSVParser;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.time.Duration;

import static com.datadog.monitoring.processor.CsvFixture.getCsvRecords;
import static org.junit.jupiter.api.Assertions.assertTrue;

class SectionLoadLoggerTest {

    private ByteArrayOutputStream out;
    private SectionLoadLogger sectionLoadLogger;

    @BeforeEach
    void setUp() {
        out = new ByteArrayOutputStream();
        sectionLoadLogger = new SectionLoadLogger("foo", Duration.ofSeconds(10), new PrintStream(out));
    }

    @Test
    void testLoggingOfMaxHits() {
        CSVParser csvRecords = getCsvRecords("\"10.0.0.3\",\"-\",\"apache\",1549574330,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574330,\"POST /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574330,\"GET /api/user HTTP/1.0\",500,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574332,\"GET /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574332,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574333,\"GET /report HTTP/1.0\",200,1136\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574334,\"POST /report HTTP/1.0\",404,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",500,1261\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",200,1261\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /report HTTP/1.0\",200,1136\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574337,\"GET /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /api/user HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /report HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574340,\"GET /report HTTP/1.0\",200,1261\n");
        csvRecords.forEach(sectionLoadLogger);
        assertTrue(output().contains("{section = '/api', hits = 10, POST = 5, GET = 5, 4xx errors = 0, 5xx errors = " +
                                     "1, successful = 9, failures = 1}" ), "Actual: " + output());
    }

    private String output() {
        return out.toString();
    }

    @Test
    void testLoggingOfTrailingData() {
        CSVParser csvRecords = getCsvRecords("\"10.0.0.2\",\"-\",\"apache\",1549574336,\"POST /report/user HTTP/1" +
                                             ".0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574337,\"GET /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /api/user HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /report HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574340,\"GET /report HTTP/1.0\",200,1261\n");
        //Use auto close to flush trailing data that may never hit the period end.
        try(SectionLoadLogger logger = sectionLoadLogger) {
            csvRecords.forEach(logger);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        assertTrue(output().contains("[07/02/2019, 22:18:56 - 07/02/2019, 22:19:06]"),
                "Expected interval to be logged but was " + output());
        assertTrue(
                output().contains("{section = '/report', hits = 4, POST = 2, GET = 2, 4xx errors = 0, 5xx errors = " +
                                  "0, successful = 4, failures = 0}"), "Actual: " + output());
    }

}