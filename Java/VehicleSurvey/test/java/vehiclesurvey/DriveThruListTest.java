package vehiclesurvey;

import org.junit.Test;

import static org.hamcrest.Matchers.closeTo;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.DriveThruFixture.aDriveThru;
import static vehiclesurvey.DriveThrusFixture.driveThrus;
import static vehiclesurvey.time.Time.time;

public class DriveThruListTest {
    @Test
    public void shouldCalculateDistancesBetweenCars(){
      assertThat(driveThrus().avgDistanceBetweenCars(),is(0d));
      assertThat(driveThrus(aDriveThru().build()).avgDistanceBetweenCars(),is(0d));
       assertThat(driveThrus(
               aDriveThru().atTime(time().minutes(1)).build(),
               aDriveThru().atTime(time().minutes(2)).build()
       ).avgDistanceBetweenCars(), is(1d));

        assertThat(driveThrus(
               aDriveThru().atTime(time().minutes(1)).build(),
               aDriveThru().atTime(time().minutes(2)).build(),
               aDriveThru().atTime(time().minutes(4)).build()
       ).avgDistanceBetweenCars(), is(1.5));

        assertThat(driveThrus(
               aDriveThru().atTime(time().seconds(1)).build(),
               aDriveThru().atTime(time().seconds(3)).build(),
               aDriveThru().atTime(time().seconds(5)).build()
       ).avgDistanceBetweenCars(), is(closeTo(0.03333,.0001)));
    }
}
