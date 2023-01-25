package com.datadog.monitoring.config;

import com.datadog.monitoring.processor.api.PeriodicProcessor;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.apache.commons.csv.CSVRecord;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.DateFormat;
import java.time.Duration;
import java.util.*;


public class Config {

    public static final String DATE = "date";
    public static final String REQUEST = "request";
    public static final String STATUS = "status";
    public static final Set<String> FIELDS = new LinkedHashSet<>(Arrays.asList("remotehost", "rfc931", "authuser", DATE,
            REQUEST,
            STATUS,
            "bytes"));
    public static final DateFormat TIMEFORMAT =
            DateFormat.getDateTimeInstance(DateFormat.SHORT, DateFormat.MEDIUM);
    public static final String COUNT = "COUNT";
    public static final String REGEX_MATCH = "=~";
    final private List<Metric> metrics;
    final private List<CalculatedMetric> calculatedMetrics;
    final private List<Alarm> alarms;
    final private List<LogConsumer> rawLogConsumers;

    public List<Metric> simpleMetrics() {
        return metrics;
    }

    public List<CalculatedMetric> calculatedMetrics() {
        return calculatedMetrics;
    }

    public List<Alarm> alarms() {
        return alarms;
    }

    public List<LogConsumer> rawLogConsumers() {
        return rawLogConsumers;
    }

    @JsonCreator
    public Config(@JsonProperty("metrics") List<Metric> metrics,
                  @JsonProperty("calculatedMetrics") List<CalculatedMetric> calculatedMetrics,
                  @JsonProperty("alarms") List<Alarm> alarms,
                  @JsonProperty("rawLogConsumers") List<LogConsumer> rawLogConsumers) {
        this.metrics = metrics==null?new ArrayList<>() : metrics;
        this.calculatedMetrics = calculatedMetrics==null?new ArrayList<>() : calculatedMetrics;
        this.alarms = alarms==null?new ArrayList<>() : alarms;
        this.rawLogConsumers = rawLogConsumers==null?new ArrayList<>():rawLogConsumers;
    }

    public static Config initialize() {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.registerModule(new JavaTimeModule());
        Config config;
        try {
            config = objectMapper.readerFor(Config.class).readValue(configLocation());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return config;
    }

    /**
     * If no override is specified via -Dconf=/path/to/config.json then the
     * default config packaged in resources will be used.
     *
     * @return URL of config
     */
    private static URL configLocation() {
        if (System.getProperties().containsKey("conf")) {
            try {
                return new URL("file://" + System.getProperty("conf"));
            } catch (MalformedURLException e) {
                throw new RuntimeException(e);
            }
        }
        return Config.class.getClassLoader().getResource("config.json");
    }

    public static void main(String[] args) throws IOException {
        Config c = Config.initialize();
        c.alarms.forEach(m-> System.out.println(m.name +" " + m.threshold + " " +
                m.dataPointsAlarm + " " + m.dataPointsRecovery));
    }

    public enum Aggregate {
        COUNT,
        SUM,
        AVG,
        MAX
    }


    public static class Metric {
        final private String name;
        final private Duration period;
        final private String type;
        final private List<Filter> filters;

        @JsonCreator
        public Metric(@JsonProperty("name") String name, @JsonProperty("period") Duration period,
                      @JsonProperty("type") String type,
                      @JsonProperty("filters") List<Filter> filters) {
            this.name = name;
            this.period = period;
            this.type = type==null? COUNT :type;
            this.filters = filters==null? Collections.emptyList(): filters;
        }

        public String name() {
            return name;
        }

        public Duration period() {
            return period;
        }

        public String type() {
            return type;
        }

        public List<Filter> filters() {
            return filters;
        }

    }

    public static class CalculatedMetric {
        final private String name;
        final private Duration period;
        final private Aggregate aggregate;
        private final List<String> inputMetrics;

        @JsonCreator(mode = JsonCreator.Mode.PROPERTIES)
        public CalculatedMetric(@JsonProperty("name") String name, @JsonProperty("period") Duration period,
                                @JsonProperty("aggregate") Aggregate aggregate,
                                @JsonProperty("inputMetrics") List<String> inputMetrics) {
            this.name = name;
            this.period = period;
            this.aggregate = aggregate;
            this.inputMetrics = inputMetrics;
        }

        public String name() {
            return name;
        }

        public Duration period() {
            return period;
        }

        public Aggregate aggregate() {
            return aggregate;
        }

        public String parent() {
            if (inputMetrics.isEmpty()) {
                throw new RuntimeException("Metric " + name + " does not have a parent metric");
            }
            return inputMetrics.get(0);
        }
    }

    public static class Alarm {
        final private String name;
        final private double threshold;

        final private String metric;
        final private int dataPointsAlarm;
        final private int dataPointsRecovery;

        @JsonCreator
        public Alarm(@JsonProperty("name") String name, @JsonProperty("threshold") double threshold,
                     @JsonProperty("metric") String metric, @JsonProperty("dataPointsAlarm") int dataPointsAlarm,
                     @JsonProperty("dataPointsRecovery") int dataPointsRecovery) {
            this.name = name;
            this.threshold = threshold;
            this.metric = metric;
            this.dataPointsAlarm = dataPointsAlarm;
            this.dataPointsRecovery = dataPointsRecovery;
        }

        public String name() {
            return name;
        }

        public double threshold() {
            return threshold;
        }

        public String metric() {
            return metric;
        }

        public int dataPointsAlarm() {
            return dataPointsAlarm;
        }

        public int dataPointsRecovery() {
            return dataPointsRecovery;
        }
    }

    public static class LogConsumer {
        final private String name;
        final private Class<PeriodicProcessor<CSVRecord>> type;
        final private Duration period;

        @JsonCreator
        public LogConsumer(@JsonProperty("name") String name, @JsonProperty("type") Class<PeriodicProcessor<CSVRecord>> type,
                      @JsonProperty("period") Duration period) {
            this.name = name;
            this.period = period;
            this.type = type;
        }

        public String name() {
            return name;
        }

        public Class<PeriodicProcessor<CSVRecord>> type() {
            return type;
        }

        public Duration period() {
            return period;
        }
    }

    public static class Filter {
        /**
         * Operator for the filter. Currently only regex operator '=~' is supported
         * In future this can be things like =, !=, >,<
         */
        private final String operator;
        /**
         * A field in the log file.
         */
        private final String operand;
        private final String value;

        @JsonCreator(mode= JsonCreator.Mode.PROPERTIES)
        public Filter(@JsonProperty("operator") String operator, @JsonProperty("operand") String operand,
                      @JsonProperty("value") String value) {
            this.operator = operator;
            this.operand = operand;
            this.value = value;
        }

        public String operator() {
            return operator;
        }

        public String operand() {
            return operand;
        }

        public String value() {
            return value;
        }

    }

}
