package com.datadog.monitoring.processor.api;

import java.time.Duration;
import java.time.Instant;
import java.util.function.Consumer;

/**
 * Represents a steam processing entity that consumers data of type T and the data aggregated is flushed out at
 * intervals specified by the `period`.
 * T is expected to be a time-series element that can provide time for the accompanying data.
 */
public abstract class PeriodicProcessor<T> implements Consumer<T>, AutoCloseable {

    protected final String name;
    private final Duration period;
    private Instant endTime = Instant.MAX;

    protected PeriodicProcessor(String name, Duration period) {
        this.name = name;
        this.period = period;
    }

    @Override
    public void accept(T data) {
        Instant instant = getTime(data);
        if (this.endTime == Instant.MAX) {
            endTime = instant.plus(period);
        }
        assert endTime!=Instant.MAX;
        while (endTime.compareTo(instant) <= 0) flushResult();
        process(data);
    }

    /**
     * For the trailing end of the stream if we do not hit the period end,
     * we need to flush any remaining data before exiting. This will enable
     * us to do so.
     */
    @Override
    public void close() {
        // No data has been processed. nothing to do
        if (endTime==Instant.MAX) return;
        flushResult();
    }
    private void flushResult() {
        flushResultImpl();
        endTime = endTime.plus(period);
    }
    protected abstract void process(T data);
    protected abstract void flushResultImpl();
    protected abstract Instant getTime(T data);

    protected final Instant startTime() {
        return endTime.minus(period);
    }
    protected final Instant endTime() {
        return endTime;
    }

    public String name() {
        return name;
    }

    public Duration period() {
        return period;
    }
}


