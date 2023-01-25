package com.datadog.monitoring.model;

public class Stats {
    final private String section;
    private int hits;
    private int post;
    private int get;
    private int err4xx;
    private int err5xx;
    private int success;

    public static final Stats NULL = new Stats("");
    public Stats(String section) {
        hits = 0;
        post = 0;
        get = 0;
        err4xx = 0;
        err5xx = 0;
        success = 0;
        this.section = section;
    }

    public int totalHits() {
        return hits;
    }

    public void addHits(int hits) {
        this.hits += hits;
    }

    public void addPost(int post) {
        this.post += post;
    }

    public void addGet(int count) {
        this.get += count;
    }

    public void add4xx(int count) {
        this.err4xx += count;
    }

    public void add5xx(int count) {
        this.err5xx += count;
    }

    public int getFailedCount() {
        return err4xx + err5xx;
    }

    public void addSuccess(int count) {
        this.success += count;
    }

    @Override
    public String toString() {
        return "{" +
               "section = '" + section + '\'' +
               ", hits = " + hits +
               ", POST = " + post +
               ", GET = " + get +
               ", 4xx errors = " + err4xx +
               ", 5xx errors = " + err5xx +
               ", successful = " + success +
               ", failures = " + getFailedCount() +
               '}';
    }
}
