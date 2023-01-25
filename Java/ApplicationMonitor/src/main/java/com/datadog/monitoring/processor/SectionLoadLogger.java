package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.model.Stats;
import com.datadog.monitoring.processor.api.PeriodicProcessor;
import org.apache.commons.csv.CSVRecord;

import java.io.PrintStream;
import java.time.Duration;
import java.time.Instant;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Accumulates stats for all sections and periodically logs stats for section with maximum hits.
 */
public class SectionLoadLogger extends PeriodicProcessor<CSVRecord> {
    private static final String METHOD = "method";
    private static final String SECTION = "section";
    // Explanation:
    // begin->(method)->space+->(section)
    // method = any non whitespace char
    // section = / followed by any non-whitespace char other than /
    public static final Pattern REQUEST_MATCHER = Pattern.compile("^(?<" + METHOD + ">[\\S]+)\\s+(?<" + SECTION +
                                                                  ">/[^/\\s]*)");
    private final PrintStream out;
    final private Map<String, Stats> stats;

    public SectionLoadLogger(String name, Duration period) {
        this(name, period, System.out);
    }

    SectionLoadLogger(String name, Duration period, PrintStream out) {
        super(name, period);
        this.stats = new HashMap<>();
        this.out = out;
    }


    private void println(String message) {
        out.println("[" + name + "] - [" + dateStr(startTime()) + " - " + dateStr(endTime()) +
                    "] " + message);
    }

    private static String dateStr(Instant instant) {
        return Config.TIMEFORMAT.format(Date.from(instant));
    }


    @Override
    protected void process(CSVRecord rec) {
        Matcher matcher = REQUEST_MATCHER.matcher(rec.get(Config.REQUEST));
        if (!matcher.find()) {
            // TODO: We might want to ignore malformed records and continue processing
            throw new RuntimeException("Malformed url");
        }
        String section = matcher.group(SECTION);
        String method = matcher.group(METHOD);
        Stats stat = this.stats.getOrDefault(section, new Stats(section));

        stat.addHits(1);
        // TODO: For now only GET/POST. Support PUT, DELETE other http methods
        if ("POST".equalsIgnoreCase(method)) {
            stat.addPost(1);
        } else if ("GET".equalsIgnoreCase(method)) {
            stat.addGet(1);
        }
        String status = rec.get(Config.STATUS);
        if (status.startsWith("5")) {
            stat.add5xx(1);
        } else if (status.startsWith("4")) {
            stat.add4xx(1);
        } else {
            stat.addSuccess(1);
        }
        this.stats.put(section, stat);
    }

    @Override
    protected void flushResultImpl() {
        Stats maxHits =
                stats.values().stream().reduce(Stats.NULL, (s1, s2) -> s1.totalHits() > s2.totalHits() ? s1 : s2);
        if (maxHits == Stats.NULL) {
            println("No hits for the interval");
        } else {
            println("Max " + SECTION + " stats for the interval is: " + maxHits);
        }
        stats.clear();
    }

    @Override
    protected Instant getTime(CSVRecord rec) {
        return Instant.ofEpochSecond(Long.parseUnsignedLong(rec.get(Config.DATE)));
    }
}
