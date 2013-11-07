package vehiclesurvey.time;

import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.String.format;

public class Time implements Comparable<Time> {
    private static final int SECOND = 1000;
    private static final int MINUTE = SECOND * 60;
    public static final int HOUR = MINUTE * 60;
    public static final Time MIN = time();
    public static final Time MAX = time(HOUR * 24);

    private final int milliseconds;


    private Time(int milliseconds) {
        this.milliseconds = milliseconds;
    }

    public static Time time() {
        return time(0);
    }

    public static Time time(int i) {
        return new Time(i);
    }

    @Override
    public String toString() {
        int hours = milliseconds / HOUR;
        int remaining = milliseconds % HOUR;
        int minutes = remaining / MINUTE;
        int seconds = (remaining % MINUTE) / SECOND;
        return format("%02d:%02d:%02d", hours, minutes, seconds);
    }

    public Time minutes(int mins) {
        return new Time(milliseconds + MINUTE * mins);
    }

    public Time seconds(int secs) {
        return new Time(milliseconds + SECOND * secs);
    }

    public Time hours(int hours) {
        return new Time(milliseconds + HOUR * hours);
    }

    public Time difference(Time other) {
        return new Time(max(milliseconds, other.milliseconds) - min(milliseconds, other.milliseconds));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Time time = (Time) o;

        if (milliseconds != time.milliseconds) return false;

        return true;
    }

    @Override
    public int hashCode() {
        return milliseconds;
    }

    @Override
    public int compareTo(Time other) {
        return milliseconds - other.milliseconds;
    }

    public int millis() {
        return milliseconds;
    }
}
