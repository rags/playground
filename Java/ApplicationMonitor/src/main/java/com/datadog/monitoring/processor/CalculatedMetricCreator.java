package com.datadog.monitoring.processor;

import com.datadog.monitoring.model.Aggregator;
import com.datadog.monitoring.model.Consumers;
import com.datadog.monitoring.model.Metric;

import java.time.Duration;
import java.time.Instant;

/**
 * Consumers a metric and aggregates it periodically
 */
public class CalculatedMetricCreator extends BaseMetricCreator<Metric> {
    private final String parent;

    public CalculatedMetricCreator(String name, Duration period, Aggregator agg, String parentMetric) {
        this(name, period, agg, parentMetric, new Consumers<>());
    }
    CalculatedMetricCreator(String name, Duration period, Aggregator agg, String parentMetric,
                                   Consumers<Metric> consumers) {
        super(name, period, consumers, agg);
        this.parent = parentMetric;
    }
    CalculatedMetricCreator(String name, Duration period, Aggregator agg, Consumers<Metric> consumers) {
        this(name, period, agg, "", consumers);
    }

    @Override
    protected void process(Metric m) {
        agg.addDataPoint(m.data());
    }

    @Override
    protected Instant getTime(Metric m) {
        return m.time();
    }
}
