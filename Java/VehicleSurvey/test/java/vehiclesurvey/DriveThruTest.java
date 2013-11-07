package vehiclesurvey;

import com.google.common.collect.Range;
import org.junit.Test;
import vehiclesurvey.time.Time;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.*;
import static vehiclesurvey.DriveThruFixture.aDriveThru;
import static vehiclesurvey.time.Time.time;

public class DriveThruTest {
    @Test
    public void shouldTellIfDriveThroughWasInATimeRange() {
        Time tenthMin = time().minutes(10);
        DriveThru driveThru = aDriveThru().atTime(tenthMin).build();
        assertFalse(driveThru.wasBetween(Range.closedOpen(time().minutes(5), tenthMin)));
        assertTrue(driveThru.wasBetween(Range.closedOpen(tenthMin, time().minutes(15))));
        assertTrue(driveThru.wasBetween(Range.closedOpen(time().minutes(9), time().minutes(15))));
        assertTrue(driveThru.wasBetween(Range.closedOpen(time(1000 * 59 + 999).minutes(9), time(1).minutes(10)))); //between -1ms +1ms
    }

    @Test
    public void shouldMergeDups() {
        DriveThru driveThruAt10 = aDriveThru().atTime(time().minutes(10)).build();
        assertFalse(driveThruAt10.mergeIfDuplicate(aDriveThru().atTime(time().minutes(11)).build()));// 1 min diff
        assertFalse(driveThruAt10.mergeIfDuplicate(aDriveThru().atTime((time(500).minutes(10))).build()));// 500ms diff

        DriveThru driveThruA = aDriveThru().atTime(time().hours(12)).build();
        DriveThru driveThruB = aDriveThru().atTime(DriveThru.DUPLICATE_THERSHOLD.hours(12)).driveAt(80d).build();
        assertTrue(driveThruA.mergeIfDuplicate(driveThruB));
        assertThat(driveThruA.direction, is(Direction.South));
        assertThat(driveThruA.speed, is(70d));

    }


}
