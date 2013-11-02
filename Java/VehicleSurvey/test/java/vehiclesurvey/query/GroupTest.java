package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import org.hamcrest.Matchers;
import org.junit.Before;
import org.junit.Test;
import vehiclesurvey.query.func.Reducer;

import java.util.*;

import static com.google.common.collect.Iterables.*;
import static java.lang.String.format;
import static java.util.Arrays.asList;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.query.GroupTest.Predicates.asList;
import static vehiclesurvey.query.func.Func.avg;


public class GroupTest {
    private Group<Employee> employees;

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

    static class Predicates extends ArrayList<Predicate<Employee>> implements vehiclesurvey.query.Predicates<Employee> {
        public Predicates(List<Predicate<Employee>> predicates) {
            super(predicates);
        }

        public static Predicates asList(Predicate<Employee>... predicates) {
            return new Predicates(Arrays.asList(predicates));
        }
    }

    @Before
    public void setUp() throws Exception {
        List<Employee> employees1 = asList(
                new Employee(23, 3000), new Employee(30, 6000, 5), new Employee(50, 10000, 30),
                new Employee(21, 3000, 2), new Employee(35, 5000, 10), new Employee(53, 9000, 10),
                new Employee(25, 5000, 5), new Employee(33, 7500, 3), new Employee(45, 7000));
        employees = new Group<Employee>(employees1, "employees");
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
        Group group = employees.group(asList(ageGroup(10, 25)));

        Group<Employee> employeeGroup = (Group<Employee>) getFirst(group, null);
        assertThat(employeeGroup.tag(), is("10 <= age < 25"));
        Iterable<Employee> expected = filter(employees, ageGroup(10, 25));
        assertThat(employeeGroup, Matchers.<Employee>iterableWithSize(size(expected)));
        for (Employee employee : expected) {
            assertThat(employeeGroup, hasItem(employee));
        }

        Group<Integer> count = (Group<Integer>) getFirst(group.count(), null);
        assertThat(count.tag(), is("10 <= age < 25"));

        assertThat(getFirst(count, 0), is(2));
    }

    private Predicate<Employee> ageGroup(final int start, final int end) {
        return new Predicate<Employee>() {
            @Override
            public boolean apply(Employee e) {
                return start <= e.age && e.age < end;
            }

            public String toString() {
                return format("%d <= age < %d", start, end);
            }
        };
    }

    @Test
    public void shouldCalculateAvgSalaryDistributionByAgeGroup() {
        Group group = employees.group(asList(
                ageGroup(20, 25), ageGroup(25, 30),
                ageGroup(30, 35), ageGroup(35, 40),
                ageGroup(40, 45), ageGroup(45, 50), ageGroup(50, 55))).
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
        assertThat(size(group), is(7));
        Iterator iterator = group.iterator();
        for (Double expected : new Double[]{3000d, 5000d, 6750d, 5000d, 0d, 7000d, 9500d}) {
            Double first = (Double) getFirst((Group) iterator.next(), 0d);
            assertThat(first, is(expected));
        }
    }

    @Test
    public void shouldGroupByAgeThenSubordinateCountAndGetMaxSalary() {
        Group group = employees.group(asList(
                ageGroup(20, 30),
                ageGroup(30, 40),
                ageGroup(40, 50))).
                group(asList(subordinates(0, 10), subordinates(10, 20))).reduce(
                new Reducer<Employee, Double>() {
                    @Override
                    public Double apply(Employee e, Double max) {
                        return Math.max(e.salary, max);
                    }
                }, 0d);
        double[][] expected = {{5000, 0}, {7500, 5000}, {7000, 0}};
        assertThat(size(group),is(expected.length));
        Iterator ageGroupsIt = group.iterator();
        for(double[] ageGroupExpected : expected){
            Group ageGroup = (Group)ageGroupsIt.next();
            assertThat(size(ageGroup),is(ageGroupExpected.length));
            Iterator subordinateGrpIt = ageGroup.iterator();
            for(double maxSal: ageGroupExpected){
                double actual = ((Group<Double>) subordinateGrpIt.next()).scalarResult();
                assertThat(maxSal,is(actual));
            }
        }

    }

    private Predicate<Employee> subordinates(final int from, final int to) {
        return new Predicate<Employee>() {
            @Override
            public boolean apply(Employee e) {
                return e.noOfSubordinates >= from && e.noOfSubordinates < to;
            }

            public String toString(){
                return format("%d <= [subordinates] < %d", from,to);
            }
        };
    }


}
