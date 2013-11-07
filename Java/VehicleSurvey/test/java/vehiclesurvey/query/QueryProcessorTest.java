package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.collect.Range;
import org.hamcrest.Matchers;
import org.junit.Before;
import org.junit.Test;
import vehiclesurvey.ScopedPredicate;
import vehiclesurvey.query.func.Reducer;

import java.util.*;

import static com.google.common.collect.Iterables.*;
import static com.google.common.collect.Range.closedOpen;
import static java.lang.String.format;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.query.QueryProcessorTest.Predicates.asList;
import static vehiclesurvey.query.func.Func.avg;
import static vehiclesurvey.query.func.Func.max;
import static vehiclesurvey.query.func.Func.min;


public class QueryProcessorTest {
    private QueryProcessor<Employee> employees;

    class Employee {
        public final int age;
        public final double salary;
        public final int noOfSubordinates;

        Employee(int age, double salary) {
            this(age, salary, 0);
        }

        Employee(int age, double salary, int noOfSubordinates) {
            this.age = age;
            this.salary = salary;
            this.noOfSubordinates = noOfSubordinates;
        }
    }

    static class Predicates extends ArrayList<ScopedPredicate<Employee>> implements vehiclesurvey.query.Predicates<Employee> {
        public Predicates(List<ScopedPredicate<Employee>> predicates) {
            super(predicates);
        }

        public static Predicates asList(ScopedPredicate<Employee>... predicates) {
            return new Predicates(Arrays.asList(predicates));
        }
    }

    @Before
    public void setUp() throws Exception {
        employees = new QueryProcessor<Employee>(Arrays.asList(
                new Employee(23, 3000), new Employee(30, 6000, 5), new Employee(50, 10000, 30),
                new Employee(21, 3000, 2), new Employee(35, 5000, 10), new Employee(53, 9000, 10),
                new Employee(25, 5000, 5), new Employee(33, 7500, 3), new Employee(45, 7000)), "employees");
    }

    @Test
    public void shouldSumAllSalaries(){
        assertThat((Double)employees.reduce(new Reducer<Employee, Double>() {

            @Override
            public Double apply(Employee item, Double accumulator) {
                return accumulator+item.salary;
            }
        }, 0d).scalarResult(),is(55500d));
    }

    @Test
    public void shouldGroup() {
        QueryProcessor queryProcessor = employees.groupBy(asList(ageGroup(closedOpen(10, 25))));

        QueryProcessor<Employee> employeeQueryProcessor = (QueryProcessor<Employee>) getFirst(queryProcessor, null);
        assertThat(employeeQueryProcessor.<Range<Integer>>scope(), is(closedOpen(10, 25)));
        Iterable<Employee> expected = filter(employees, ageGroup(closedOpen(10, 25)));
        assertThat(employeeQueryProcessor, Matchers.<Employee>iterableWithSize(size(expected)));
        for (Employee employee : expected) {
            assertThat(employeeQueryProcessor, hasItem(employee));
        }

        QueryProcessor<Integer> count = (QueryProcessor<Integer>) getFirst(queryProcessor.count(), null);
        assertThat(count.<Range<Integer>>scope(), is(closedOpen(10,25)));

        assertThat(getFirst(count, 0), is(2));
    }

    @Test
    public void shouldFilter() {
        QueryProcessor<Employee> employeeQueryProcessor = employees.where(ageGroup(closedOpen(30,50)));

        Iterable<Employee> expected = filter(employees, ageGroup(closedOpen(30, 50)));
        assertThat(employeeQueryProcessor, Matchers.<Employee>iterableWithSize(size(expected)));
        for (Employee employee : expected) {
            assertThat(employeeQueryProcessor, hasItem(employee));
        }
    }

    private ScopedPredicate<Employee> ageGroup(final Range<Integer> range) {
        return new ScopedPredicate<Employee>() {
            @Override
            public boolean apply(Employee e) {
                return range.contains(e.age);
            }

            public Object scope() {
                return range;
            }
        };
    }

