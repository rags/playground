package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Aggregator;
import com.datadog.monitoring.processor.api.PeriodicProcessor;
import org.apache.commons.csv.CSVRecord;

import java.lang.reflect.InvocationTargetException;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import static com.datadog.monitoring.config.Config.FIELDS;
import static com.datadog.monitoring.config.Config.REGEX_MATCH;

public class ProcessorFactory {
    public LogDistributor createProcessors(Config config) {
        Map<String, SimpleMetricCreator> simpleMetrics = simpleMetricCreatorsFor(config.simpleMetrics());
        alarmsFor(config.alarms(), simpleMetrics,
                calculatedMetricCreatorsFor(config.calculatedMetrics(), simpleMetrics));
        List<PeriodicProcessor<CSVRecord>> processors = createLogConsumers(config.rawLogConsumers());
        processors.addAll(simpleMetrics.values());
        return new LogDistributor(processors);
    }

    /**
     * Assumption here is calculated metrics only depend on one simple metric. In future we need view this as a
     * depency graph of metrics that are arbitrarily deep. To implement this we can use topological sort to generate a
     * dependency order and process metrics in the topological order. That way we can have arbitrarily complex acyclic
     * dependency graph for metrics.
     */
    private CalculatedMetricCreator calculatedMetricCreatorFor(Config.CalculatedMetric config,
                                                               Map<String, SimpleMetricCreator> simpleMetrics) {
        if (!simpleMetrics.containsKey(config.parent())) {
            throw new RuntimeException(
                    "Input metric " + config.parent() + " missing for caclulated metric " + config.name());
        }
        CalculatedMetricCreator calculatedMetricCreator =
                new CalculatedMetricCreator(config.name(), config.period(), Aggregator.of(config.aggregate()),
                        config.parent());
        SimpleMetricCreator simpleMetricCreator = simpleMetrics.get(config.parent());
        simpleMetricCreator.addConsumer(calculatedMetricCreator);
        return calculatedMetricCreator;
    }

    private Predicate<CSVRecord> createPredicate(Config.Filter f) {
        if (!REGEX_MATCH.equals(f.operator())) {
            throw new RuntimeException("Operator " + f.operator() + " is not supported.");
        }
        if (!FIELDS.contains(f.operand())) {
            throw new RuntimeException("operand must be one of  " + FIELDS + "; Found: " + f.operand());
        }
        return new Predicate<CSVRecord>() {
            private final Pattern pattern = Pattern.compile(f.value());

            @Override
            public boolean test(CSVRecord rec) {
                return pattern.matcher(rec.get(f.operand())).matches();
            }
        };
    }

    private List<PeriodicProcessor<CSVRecord>> createLogConsumers(List<Config.LogConsumer> rawLogConsumers) {
        return rawLogConsumers.stream().map(config -> {
            try {
                return config.type().getConstructor(String.class, Duration.class)
                        .newInstance(config.name(), config.period());
            } catch (InstantiationException e) {
                throw new RuntimeException(e);
            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            } catch (InvocationTargetException e) {
                throw new RuntimeException(e);
            } catch (NoSuchMethodException e) {
                throw new RuntimeException(e);
            }

        }).collect(Collectors.toList());
    }

    private void alarmsFor(List<Config.Alarm> alarms, Map<String, SimpleMetricCreator> simpleMetrics,
                           Map<String, CalculatedMetricCreator> calculatedMetrics) {
        alarms.stream().map(config -> alarmFor(config, simpleMetrics, calculatedMetrics)).collect(Collectors.toList());
    }

    private AlarmProcessor alarmFor(Config.Alarm config, Map<String, SimpleMetricCreator> simpleMetrics,
                                    Map<String, CalculatedMetricCreator> calculatedMetrics) {
        String metric = config.metric();
        BaseMetricCreator<?> dependentMetric = null;
        if (simpleMetrics.containsKey(metric)) {
            dependentMetric = simpleMetrics.get(metric);
        } else if (calculatedMetrics.containsKey(metric)) {
            dependentMetric = calculatedMetrics.get(metric);
        }
        if (dependentMetric == null) {
            throw new RuntimeException("Dependent metric " + metric + " not found for alarm: " + config.name());
        }
        AlarmProcessor alarmProcessor = new AlarmProcessor(config.name(), config.threshold(),
                config.dataPointsAlarm(), config.dataPointsRecovery(), dependentMetric.period(), metric);
        dependentMetric.addConsumer(alarmProcessor);
        return alarmProcessor;
    }

    private Map<String, CalculatedMetricCreator> calculatedMetricCreatorsFor(
            List<Config.CalculatedMetric> calculatedMetrics, Map<String, SimpleMetricCreator> simpleMetrics) {
        return calculatedMetrics.stream()
                .map(m -> calculatedMetricCreatorFor(m, simpleMetrics))
                .collect(Collectors.toMap(CalculatedMetricCreator::name, Function.identity()));
    }

    private Map<String, SimpleMetricCreator> simpleMetricCreatorsFor(List<Config.Metric> metrics) {
        return metrics.stream()
                .map(m -> new SimpleMetricCreator(m.name(), m.period(), createPredicate(m.filters()), m.type()))
                .collect(Collectors.toMap(SimpleMetricCreator::name, Function.identity()));
    }

    private Optional<Predicate<CSVRecord>> createPredicate(List<Config.Filter> filters) {
        return filters.stream().map(this::createPredicate).reduce(Predicate::and);
    }
}