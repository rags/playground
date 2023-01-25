package com.datadog.monitoring.model;

import java.time.Instant;
import java.util.Objects;

/**
 * Represents a single point in a timeseries data.
 */
public class Metric {
    // Double data for simplicity. Ideal this would T in `Metric<T is Number>`.
    // Due to java limitations of templating this is not trivial to implement.
    // Java generics specifically does not play well with primitives. So you cant
    // do numeric arithmetic in meaningful way with generics.
    final double data;
    final Instant time;
    public Metric(double data, Instant time) {
        this.data = data;
        this.time = time;
    }

    public double data() {
        return data;
    }

    public Instant time() {
        return time;
    }

    @Override
    public String toString() {
        return "Metric{" +
               "data=" + data +
               ", time=" + time +
               '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Metric metric = (Metric) o;
        return Double.compare(metric.data, data) == 0 && time.equals(metric.time);
    }

    @Override
    public int hashCode() {
        return Objects.hash(data, time);
    }
}