    @Test
    public void shouldCalculateAvgSalaryDistributionByAgeGroup() {
        QueryProcessor queryProcessor = avgSalaryByAgeGroup();
        assertThat(size(queryProcessor), is(7));
        Iterator iterator = queryProcessor.iterator();
        for (Double expected : new Double[]{3000d, 5000d, 6750d, 5000d, 0d, 7000d, 9500d}) {
            Double first = (Double) getFirst((QueryProcessor) iterator.next(), 0d);
            assertThat(first, is(expected));
        }
    }

    @Test
    public void shouldGiveMaxAvgSalaryAcrossAgeGroups(){
        assertThat((Double)avgSalaryByAgeGroup().aggregateAggregates(new Function<Iterable<QueryProcessor>, Double>() {

            @Override
            public Double apply(Iterable<QueryProcessor> processors) {

                QueryProcessor<Double> max = max(new Function<QueryProcessor<Double>, Double>() {
                    @Override
                    public Double apply(QueryProcessor<Double> queryProcessor) {
                        return queryProcessor.scalarResult();
                    }
                }, (Iterable) processors);
                return max.scalarResult();
            }
        }).scalarResult(),is(9500d));
    }

    @Test
    public void shouldGiveMaxAvgSalaryAgeGroup(){
        assertThat((Range<Integer>)avgSalaryByAgeGroup().aggregateAggregates(new Function<Iterable<QueryProcessor>, Object>() {

            @Override
            public Object apply(Iterable<QueryProcessor> processors) {

                return min(new Function<QueryProcessor<Double>, Double>() {
                    @Override
                    public Double apply(QueryProcessor<Double> queryProcessor) {
                        return queryProcessor.scalarResult();
                    }
                }, (Iterable) processors).scope();
            }
        }).scalarResult(),is(closedOpen(40,45)));
    }

    private QueryProcessor avgSalaryByAgeGroup() {
        return employees.groupBy(asList(
                ageGroup(closedOpen(20, 25)), ageGroup(closedOpen(25, 30)),
                ageGroup(closedOpen(30, 35)), ageGroup(closedOpen(35, 40)),
                ageGroup(closedOpen(40, 45)), ageGroup(closedOpen(45, 50)), ageGroup(closedOpen(50, 55)))).
                aggregate(new Function<Collection<Employee>, Double>() {
                    @Override
                    public Double apply(Collection<Employee> employees) {
                        return avg(new Function<Employee, Double>() {
                            @Override
                            public Double apply(Employee e) {
                                return e.salary;
                            }
                        }, employees);
                    }
                });
    }

    @Test
    public void shouldGroupByAgeThenSubordinateCountAndGetMaxSalary() {
        QueryProcessor queryProcessor = employees.groupBy(asList(
                ageGroup(closedOpen(20, 30)),
                ageGroup(closedOpen(30, 40)),
                ageGroup(closedOpen(40, 50)))).
                groupBy(asList(subordinates(0, 10), subordinates(10, 20))).reduce(
                new Reducer<Employee, Double>() {
                    @Override
                    public Double apply(Employee e, Double max) {
                        return Math.max(e.salary, max);
                    }
                }, 0d);
        double[][] expected = {{5000, 0}, {7500, 5000}, {7000, 0}};
        assertThat(size(queryProcessor),is(expected.length));
        Iterator ageGroupsIt = queryProcessor.iterator();
        for(double[] ageGroupExpected : expected){
            QueryProcessor ageQueryProcessor = (QueryProcessor)ageGroupsIt.next();
            assertThat(size(ageQueryProcessor),is(ageGroupExpected.length));
            Iterator subordinateGrpIt = ageQueryProcessor.iterator();
            for(double maxSal: ageGroupExpected){
                double actual = ((QueryProcessor<Double>) subordinateGrpIt.next()).scalarResult();
                assertThat(maxSal,is(actual));
            }
        }

    }

    private ScopedPredicate<Employee> subordinates(final int from, final int to) {
        return new ScopedPredicate<Employee>() {
            @Override
            public boolean apply(Employee e) {
                return e.noOfSubordinates >= from && e.noOfSubordinates < to;
            }

            public String scope(){
                return format("%d <= [subordinates] < %d", from,to);
            }
        };
    }

}
