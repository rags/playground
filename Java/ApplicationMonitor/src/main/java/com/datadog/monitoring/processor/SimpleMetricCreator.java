package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Aggregator;
import com.datadog.monitoring.model.Consumers;
import com.datadog.monitoring.model.Metric;
import org.apache.commons.csv.CSVRecord;

import java.time.Duration;
import java.time.Instant;
import java.util.Optional;
import java.util.function.Predicate;

/**
 * Consumes log records and creates a simple metric periodically.
 */
public class SimpleMetricCreator extends BaseMetricCreator<CSVRecord> {
    private final Optional<Predicate<CSVRecord>> filters;

    public SimpleMetricCreator(String name, Duration period, Optional<Predicate<CSVRecord>> filters,
                               String type) {
        this(name, period, filters, new Consumers<>(), type);
    }

    SimpleMetricCreator(String name, Duration period, Consumers<Metric> consumers) {
        this(name, period, Optional.empty(), consumers, Config.COUNT);
    }

    SimpleMetricCreator(String name, Duration period, Optional<Predicate<CSVRecord>> filters,
                               Consumers<Metric> consumers, String type) {
        super(name, period, consumers, Aggregator.of(Config.Aggregate.SUM));
        if (!"COUNT".equalsIgnoreCase(type)) {
            throw new RuntimeException("Only count supported for simple metrics");
        }
        this.filters = filters;
    }

    @Override
    protected void process(CSVRecord rec) {
        if(!filters.map(p->p.test(rec)).orElse(true)) {
            return;
        }
        agg.addDataPoint(1);
    }

    @Override
    protected Instant getTime(CSVRecord rec) {
        return Instant.ofEpochSecond(Long.parseUnsignedLong(rec.get(Config.DATE)));
    }
}
