package vehiclesurvey.time;

import org.junit.Test;

import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.time.Time.time;

public class TimeTest {
    @Test
    public void shouldAddHours() {
        assertThat(time().hours(2), is(time(2 * 60 * 60 * 1000)));
    }

    @Test
    public void shouldAddMins() {
        assertThat(time().minutes(2), is(time(2 * 60 * 1000)));
        assertThat(time().minutes(1).hours(2).hours(3).minutes(2), is(time(5 * 60 * 60 * 1000 + 3 * 60 * 1000)));
    }

    @Test
    public void shouldProvideHumanReadableTime() {
        assertThat(time().hours(3).hours(7).minutes(2).toString(), is("10:02:00"));
        assertThat(time().minutes(23).hours(22).toString(), is("22:23:00"));
        assertThat(time().minutes(23).hours(50).toString(), is("50:23:00")); //can add more then 24 hours
    }

    @Test
    public void shouldSubstract() {
        assertThat(time().minutes(3).difference(time().minutes(5)), is(time(2 * 60 * 1000)));
        assertThat(time().minutes(6).difference(time().minutes(2)), is(time(4 * 60 * 1000)));
    }

    @Test
    public void shouldCompare() {

        assertThat(time().minutes(3).compareTo(time().minutes(5)), is(lessThan(0)));
        assertThat(time().minutes(4).compareTo(time().minutes(3)), is(greaterThan(0)));
        assertThat(time().minutes(3).compareTo(time().minutes(3)), is(0));
    }

}
