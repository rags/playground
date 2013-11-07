package vehiclesurvey;

import com.google.common.collect.Range;
import vehiclesurvey.time.Time;

import static vehiclesurvey.time.Time.time;

public class DriveThru {
    static final Time DUPLICATE_THERSHOLD = time(10);
    public static final Double AVG_SPEED_KMPH = 60d;
    final int day;
    final Time time;
    double speed;
    Direction direction;

    public DriveThru(int day, Time time, double speed, Direction direction) {
        this.day = day;
        this.time = time;
        this.speed = speed;
        this.direction = direction;
    }

    public DriveThru(int day, int milliseconds, double speed, Direction direction) {
        this(day, time(milliseconds), speed, direction);
    }

    public DriveThru(int day, int milliseconds, double speed) {
        this(day, milliseconds, speed, Direction.North);
    }

    private void setDirection(Direction direction) {
        this.direction = direction;
    }

    public boolean mergeIfDuplicate(DriveThru other) {
        if (other.time.difference(time).compareTo(DUPLICATE_THERSHOLD) > 0) {
            return false;
        }
        speed = (speed + other.speed) / 2;
        setDirection(Direction.South);
        return true;
    }

    @Override
    public String toString() {
        return "DriveThru{" +
                "day=" + day +
                ", time=" + time +
                ", speed=" + speed +
                ", direction=" + direction +
                '}';
    }

    // start>time<=end
    public boolean wasBetween(Range<Time> timeRange) {
        return timeRange.contains(time);
    }

    public boolean onDay(int day) {
        return this.day == day;
    }

    public Double speed() {
        return speed;
    }

    public Direction heading() {
        return direction;
    }

    public Time timeDifference(DriveThru other) {
        return time.difference(other.time);
    }
}
