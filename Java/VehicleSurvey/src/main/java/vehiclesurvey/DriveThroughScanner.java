package vehiclesurvey;

import com.google.common.base.Optional;
import com.google.common.collect.ImmutableMap;
import com.google.common.io.Files;

import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayDeque;
import java.util.Queue;

import static com.google.common.collect.Iterables.getLast;
import static vehiclesurvey.time.Time.HOUR;

class DriveThruBuilder {
    private Queue<Integer> timeStamps;
    private int day = 1;
    private int lastseen = -1;
    public static final double CAR_LENGTH = 2.5 / 1000;//in km
    public static final int AXEL_TIME_THRESHOLD_LOWER = 75; //120 KMPH


    DriveThruBuilder() {
        timeStamps = new ArrayDeque<Integer>();
        day = 1;
    }

    public Optional<DriveThru> addTimeStamp(int timestamp) {
        if (timestamp < lastseen) {
            day += 1;
        }
        lastseen = timestamp;
        if (timeStamps.isEmpty() || isConcurrentDriveThru(timestamp)) {
            timeStamps.add(timestamp);
            return Optional.absent();
        }
        Integer axel1Timestamp = timeStamps.remove();
        return Optional.of(new DriveThru(day, axel1Timestamp, CAR_LENGTH / (timestamp - axel1Timestamp) * HOUR));
    }

    private boolean isConcurrentDriveThru(int timestamp) {
        return timestamp - timeStamps.peek() < AXEL_TIME_THRESHOLD_LOWER;
    }
}

public class DriveThroughScanner {
    public DriveThruList scan(File file) {
        try {
            return scan(Files.newReader(file, Charset.defaultCharset()));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    private DriveThruList scan(BufferedReader bufferedReader) {
        try {
            ImmutableMap<Character, DriveThruList> driveThruLists = ImmutableMap.of('A', new DriveThruList(), 'B', new DriveThruList());
            ImmutableMap<Character, DriveThruBuilder> driveThruBuilders = ImmutableMap.of('A', new DriveThruBuilder(), 'B', new DriveThruBuilder());
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                char category = line.charAt(0);
                Optional<DriveThru> driveThruOptional = driveThruBuilders.get(category).addTimeStamp(Integer.parseInt(line.substring(1)));
                if (driveThruOptional.isPresent()) {
                    driveThruLists.get(category).add(driveThruOptional.get());
                    mergeDuplicates(driveThruLists.get('A'), driveThruLists.get('B'));
                }
            }
            assert driveThruLists.get('B').isEmpty();
            return driveThruLists.get('A');
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void mergeDuplicates(DriveThruList as, DriveThruList bs) {
        if (bs.isEmpty() || as.isEmpty()) {
            return;
        }
        while (!bs.isEmpty()) {
            if (!getLast(as).mergeIfDuplicate(getLast(bs))) {
                return;
            }
            bs.remove(bs.size() - 1);
        }
    }

    public DriveThruList scan(InputStream resourceAsStream) {
        return scan(new BufferedReader(new InputStreamReader(resourceAsStream)));
    }
}
