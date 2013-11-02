package vehiclesurvey;

import org.hamcrest.CustomTypeSafeMatcher;
import org.hamcrest.Matcher;
import org.hamcrest.core.AllOf;
import vehiclesurvey.time.Time;

import java.util.ArrayList;
import java.util.Collection;

import static java.lang.Math.abs;
import static vehiclesurvey.time.Time.time;


/*
* A fluent interface for matchers someDriveThru().atTime(1234).withSpeed(62.1).....
* */
public class DriveThruMatcher extends CustomTypeSafeMatcher<DriveThru> {

    private Collection<Matcher<DriveThru>> matchers;

    public DriveThruMatcher() {
        super("Composite matcher");
        matchers = new ArrayList<Matcher<DriveThru>>();
    }

    @Override
    protected boolean matchesSafely(DriveThru item) {
        return new AllOf(matchers).matches(item);
    }

    public static DriveThruMatcher someDriveThru() {
        return new DriveThruMatcher();
    }

    public DriveThruMatcher atTime(int timeStamp) {
        final Time time = time(timeStamp);
        matchers.add(new CustomTypeSafeMatcher<DriveThru>("Expected drive through with time: " + time) {
            @Override
            protected boolean matchesSafely(DriveThru item) {
                return time.equals(item.time);
            }
        });
        return this;
    }

    public DriveThruMatcher onDay(final int day) {
        matchers.add(new CustomTypeSafeMatcher<DriveThru>("Expected drive through on day: " + day) {
            @Override
            protected boolean matchesSafely(DriveThru item) {
                return item.day == day;
            }
        });
        return this;
    }

    public DriveThruMatcher withSpeed(final double speed) {
        matchers.add(new CustomTypeSafeMatcher<DriveThru>("Expected drive through with speed: " + speed) {
            @Override
            protected boolean matchesSafely(DriveThru item) {
                return abs(item.speed - speed) < .01;
            }
        });
        return this;
    }
}
