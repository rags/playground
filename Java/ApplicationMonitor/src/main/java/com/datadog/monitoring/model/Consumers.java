package com.datadog.monitoring.model;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Stream;

/**
 * Composite of Consumer. Calls accept on its constituents.
 * Order of call is not guaranteed and the assumption is that
 * the constituents are independent.
 */
public class Consumers<T> implements Consumer<T> {
    private final List<Consumer<T>> consumers;

    public Consumers() {
        this(new ArrayList<>());
    }

    public Consumers(List<Consumer<T>> consumers) {
        this.consumers = consumers;
    }

    public void add(Consumer<T> c) {
        consumers.add(c);
    }

    @Override
    public void accept(T data) {
        // Call accept in parallel
        consumers.parallelStream().forEach(t -> t.accept(data));
    }

    public Stream<Consumer<T>> parallel() {
        return consumers.parallelStream();
    }
}
