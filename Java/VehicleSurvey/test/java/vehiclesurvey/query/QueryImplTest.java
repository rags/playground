package vehiclesurvey.query;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Range;
import org.junit.Before;
import org.junit.Test;
import vehiclesurvey.Direction;
import vehiclesurvey.DriveThru;
import vehiclesurvey.DriveThruList;
import vehiclesurvey.time.Time;

import java.util.*;

import static com.google.common.base.Predicates.and;
import static com.google.common.collect.Iterables.concat;
import static java.lang.String.format;
import static java.util.Arrays.asList;
import static org.hamcrest.Matchers.closeTo;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.Direction.North;
import static vehiclesurvey.Direction.South;
import static vehiclesurvey.DriveThruFixture.aDriveThru;
import static vehiclesurvey.DriveThrusFixture.driveThrus;
import static vehiclesurvey.query.DriveThruFilters.*;
import static vehiclesurvey.query.QueryImpl.aggregateAvg;
import static vehiclesurvey.query.QueryImpl.select;
import static vehiclesurvey.time.Time.time;

public class QueryImplTest {

    private DriveThruList driveThrus;

    @Before
    public void setUp() throws Exception {
        driveThrus = driveThrus(
                drive(1, t().minutes(30), 65, North), drive(1, t().hours(2), 55, North), drive(1, t().minutes(150), 66, South),
                drive(1, t().minutes(160), 62, South), drive(1, t().minutes(190), 62.5, South), drive(1, t().minutes(200), 50, North),
                drive(1, t().hours(5), 53, North), drive(1, t().hours(18), 59, North), drive(1, t().hours(18).minutes(10), 72, South),
                drive(1, t().hours(18).minutes(30), 69, South), drive(1, t().hours(18).minutes(50), 57, South), drive(1, t().hours(22), 64, North),

                drive(2, t().minutes(50), 58, South), drive(2, t().hours(2), 49, North), drive(2, t().minutes(150), 68, South),
                drive(2, t().hours(4), 55, North), drive(2, t().minutes(250), 59, South), drive(2, t().minutes(280), 63.7, North),
                drive(2, t().hours(6), 59, South), drive(2, t().hours(17), 62, South), drive(2, t().hours(17).minutes(10), 57.6, North),
                drive(2, t().hours(17).minutes(30), 49, North), drive(2, t().hours(18).minutes(50), 75, North), drive(2, t().hours(23), 62, North),

                drive(3, t().minutes(100), 55, South), drive(3, t().hours(2), 58, North), drive(3, t().minutes(150), 68, North),
                drive(3, t().hours(9), 59, South), drive(3, t().hours(9).minutes(2), 61, South), drive(3, t().hours(9).minutes(28), 63.7, South),
                drive(3, t().hours(9).minutes(45), 64, North), drive(3, t().hours(18), 60, North), drive(3, t().hours(18).minutes(1), 57.6, North),
                drive(3, t().hours(18).minutes(30), 65, South), drive(3, t().hours(19).minutes(1), 65, South), drive(3, t().hours(21), 62, South)
        );
    }

    @Test
    public void shouldCountMorningEveningTraffic() {
        QueryProcessor result = select(DriveThru.class)
                .where(and(directionFilter(North), dayFilter(3)))
                .groupBy(morningEvening()).count().execute(driveThrus);

        assertThat((Integer)result.resultFor(MORNING).scalarResult(), is(1));
        assertThat((Integer)result.resultFor(EVENING).scalarResult(), is(2));
    }

    @Test
    public void shouldGiveTrafficOnAGivenDayAndGivenDirection() {
        QueryProcessor result = select(DriveThru.class)
                .where(and(dayFilter(2), directionFilter(North)))
                .groupBy(hours(6)).count().execute(driveThrus);

        Map<Range<Time>, Integer> expected = map(asList(
                range(t().hours(0), t().hours(6)),
                range(t().hours(6), t().hours(12)),
                range(t().hours(12), t().hours(18)),
                range(t().hours(18), t().hours(24))), asList(3, 0, 2, 2));

        for (Range<Time> timeRange : expected.keySet()) {
            assertThat((Integer) result.resultFor(timeRange).scalarResult(), is(expected.get(timeRange)));
        }

    }

