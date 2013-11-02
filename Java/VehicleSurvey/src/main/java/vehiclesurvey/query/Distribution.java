package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import vehiclesurvey.DriveThru;
import vehiclesurvey.DriveThruList;
import vehiclesurvey.time.Time;

import java.util.Iterator;

import static java.lang.String.format;


interface DriveThruPredicates extends Predicates<DriveThru> {
} //alias to reduce <> clutter

public class Distribution {

    public static Time min(Time time1, Time time2) {
        return time1.compareTo(time2) > 0 ? time2 : time1;
    }


    public static Function<DriveThru, Double> speed() {
        return new Function<DriveThru, Double>() {
            @Override
            public Double apply(DriveThru driveThru) {
                return driveThru.speed();
            }
        };
    }


    public static DriveThruPredicates speeds(DriveThruList driveThrus) {
        return speeds(driveThrus, 1);
    }

    public static DriveThruPredicates speeds(final DriveThruList driveThrus, final int slotSize) {
        final double min = Math.floor(driveThrus.min(speed()));
        Double maxUnrounded = driveThrus.max(speed());
        final double max = Math.ceil(maxUnrounded) == maxUnrounded ? maxUnrounded + .1 : Math.ceil(maxUnrounded);

        return new DriveThruPredicates() {
            @Override
            public Predicates iterator() {

                return new Predicates() {
                    double value = min;

                    @Override
                    public boolean hasNext() {
                        return value < max;
                    }

                    @Override
                    public Predicate<DriveThru> next() {
                        final double start = value;
                        value = Math.min(max, slotSize + value);
                        final double end = value;//closure created from final variable. Field 'value' cannot directly used.
                        return new Predicate<DriveThru>() {
                            @Override
                            public boolean apply(final DriveThru driveThru) {
                                return driveThru.speed() >= start && driveThru.speed() < end;
                            }

                            public String toString() {
                                return format("%f >= [Speed] < %f", start, end);
                            }
                        };
                    }
                };
            }
        };
    }

    public static DriveThruPredicates days(DriveThruList driveThrus) {
        final int max = driveThrus.lastDay();
        return new DriveThruPredicates() {
            @Override
            public Predicates iterator() {

                return new Predicates() {
                    int day = 1;

                    @Override
                    public boolean hasNext() {
                        return day <= max;
                    }

                    @Override
                    public Predicate<DriveThru> next() {
                        final int curDay = day++;
                        return new Predicate<DriveThru>() {
                            @Override
                            public boolean apply(final DriveThru driveThru) {
                                return driveThru.onDay(curDay);
                            }

                            public String toString() {
                                return format("On day %d", curDay);
                            }
                        };
                    }
                };
            }
        };
    }

    public static DriveThruPredicates hours(final int hours) {
        return minutes(hours * 60);
    }

    public static DriveThruPredicates minutes(final int minutes) {
        return new DriveThruPredicates() {
            @Override
            public Predicates iterator() {

                return new Predicates() {
                    Time time = Time.MIN;

                    @Override
                    public boolean hasNext() {
                        return Time.MAX.compareTo(time) > 0;
                    }

                    @Override
                    public Predicate<DriveThru> next() {
                        final Time start = time;
                        final Time end = min(time.minutes(minutes), Time.MAX);
                        time = end;
                        return new Predicate<DriveThru>() {
                            @Override
                            public boolean apply(final DriveThru driveThru) {
                                return driveThru.wasBetween(start, end);
                            }

                            public String toString() {
                                return format("Drive Through between %s and %s", start, end);
                            }
                        };
                    }
                };
            }
        };
    }

    abstract static class Predicates implements Iterator<Predicate<DriveThru>> {
        @Override
        public void remove() {
            throw new RuntimeException("Not supported");
        }
    }
}
