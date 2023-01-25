package com.datadog.monitoring.processor;

import com.datadog.monitoring.model.Aggregator;
import com.datadog.monitoring.model.Consumers;
import com.datadog.monitoring.model.Metric;
import com.datadog.monitoring.processor.api.PeriodicProcessor;

import java.time.Duration;
import java.util.function.Consumer;

/**
 * Base class for SimpleMetricProcessor, CalculatedMetricProcessor
 */
public abstract class BaseMetricCreator<T> extends PeriodicProcessor<T> {

    protected final Consumers<Metric> consumers;
    protected final Aggregator agg;

    protected BaseMetricCreator(String name, Duration period, Consumers<Metric> consumers, Aggregator agg) {
        super(name, period);
        this.consumers = consumers;
        this.agg = agg;
    }

    protected void flushResultImpl() {
        consumers.accept(new Metric(agg.finish(), startTime()));
    }

    public void addConsumer(Consumer<Metric> consumer) {
        consumers.add(consumer);
    }

    @Override
    public void close() {
        super.close();
        // Also close all closable consumers
        consumers.parallel()
                .filter(c-> c instanceof AutoCloseable)
                .map(c->(AutoCloseable) c)
                .forEach(c-> {
                    try {
                        c.close();
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                });
    }
}
