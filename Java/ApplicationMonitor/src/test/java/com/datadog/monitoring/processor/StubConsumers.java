package com.datadog.monitoring.processor;

import com.datadog.monitoring.model.Consumers;

import java.util.ArrayList;
import java.util.List;

public class StubConsumers<T> extends Consumers<T> {
    private final List<T> output;

    public StubConsumers() {
        output = new ArrayList<>();
    }

    @Override
    public void accept(T data) {
        output.add(data);
    }

    public int outputSize() {
        return output.size();
    }
    public T output(int i) {
        return output.get(i);
    }
}
