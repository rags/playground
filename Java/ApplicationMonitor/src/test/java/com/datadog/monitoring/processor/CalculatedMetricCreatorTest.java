package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Aggregator;
import com.datadog.monitoring.model.Metric;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.time.Instant;

import static org.junit.jupiter.api.Assertions.*;

class CalculatedMetricCreatorTest {

    private StubConsumers<Metric> consumers;

    @BeforeEach
    void setUp() {
        consumers = new StubConsumers<>();
    }

    public
    @Test
    void testAverage() {
        Instant start = Instant.now();
        try(CalculatedMetricCreator metricCreator =
                new CalculatedMetricCreator("blahMetric", Duration.ofMinutes(2), Aggregator.of(Config.Aggregate.AVG),
                        consumers)) {

            double metric = 1;
            // 4 metrics per 2-min period for 5 mins. values: p1: 1,2,3,4, p2: 5,6,7,8, p3 (only 1 min): 9,10
            for (Instant i = start; i.isBefore(start.plus(Duration.ofMinutes(5))); i = i.plusSeconds(30)) {
                metricCreator.accept(new Metric(metric++, i));
            }
            assertEquals(2, consumers.outputSize());
            assertEquals(new Metric(2.5, start), consumers.output(0)); //avg(1,2,3,4)
            assertEquals(new Metric(6.5, start.plus(Duration.ofMinutes(2))), consumers.output(1)); //avg(5,6,7,8)
        } // remaining data gets flushes here
        assertEquals(3, consumers.outputSize());
        assertEquals(new Metric(9.5, start.plus(Duration.ofMinutes(4))), consumers.output(2)); // avg(9,10)
    }

    @Test
    void testSum() {
        Instant start = Instant.now();
        try(CalculatedMetricCreator metricCreator =
                    new CalculatedMetricCreator("blahMetric", Duration.ofMinutes(1),
                            Aggregator.of(Config.Aggregate.SUM),
                            consumers)) {

            double metric = 10;
            // values:10,9,8,7,6,5,4,3,2,1 (2 vals per min)
            for (Instant i = start; i.isBefore(start.plus(Duration.ofMinutes(5))); i = i.plusSeconds(30)) {
                metricCreator.accept(new Metric(metric--, i));
            }
            assertEquals(4, consumers.outputSize());
            assertEquals(new Metric(19, start), consumers.output(0));
            assertEquals(new Metric(15, start.plus(Duration.ofMinutes(1))), consumers.output(1));
            assertEquals(new Metric(11, start.plus(Duration.ofMinutes(2))), consumers.output(2));
            assertEquals(new Metric(7, start.plus(Duration.ofMinutes(3))), consumers.output(3));
        } // remaining data gets flushes here
        assertEquals(5, consumers.outputSize());
        assertEquals(new Metric(3, start.plus(Duration.ofMinutes(4))), consumers.output(4)); // avg(9,10)
    }
}