    @Test
    public void shouldCalculateTotalVehiclesPer3HourInEachDirection() {
        Query count = select(DriveThru.class)
                .groupBy(direction())
                .groupBy(days(driveThrus))
                .groupBy(hours(3)).count();

        QueryProcessor result = count.execute(driveThrus);

        List<Range<Time>> ranges = threeHourSlots();

        ImmutableMap<Direction, ImmutableMap<Integer, Map<Range<Time>, Integer>>> expected =
                ImmutableMap.of(
                        North, ImmutableMap.of(
                        1, map(ranges, asList(2, 2, 0, 0, 0, 0, 1, 1)),
                        2, map(ranges, asList(1, 2, 0, 0, 0, 2, 1, 1)),
                        3, map(ranges, asList(2, 0, 0, 1, 0, 0, 2, 0))),

                        South, ImmutableMap.of(
                        1, map(ranges, asList(2, 1, 0, 0, 0, 0, 3, 0)),
                        2, map(ranges, asList(2, 1, 1, 0, 0, 1, 0, 0)),
                        3, map(ranges, asList(1, 0, 0, 3, 0, 0, 2, 1))));

        for (Direction direction : expected.keySet()) {
            GroupOfQueryProcessors directionData = (GroupOfQueryProcessors) result.resultFor(direction);
            ImmutableMap<Integer, Map<Range<Time>, Integer>> daysExpected = expected.get(direction);
            for (int day : daysExpected.keySet()) {
                Map<Range<Time>, Integer> dayExpected = daysExpected.get(day);
                for (Range<Time> threeHrSlot : ranges) {
                    Integer actualCnt = ((QueryProcessor<Integer>) directionData.resultFor(day).resultFor(threeHrSlot)).scalarResult();
                    Integer expectedCnt = dayExpected.get(threeHrSlot);
                    assertThat(format("For direction %s on day %d @ %s:\nExpected %d but was %d ", direction, day, threeHrSlot, expectedCnt, actualCnt), actualCnt, is(expectedCnt));
                }
            }
        }
    }

    @Test
    public void shouldTotalsAveragedAcrossDaysInEachDirectionFor3HoursSlots() {
        QueryProcessor result = avgCountAcrossDaysFor3hrSlots();

        List<Range<Time>> ranges = threeHourSlots();
        ImmutableMap<Direction, Map<Range<Time>, Double>> expected = ImmutableMap.of(
                North, map(ranges, asList(5d / 3, 4d / 3, 0d, 1d / 3, 0d, 2d / 3, 4d / 3, 2d / 3)),
                South, map(ranges, asList(5d / 3, 2d / 3, 1d / 3, 1d, 0d, 1d / 3, 5d / 3, 1d / 3)));

        for (Direction direction : expected.keySet()) {
            GroupOfQueryProcessors directionData = (GroupOfQueryProcessors) result.resultFor(direction);
            for (Range<Time> range : ranges) {
                assertThat(range.toString(), (Double) directionData.resultFor(range).scalarResult(), is(expected.get(direction).get(range)));
            }
        }
    }

    @Test
    public void shouldListPeakVolumeTimes() {
        QueryProcessor result = avgCountAcrossDaysFor3hrSlots().filterAggregates(aggregateAllMax());
        ImmutableMap<Direction, ImmutableMap<Range<Time>, Double>> expected = ImmutableMap.of(
                North, ImmutableMap.of(range(t().hours(0), t().hours(3)), 5d / 3),

                South, ImmutableMap.of(
                range(t().hours(0), t().hours(3)), 5d / 3,
                range(t().hours(18), t().hours(21)), 5d / 3));

        for (Direction direction : expected.keySet()) {
            QueryProcessor queryProcessor = result.resultFor(direction);
            ImmutableMap<Range<Time>, Double> expectedPeakTimes = expected.get(direction);
            for (Range<Time> timeRange : expectedPeakTimes.keySet()) {
                assertThat((Double) queryProcessor.resultFor(timeRange).scalarResult(), is(expectedPeakTimes.get(timeRange)));
            }
        }
    }

    @Test
    public void shouldSpeedDistributionCount() {
        QueryProcessor queryProcessor = select(DriveThru.class).groupBy(speeds(driveThrus, 3)).count().execute(driveThrus);
        Map<Range<Double>, Integer> expected = map(speedDistribution3KMSlot(), asList(3, 1, 6, 7, 8, 6, 3, 1, 1));

        for (Range speedRange : expected.keySet()) {
            assertThat((Integer) queryProcessor.resultFor(speedRange).scalarResult(), is(expected.get(speedRange)));
        }
    }

    @Test
    public void shouldProvideSpeedDistributionPercentage() {
        int total = driveThrus.size();
        QueryProcessor result = select(DriveThru.class).groupBy(speeds(driveThrus, 3)).count().execute(driveThrus).map(percentMapper(total));
        Map<Range<Double>, Double> expected = map(
                speedDistribution3KMSlot(),
                asList(3 * 100d / total, 1 * 100d / total, 6 * 100d / total,
                        7 * 100d / total, 8 * 100d / total, 6 * 100d / total,
                        3 * 100d / total, 1 * 100d / total, 1 * 100d / total));
        double totalPercent = 0;
        for (Range speedRange : expected.keySet()) {
            Double actual = (Double) result.resultFor(speedRange).scalarResult();
            totalPercent += actual;
            assertThat(actual, is(closeTo(expected.get(speedRange), .0001)));
        }
        assertThat(totalPercent, is(closeTo(100d, .0001)));
    }

