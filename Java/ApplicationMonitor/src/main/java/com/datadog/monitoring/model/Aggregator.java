package com.datadog.monitoring.model;

import com.datadog.monitoring.config.Config;

public abstract class Aggregator {
    public static Aggregator of(Config.Aggregate agg) {
        switch (agg) {
            case SUM:
                return new Sum();
            case AVG:
                return new Avg();
        }
        throw new RuntimeException("Aggregate " + agg + " not yet implemented");
    }

    public static Aggregator sum() {
        return new Sum();
    }

    /**
     * Return the accumulated result and clear state.
     * @return - Accumulated result
     */
    public double finish() {
        double ret = result();
        reset();
        return ret;
    }
    public abstract void addDataPoint(double d);

    protected abstract double result();

    protected abstract void reset();

    private static class Sum extends Aggregator {
        private double res;

        public Sum() {
            reset();
        }

        public void addDataPoint(double d) {
            res += d;
        }

        @Override
        public double result() {
            return res;
        }

        @Override
        public void reset() {
            res = 0;
        }
    }

    private static class Avg extends Aggregator {
        final Sum sum;
        private int count;

        Avg() {
            this.sum = new Sum();
            count = 0;
        }

        @Override
        public void addDataPoint(double d) {
            sum.addDataPoint(d);
            count++;
        }

        @Override
        public double result() {
            return sum.result() / count;
        }

        @Override
        public void reset() {
            sum.reset();
            count = 0;
        }
    }
}
