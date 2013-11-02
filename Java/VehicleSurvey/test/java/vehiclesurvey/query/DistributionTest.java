package vehiclesurvey.query;

import com.google.common.base.Predicate;
import org.hamcrest.Matchers;
import org.junit.Test;
import vehiclesurvey.DriveThru;
import vehiclesurvey.DriveThruList;

import static com.google.common.collect.Iterables.getLast;
import static com.google.common.collect.Iterables.toArray;
import static com.google.common.collect.Iterables.get;
import static com.google.common.collect.Iterables.getFirst;
import static org.hamcrest.Matchers.arrayWithSize;
import static org.junit.Assert.*;
import static vehiclesurvey.DriveThruFixture.aDriveThru;
import static vehiclesurvey.DriveThrusFixture.driveThrus;
import static vehiclesurvey.query.Distribution.*;
import static vehiclesurvey.time.Time.time;

public class DistributionTest {

    @Test
    public void shouldCreateSlotsForSpeedDistribution() {
        DriveThruList driveThrus = driveThrus(
                aDriveThru().driveAt(40).build(),
                aDriveThru().driveAt(50).build(),
                aDriveThru().driveAt(60).build(),
                aDriveThru().driveAt(30).build(),
                aDriveThru().driveAt(43).build(),
                aDriveThru().driveAt(55).build()
        );
        assertThat(speeds(driveThrus), Matchers.<Predicate<DriveThru>>iterableWithSize(31));
        assertThat(speeds(driveThrus, 5), Matchers.<Predicate<DriveThru>>iterableWithSize(7));
        Predicate<DriveThru>[] speeds = toArray(speeds(driveThrus, 10), Predicate.class);
        assertThat(speeds, arrayWithSize(4));

        Predicate<DriveThru> range30To40 = speeds[0];
        assertTrue(range30To40.apply(aDriveThru().driveAt(33).build()));
        assertTrue(range30To40.apply(aDriveThru().driveAt(35).build()));
        assertFalse(range30To40.apply(aDriveThru().driveAt(40).build()));

        Predicate<DriveThru> speed60 = speeds[speeds.length - 1];
        assertFalse(speed60.apply(aDriveThru().driveAt(59.9).build()));
        assertFalse(speed60.apply(aDriveThru().driveAt(61).build()));
        assertTrue(speed60.apply(aDriveThru().driveAt(60).build()));
    }


    @Test
    public void shouldCreateHourlyDistribution() {
        Iterable<Predicate<DriveThru>> predicates = hours(2);
        assertThat(predicates, Matchers.<Predicate<DriveThru>>iterableWithSize(12));
        assertThat(predicates, Matchers.<Predicate<DriveThru>>iterableWithSize(12)); //should create new iterator 2nd time

        Predicate<DriveThru> range22to24Hrs = getLast(predicates);
        assertTrue(range22to24Hrs.apply(aDriveThru().atTime(time().hours(22)).build()));
        assertTrue(range22to24Hrs.apply(aDriveThru().atTime(time().hours(23).minutes(59)).build()));
        assertFalse(range22to24Hrs.apply(aDriveThru().atTime(time().hours(24)).build()));
    }

    @Test
    public void shouldDailyDistribution() {
        DriveThruList driveThrus = driveThrus(aDriveThru().onDay(4).build());
        Iterable<Predicate<DriveThru>> predicates = days(driveThrus);
        assertThat(predicates, Matchers.<Predicate<DriveThru>>iterableWithSize(4));
        assertTrue(getLast(predicates).apply(driveThrus.get(0)));
        assertFalse(getFirst(predicates, null).apply(driveThrus.get(0)));
        assertFalse(get(predicates, 2, null).apply(driveThrus.get(0)));

    }

}
