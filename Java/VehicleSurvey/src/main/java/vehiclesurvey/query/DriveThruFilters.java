package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.Range;
import vehiclesurvey.Direction;
import vehiclesurvey.DriveThru;
import vehiclesurvey.DriveThruList;
import vehiclesurvey.ScopedPredicate;
import vehiclesurvey.query.func.Func;
import vehiclesurvey.time.Time;

import java.util.*;

import static com.google.common.collect.Iterables.transform;
import static com.google.common.collect.Range.closedOpen;
import static vehiclesurvey.query.PredicateList.asList;
import static vehiclesurvey.query.func.Func.max;
import static vehiclesurvey.time.Time.time;


class PredicateList extends ArrayList<ScopedPredicate<DriveThru>> implements DriveThruPredicates { //keep compiler happy

    public PredicateList(List<ScopedPredicate<DriveThru>> predicates) {
        super(predicates);
    }

    public static PredicateList asList(ScopedPredicate<DriveThru>... predicates) {
        return new PredicateList(Arrays.asList(predicates));
    }
}

//Query is a generic class. This one has any filters/predicates/grouping specific to drivethrus
public class DriveThruFilters {

    public static final Range<Time> MORNING = closedOpen(time().hours(6), time().hours(10));
    public static final Range<Time> EVENING = closedOpen(time().hours(16), time().hours(20));

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

    public static DriveThruPredicates direction() {
        return asList(direction(Direction.North), direction(Direction.South));
    }

    private static ScopedPredicate<DriveThru> direction(final Direction direction) {
        return new ScopedPredicate<DriveThru>() {
            @Override
            public boolean apply(DriveThru driveThru) {
                return driveThru.heading() == direction;
            }

            public Object scope() {
                return direction;
            }
        };
    }

    public static DriveThruPredicates speeds(DriveThruList driveThrus) {
        return speeds(driveThrus, 1);
    }

    public static DriveThruPredicates speeds(final DriveThruList driveThrus, final int slotSize) {
        final double min = Math.floor(Func.min(speed(), driveThrus).speed());
        Double maxUnrounded = max(speed(), driveThrus).speed();
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
                    public ScopedPredicate<DriveThru> next() {
                        final Range<Double> speedRange = closedOpen(value, value = slotSize + value);
                        return new ScopedPredicate<DriveThru>() {
                            @Override
                            public boolean apply(final DriveThru driveThru) {
                                return speedRange.contains(driveThru.speed());
                            }

                            public Range<Double> scope() {
                                return speedRange;
                            }
                        };
                    }
                };
            }
        };
    }

    public static Function<Collection<DriveThru>, Double> avgDistanceBetweenCars(){
        return new Function<Collection<DriveThru>,Double>(){
            @Override
            public Double apply(Collection<DriveThru> driveThrus) {
                return new DriveThruList(driveThrus).avgDistanceBetweenCars();
            }
        };
    }

    public static Function<Integer, Double> percentMapper(final int total) {
        return new Function<Integer, Double>() {
            @Override
            public Double apply(Integer input) {
                return ((input * 1d) / total) * 100;
            }
        };
    }

    public static ScopedPredicate<DriveThru> dayFilter(final int day) {
        return new ScopedPredicate<DriveThru>() {
            @Override
            public Object scope() {
                return day;
            }

            @Override
            public boolean apply(DriveThru driveThru) {
                return driveThru.onDay(day);
            }
        };
    }

    public static ScopedPredicate<DriveThru> directionFilter(final Direction direction) {
        return new ScopedPredicate<DriveThru>() {
            @Override
            public Object scope() {
                return direction;
            }

            @Override
            public boolean apply(DriveThru driveThru) {
                return driveThru.heading()==direction;
            }
        };
    }

    public static DriveThruPredicates days(DriveThruList driveThrus) {
        return days(driveThrus.lastDay());
    }

    public static DriveThruPredicates days(final int days) {
        return new DriveThruPredicates() {
            @Override
            public Predicates iterator() {

                return new Predicates() {
                    int day = 1;

                    @Override
                    public boolean hasNext() {
                        return day <= days;
                    }

                    @Override
                    public ScopedPredicate<DriveThru> next() {
                        final int curDay = day++;
                        return new ScopedPredicate<DriveThru>() {
                            @Override
                            public boolean apply(final DriveThru driveThru) {
                                return driveThru.onDay(curDay);
                            }

                            public Integer scope() {
                                return curDay;
                            }
                        };
                    }
                };
            }
        };
    }

    public static DriveThruPredicates morningEvening() {
        return timeRanges(Arrays.asList(MORNING, EVENING));
    }

    public static DriveThruPredicates hours(final int hours) {
        return minutes(hours * 60);
    }

    public static DriveThruPredicates timeRanges(final Iterable<Range<Time>> timeRanges) {
        final Iterable<ScopedPredicate<DriveThru>> scopedPredicates = transform(timeRanges, new Function<Range<Time>, ScopedPredicate<DriveThru>>() {
            @Override
            public ScopedPredicate<DriveThru> apply(Range<Time> timeRange) {
                return timeRangePredicate(timeRange);
            }
        });
        return new DriveThruPredicates() {
            @Override
            public Iterator<ScopedPredicate<DriveThru>> iterator() {
                return scopedPredicates.iterator();
            }
        };
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
                    public ScopedPredicate<DriveThru> next() {
                        final Range<Time> timeRange = closedOpen(time, time = min(time.minutes(minutes), Time.MAX));
                        return timeRangePredicate(timeRange);
                    }
                };
            }
        };
    }

    private static ScopedPredicate<DriveThru> timeRangePredicate(final Range<Time> timeRange) {
        return new ScopedPredicate<DriveThru>() {
            @Override
            public boolean apply(final DriveThru driveThru) {
                return driveThru.wasBetween(timeRange);
            }

            public Range<Time> scope() {
                return timeRange;
            }
        };
    }

    public static Function<Iterable<QueryProcessor<Comparable>>, Iterable<QueryProcessor<Comparable>>> aggregateAllMax() {
        return new Function<Iterable<QueryProcessor<Comparable>>, Iterable<QueryProcessor<Comparable>>>() {
            @Override
            public Iterable<QueryProcessor<Comparable>> apply(Iterable<QueryProcessor<Comparable>> processors) {
                return Func.allMax(new Function<QueryProcessor<Comparable>, Comparable>() {
                    @Override
                    public Comparable apply(QueryProcessor<Comparable> input) {
                        return input.scalarResult();
                    }
                }, processors);
            }
        };
    }


    abstract static class Predicates implements Iterator<ScopedPredicate<DriveThru>> {
        @Override
        public void remove() {
            throw new RuntimeException("Not supported");
        }
    }
}
