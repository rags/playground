package vehiclesurvey;

import com.google.common.io.Files;
import vehiclesurvey.query.DriveThruPredicates;
import vehiclesurvey.query.QueryProcessor;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static java.lang.String.format;
import static java.lang.String.valueOf;
import static java.util.Arrays.asList;
import static vehiclesurvey.query.DriveThruFilters.*;
import static vehiclesurvey.query.QueryImpl.aggregateAvg;
import static vehiclesurvey.query.QueryImpl.select;

//No tests for this class
public class ReportGenerator {
    private final DriveThruList driveThrus;
    private File reportFolder;

    public ReportGenerator(String reportFolder) {
        this.reportFolder = new File(reportFolder);
        driveThrus = parseDriveThrus();
    }

    public static void main(String[] args) throws URISyntaxException {
        new ReportGenerator("reports").run();
    }

    private void run() {
        mkdirs();
        System.out.println(format("Exporting %d drive through to CSV", driveThrus.size()));
        exportToCsv();
        System.out.println("Generating count and avg counts across days reports for 15,20,30 min, 1 hour, morning/evening");
        countReportsForTimePeriods();
        System.out.println("Generating peak volume reports");
        peakVolumeReports();
        System.out.println("Generating speed distribution reports");
        speedDistributionReports();
        System.out.println("Distance between cars for  15,20,30 min, 1 hour, morning/evening");
        distancesReports();
    }

    private void distancesReports() {
        for (Map.Entry<String, DriveThruPredicates> tuple : timePeriods().entrySet()) {
            QueryProcessor result = select(DriveThru.class)
                    .groupBy(direction())
                    .groupBy(tuple.getValue())
                    .groupBy(days(driveThrus))
                    .aggregate(avgDistanceBetweenCars()).execute(driveThrus).aggregateAggregates(aggregateAvg());
            BufferedWriter bufferedWriter = null;
            try {
                bufferedWriter = writerFor("car-distances/every-" + tuple.getKey() + ".txt");
                bufferedWriter.append("Format: <start time>_<end time> = <avg distance> in KM\n\n");
                for (Direction direction : Direction.values()) {
                    bufferedWriter.write(direction.name());
                    bufferedWriter.write("\n-------------------------\n");
                    QueryProcessor<QueryProcessor> dataForDirection = result.resultFor(direction);
                    writeLeafData(bufferedWriter, dataForDirection);
                }
            } catch (Exception e) {
                throw new RuntimeException(e);
            } finally {
                close(bufferedWriter);
            }
        }

    }

    private void mkdirs() {
        for (String dirname : new String[]{"count", "count-avg", "peak-volume", "speed-distributions", "car-distances"}) {
            File subFolder = new File(reportFolder, dirname);
            if (!subFolder.exists()) {
                subFolder.mkdirs();
            }
        }
    }

    private void peakVolumeReports() {
        List<DriveThruPredicates> predicatesList = asList(hours(1), hours(2));
        for (int i = 0; i < predicatesList.size(); i++) {
            QueryProcessor result = select(DriveThru.class)
                    .groupBy(direction())
                    .groupBy(predicatesList.get(i))
                    .groupBy(days(driveThrus)).countAvg()
                    .execute(driveThrus).filterAggregates(aggregateAllMax());

            BufferedWriter bufferedWriter = null;
            try {
                bufferedWriter = writerFor("peak-volume/" + (i + 1) + "-hour-slots.txt");
                bufferedWriter.append("Peak volume report based on " + (i + 1) + " hour time slots\n")
                        .append("Format: <start time>_<end time> = <avg drive by counts>\n\n");
                for (Direction direction : Direction.values()) {
                    bufferedWriter.write(direction.name());
                    bufferedWriter.write("\n-------------------------\n");
                    QueryProcessor<QueryProcessor> dataForDirection = result.resultFor(direction);
                    writeLeafData(bufferedWriter, dataForDirection);
                }
            } catch (Exception e) {
                throw new RuntimeException(e);
            } finally {
                close(bufferedWriter);
            }

        }
    }

