package com.datadog.monitoring.processor;

import com.datadog.monitoring.processor.api.PeriodicProcessor;
import org.apache.commons.csv.CSVRecord;

import java.util.List;
import java.util.function.Consumer;

/**
 * Distributes log records to consumers in parallel.
 * A naive implementation of stream distribution. In real world application
 * something like AWS kinesis might replace this.
 */
public class LogDistributor implements Consumer<CSVRecord>, AutoCloseable {
    private final List<PeriodicProcessor<CSVRecord>> processorList;

    public LogDistributor(List<PeriodicProcessor<CSVRecord>> processorList) {
        this.processorList = processorList;
    }

    @Override
    public void close() {
        processorList.parallelStream().forEach(PeriodicProcessor::close);
    }

    @Override
    public void accept(CSVRecord rec) {
        processorList.parallelStream().forEach(processor -> processor.accept(rec));
    }
}
