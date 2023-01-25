package com.datadog.monitoring.processor;

import com.datadog.monitoring.config.Config;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;

import java.io.IOException;
import java.io.StringReader;

public class CsvFixture {
    public static CSVParser getCsvRecords(String csv) {
        try {
            return CSVFormat.RFC4180
                    .builder()
                    .setHeader(Config.FIELDS.toArray(String[]::new)).build().parse(new StringReader(
                            csv
                    ));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
