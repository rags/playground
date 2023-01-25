package com.datadog.monitoring;

import com.datadog.monitoring.config.Config;
import com.datadog.monitoring.processor.LogDistributor;
import com.datadog.monitoring.processor.ProcessorFactory;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;

import java.io.*;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        // Comment the line above and uncomment the one below to read from file instead of input stream.
        //BufferedReader f = new BufferedReader(new FileReader("/path/to/sample_csv.txt"));
        Config config = Config.initialize();
        try (LogDistributor processor = new ProcessorFactory().createProcessors(config);
             CSVParser parser = CSVFormat.RFC4180
                .builder()
                .setHeader(Config.FIELDS.toArray(String[]::new))
                .setSkipHeaderRecord(true)
                .build()
                .parse(f)) {
            parser.forEach(processor);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}