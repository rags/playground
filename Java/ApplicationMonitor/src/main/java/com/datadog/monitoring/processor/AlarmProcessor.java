package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Metric;

import java.io.PrintStream;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.function.Consumer;

/**
 * Monitors a metric and alerts when it sees anomalies in the data.
 */
public class AlarmProcessor implements Consumer<Metric> {
    private final String name;
    private final double threshold;
    private final int dataPointsToAlarm;
    private final int dataPointToClearAlarm;

    private final PrintStream out;
    private final String metric;

    private boolean inAlarm;

    // Hold data that breach the threshold line (<= when not in alarm and > when in alarm).
    // It would be less confusing if 2 lists were used for each state - but only one of
    // them is updated depending on state. So this double up as the list tracking breach on
    // either side of threshold line depending on alarm state
    List<Metric> breachedTimeSeries;
    final private Duration period;

    public AlarmProcessor(String name, double threshold, int dataPointsToAlarm, int dataPointToClearAlarm,
                          Duration period, String metric) {
        this(name, threshold, dataPointsToAlarm, dataPointToClearAlarm, period, metric, System.out);
    }

    AlarmProcessor(String name, double threshold, int dataPointsToAlarm, int dataPointToClearAlarm, Duration period,
                          PrintStream out) {
        this(name, threshold, dataPointsToAlarm, dataPointToClearAlarm, period, "", out);
    }

    AlarmProcessor(String name, double threshold, int dataPointsToAlarm, int dataPointToClearAlarm,
                          Duration period, String metric,
                          PrintStream out) {
        this.name = name;
        this.threshold = threshold;
        this.dataPointsToAlarm = dataPointsToAlarm;
        this.dataPointToClearAlarm = dataPointToClearAlarm;
        this.out = out;
        this.period = period;
        this.metric = metric;
        inAlarm=false;
        breachedTimeSeries = new ArrayList<>(Math.max(dataPointsToAlarm, dataPointToClearAlarm));
    }


    @Override
    public void accept(Metric metric) {
        //For now there is no need to track metric and times.
        // This might be required in future Ex: render a graph.
        if (inAlarm) {
            if((metric.data()<=threshold)) {
                breachedTimeSeries.add(metric);
            }
            else {
                breachedTimeSeries.clear();
            }
            if (breachedTimeSeries.size() >= dataPointToClearAlarm) {
                clearAlarm();
            }
        } else {
            if((metric.data()>threshold)) {
                breachedTimeSeries.add(metric);
            }
            else {
                breachedTimeSeries.clear();
            }
            if(breachedTimeSeries.size() >= dataPointsToAlarm) {
                alarm();
            }
        }
    }

    private void alarm() {
        inAlarm = true;
        // "High traffic generated an alert - hits = {value}, triggered at {time}"
        out.println("Alarm '" + name + "' triggered at time " + triggeredTime() + ". Datapoints: " + Arrays.toString(breachPoints()));
        breachedTimeSeries.clear();
    }

    private void clearAlarm() {
        inAlarm = false;
        out.println("Alarm '" + name + "' recovered at time " + triggeredTime() + ". Datapoints: " + Arrays.toString(breachPoints()));
        breachedTimeSeries.clear();
    }

    String triggeredTime() {
        return Config.TIMEFORMAT.format(Date.from(breachedTimeSeries.get(breachedTimeSeries.size() - 1).time().plus(period)));
    }

    double[] breachPoints() {
       return breachedTimeSeries.stream().mapToDouble(Metric::data).toArray();
    }
    boolean inAlarm() {
        return inAlarm;
    }
}