    private void speedDistributionReports() {
        List<DriveThruPredicates> predicatesList = asList(speeds(driveThrus), speeds(driveThrus, 2));
        for (int i = 0; i < predicatesList.size(); i++) {
            QueryProcessor<QueryProcessor> result = select(DriveThru.class).groupBy(predicatesList.get(i)).count().execute(driveThrus);

            BufferedWriter bufferedWriter = null;
            try {
                bufferedWriter = writerFor("speed-distributions/" + (i + 1) + "-KMPH-slots.txt");
                bufferedWriter.append("Speed distribution report based on " + (i + 1) + " KMPH speed slots\n")
                        .append("Format: <min speed>_<max speed> = % distribution (<counts>)\n\n");
                for (QueryProcessor processor : result.results()) {
                    QueryProcessor percentage = processor.map(percentMapper(driveThrus.size()));
                    bufferedWriter.append(processor.scope().toString())
                            .append(" = ")
                            .append(percentage.scalarResult().toString())
                            .append("% (")
                            .append(processor.scalarResult().toString())
                            .append(')')
                            .append('\n');
                }

            } catch (Exception e) {
                throw new RuntimeException(e);
            } finally {
                close(bufferedWriter);
            }

        }
    }

    private void countReportsForTimePeriods() {
        for (Map.Entry<String, DriveThruPredicates> tuple : timePeriods().entrySet()) {
            countReportForEachDay(tuple);
            countReportAvgAcrossDays(tuple);
        }
    }

    private void countReportAvgAcrossDays(Map.Entry<String, DriveThruPredicates> tuple) {
        QueryProcessor result = select(DriveThru.class)
                .groupBy(direction()).groupBy(tuple.getValue())
                .groupBy(days(driveThrus)).countAvg().execute(driveThrus);
        BufferedWriter bufferedWriter = null;
        try {
            bufferedWriter = writerFor("count-avg/every-" + tuple.getKey() + ".txt");
            for (Direction direction : Direction.values()) {
                bufferedWriter.write(direction.name());
                bufferedWriter.write("\n-------------------------\n");
                QueryProcessor<QueryProcessor> dataForDirection = result.resultFor(direction);
                writeLeafData(bufferedWriter, dataForDirection);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            close(bufferedWriter);
        }

    }

    private void countReportForEachDay(Map.Entry<String, DriveThruPredicates> tuple) {
        QueryProcessor result = select(DriveThru.class)
                .groupBy(direction()).groupBy(days(driveThrus))
                .groupBy(tuple.getValue()).count().execute(driveThrus);
        BufferedWriter bufferedWriter = null;
        try {
            bufferedWriter = writerFor("count/every-" + tuple.getKey() + ".txt");

            for (Direction direction : Direction.values()) {
                bufferedWriter.append(direction.name())
                        .append("\n-------------------------\n");
                QueryProcessor<QueryProcessor> dataForDirection = result.resultFor(direction);

                for (int day : new int[]{1, 2, 3, 4, 5}) {
                    bufferedWriter.append(format("Data for day %d\n______________________\n", day));
                    QueryProcessor dataForDay = dataForDirection.resultFor(day);
                    writeLeafData(bufferedWriter, dataForDay);
                }
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            close(bufferedWriter);
        }

    }

    private void writeLeafData(BufferedWriter bufferedWriter, QueryProcessor<QueryProcessor> leafData) throws IOException {
        for (QueryProcessor processor : leafData.results()) {
            bufferedWriter.append(processor.scope().toString())
                    .append(" = ")
                    .append(processor.scalarResult().toString()).append('\n');
        }
    }

    private HashMap<String, DriveThruPredicates> timePeriods() {
        return new HashMap<String, DriveThruPredicates>() {{
            put("15-minutes", minutes(15));
            put("20-minutes", minutes(20));
            put("30-minutes", minutes(30));
            put("1-hour", hours(1));
            put("morning-evening", morningEvening());
        }};
    }

    private void exportToCsv() {
        BufferedWriter bufferedWriter = null;
        try {
            bufferedWriter = writerFor("drive-thrus.csv");
            for (DriveThru driveThru : driveThrus) {
                bufferedWriter.append(valueOf(driveThru.day))
                        .append(',')
                        .append(valueOf(driveThru.time.millis()))
                        .append(',')
                        .append(valueOf(driveThru.speed))
                        .append(',')
                        .append(driveThru.direction.name())
                        .append('\n');
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            close(bufferedWriter);
        }
    }

    private BufferedWriter writerFor(String fileName) throws FileNotFoundException {
        return Files.newWriter(new File(reportFolder, fileName), Charset.defaultCharset());
    }

    private void close(BufferedWriter bufferedWriter) {
        try {
            if (bufferedWriter != null) {
                bufferedWriter.flush();
                bufferedWriter.close();
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private static DriveThruList parseDriveThrus() {
        return new DriveThroughScanner().scan(ReportGenerator.class.getResourceAsStream("sample.txt"));
    }

}