    @Test
    public void shouldCalculateDistanceBetweenCarsForEachDay() {
        QueryProcessor result = select(DriveThru.class)
                .where(directionFilter(North))
                .groupBy(days(driveThrus)).aggregate(avgDistanceBetweenCars()).execute(driveThrus);
        double[] expected = {0, 258, 210, 240.25};
        for (int day = 1; day < expected.length; day++) {
            assertThat((Double) result.resultFor(day).scalarResult(), is(expected[day]));
        }
    }

    @Test
    public void shouldCalculateAvgDistanceInBothDirectionBetweenCars_3HourSlots_AvgAcrossDays() {
        QueryProcessor result = select(DriveThru.class)
                .groupBy(direction())
                .groupBy(hours(3))
                .groupBy(days(driveThrus))
                .aggregate(avgDistanceBetweenCars()).execute(driveThrus).aggregateAggregates(aggregateAvg());
        ImmutableMap<Direction, Map<Range<Time>, Double>> expected = (ImmutableMap<Direction, Map<Range<Time>, Double>>) ImmutableMap.of(
                North, map(threeHourSlots(), asList(40d, 46.66, 0d, 0d, 0d, 6.66, 0.33, 0d)),
                South, map(threeHourSlots(), asList(36.66, 0d, 0d, 4.66, 0d, 0d, 17d, 0d)));
        for (Direction direction : expected.keySet()) {
            for (Range timeRange : threeHourSlots()) {
                assertThat((Double) result.resultFor(direction).resultFor(timeRange).scalarResult(),
                        is(closeTo(expected.get(direction).get(timeRange), .01)));
            }
        }
    }

    @Test
    public void shouldAvgDistanceBetweenVehiclesDuringPeakVolumeHours() {
        final QueryProcessor peakTraffic = avgCountAcrossDaysFor3hrSlots().filterAggregates(aggregateAllMax());
        HashSet<Range<Time>> peakTimes = new HashSet<Range<Time>>() {{
            for (QueryProcessor queryProcessor : concat((Collection<QueryProcessor>) peakTraffic.resultFor(North).results(), (Collection<QueryProcessor>) peakTraffic.resultFor(South).results())) {
                add((Range<Time>) queryProcessor.scope());
            }
        }};
        QueryProcessor result = select(DriveThru.class)
                .groupBy(direction())
                .groupBy(timeRanges(peakTimes))
                .groupBy(days(driveThrus))
                .aggregate(avgDistanceBetweenCars())
                .execute(driveThrus)
                .aggregateAggregates(aggregateAvg());

        ImmutableMap<Direction, ? extends Map<Range<Time>, Double>> expected = ImmutableMap.of(
                North, map(peakTimes, asList(0.333, 40d)),
                South, map(peakTimes, asList(17d, 36.666)));
        for (Direction direction : expected.keySet()) {
            for (Range<Time> peakTime : peakTimes) {
                assertThat((Double) result.resultFor(direction).resultFor(peakTime).scalarResult(),
                        is(closeTo(expected.get(direction).get(peakTime), .001)));
            }
        }
    }

    private List<Range<Double>> speedDistribution3KMSlot() {
        return asList(
                range(49d, 52d), range(52d, 55d), range(55d, 58d), range(58d, 61d),
                range(61d, 64d), range(64d, 67d), range(67d, 70d), range(70d, 73d), range(73d, 76d));
    }

    private <T extends Comparable> Range<T> range(T item1, T time2) {
        return Range.closedOpen(item1, time2);
    }

    private QueryProcessor avgCountAcrossDaysFor3hrSlots() {
        Query<DriveThru> query = select(DriveThru.class)
                .groupBy(direction())
                .groupBy(hours(3))
                .groupBy(days(driveThrus)).countAvg();
        return query.execute(driveThrus);
    }

    private List<Range<Time>> threeHourSlots() {//8 slots per day - 00-03, 03-06, 06-09, 09-12, 12-15, 15-18, 18-21, 21-24/00
        return asList(
                range(t(), t().hours(3)), range(t().hours(3), t().hours(6)), range(t().hours(6), t().hours(9)),
                range(t().hours(9), t().hours(12)), range(t().hours(12), t().hours(15)), range(t().hours(15), t().hours(18)),
                range(t().hours(18), t().hours(21)), range(t().hours(21), t().hours(24)));
    }

    private DriveThru drive(int day, Time time, double speed, Direction direction) {
        return aDriveThru().onDay(day).atTime(time).driveAt(speed).heading(direction).build();
    }

    private Time t() {//shorthand
        return time();
    }

    public <K, V> Map<K, V> map(final Iterable<K> keys, final Iterable<V> values) {
        return new HashMap<K, V>() {{
            Iterator<V> iterator = values.iterator();
            for (K key : keys) {
                put(key, iterator.next());
            }
        }};
    }
}
