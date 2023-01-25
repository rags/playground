package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Metric;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.time.Instant;
import java.util.Optional;
import java.util.function.Predicate;
import java.util.regex.Pattern;

import static com.datadog.monitoring.processor.CsvFixture.getCsvRecords;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class SimpleMetricCreatorTest {
    private StubConsumers<Metric> consumers;

    @BeforeEach
    void setUp() {
        consumers = new StubConsumers<>();

    }

    @Test
    void testLoggingOfMaxHits() {
        SimpleMetricCreator simpleMetricCreator = new SimpleMetricCreator("foo", Duration.ofSeconds(5), consumers);
        CSVParser csvRecords = getCsvRecords("\"10.0.0.3\",\"-\",\"apache\",1549574330,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574330,\"POST /report HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.4\",\"-\",\"apache\",1549574330,\"GET /api/user HTTP/1.0\",500,1234\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574332,\"GET /report HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574332,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.4\",\"-\",\"apache\",1549574333,\"GET /report HTTP/1.0\",200,1136\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                                        "\"10.0.0.4\",\"-\",\"apache\",1549574334,\"POST /report HTTP/1.0\",404,1307\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",500,1261\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",200,1261\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /report HTTP/1.0\",200,1136\n" +
                                                        "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574337,\"GET /report HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /api/user HTTP/1.0\",200,1307\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /report HTTP/1.0\",200,1307\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574340,\"GET /report HTTP/1.0\",200,1261\n");
        csvRecords.forEach(simpleMetricCreator);
        assertEquals(2, consumers.outputSize());
        assertEquals(new Metric(9, Instant.ofEpochSecond(1549574330)), consumers.output(0));
        assertEquals(new Metric(10, Instant.ofEpochSecond(1549574335)), consumers.output(1));
    }

    @Test
    void testLoggingOfTrailingData() {
        SimpleMetricCreator simpleMetricCreator = new SimpleMetricCreator("foo", Duration.ofSeconds(10), consumers);
        CSVParser csvRecords = getCsvRecords("\"10.0.0.2\",\"-\",\"apache\",1549574336,\"POST /report/user HTTP/1" +
                                                        ".0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574337,\"GET /report HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /api/user HTTP/1.0\",200,1307\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /report HTTP/1.0\",200,1307\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                                        "\"10.0.0.1\",\"-\",\"apache\",1549574340,\"GET /report HTTP/1.0\",200,1261\n");
        //Use auto close to flush trailing data will never hit the period end.
        try(SimpleMetricCreator creator = simpleMetricCreator) {
            csvRecords.forEach(creator);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        assertEquals(1, consumers.outputSize());
        assertEquals(new Metric(6, Instant.ofEpochSecond(1549574336)), consumers.output(0));
    }

    @Test
    void testFilters() {
        // Filter to look at only post requests.
        Predicate<CSVRecord> POST_REQUEST = filter(Config.REQUEST, "^POST.*$");
        Predicate<CSVRecord> SUCCESS_REQUESTS = filter(Config.STATUS, "^2.*$");

        SimpleMetricCreator simpleMetricCreator = new SimpleMetricCreator("foo", Duration.ofSeconds(10),
                Optional.of(POST_REQUEST.and(SUCCESS_REQUESTS)), consumers, Config.COUNT
        ); // Count only POST with 200 response
        CSVParser csvRecords = getCsvRecords("\"10.0.0.3\",\"-\",\"apache\",1549574330,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574330,\"POST /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574330,\"GET /api/user HTTP/1.0\",500,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574332,\"GET /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574332,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574333,\"GET /report HTTP/1.0\",200,1136\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                             "\"10.0.0.4\",\"-\",\"apache\",1549574334,\"POST /report HTTP/1.0\",404,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574334,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",500,1261\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /api/user HTTP/1.0\",200,1194\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574335,\"POST /report HTTP/1.0\",200,1261\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"GET /report HTTP/1.0\",200,1136\n" +
                                             "\"10.0.0.2\",\"-\",\"apache\",1549574336,\"POST /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574337,\"GET /report HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /api/user HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"POST /report HTTP/1.0\",200,1307\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574338,\"GET /api/user HTTP/1.0\",200,1234\n" +
                                             "\"10.0.0.1\",\"-\",\"apache\",1549574340,\"GET /report HTTP/1.0\",200,1261\n");
        csvRecords.forEach(simpleMetricCreator);
        assertEquals(1, consumers.outputSize());
        assertEquals(new Metric(8, Instant.ofEpochSecond(1549574330)), consumers.output(0));
    }

    private static Predicate<CSVRecord> filter(final String field, final String regex) {
        return new Predicate<>() {
            private final Pattern pattern = Pattern.compile(regex);

            @Override
            public boolean test(CSVRecord rec) {
                return pattern.matcher(rec.get(field)).matches();
            }
        };
    }

}