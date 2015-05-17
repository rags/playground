package fp;

import com.google.common.base.Function;
import com.google.common.collect.FluentIterable;
import fp.v4.EmployeeList;

import java.util.ArrayList;
import java.util.Map;
import java.util.stream.Stream;

import static com.google.common.collect.Maps.transformValues;
import static com.google.common.collect.Maps.uniqueIndex;

interface F<T, K> {
    K apply(K k, T t);
}

public class Department {
    private String name;
    private EmployeeList employees;

    public Department(String name) {
        this.name = name;
        this.employees = new EmployeeList();
    }

    public static <T, K> K reduce(Iterable<T> iterable, K init, F<T, K> f) {
        K retVal = init;
        for (T t : iterable) {
            retVal = f.apply(retVal, t);
        }
        return retVal;
    }

    public static void main(String[] args) {
        //map of department name and total salary
        final ArrayList<Department> departments = new ArrayList<>();
        final Map<String, Double> departmentTotalSalMap = transformValues(
                uniqueIndex(departments, new Function<Department, String>() {
                    @Override
                    public String apply(Department department) {
                        return department.name;
                    }
                }),
                new Function<Department, Double>() {
                    @Override
                    public Double apply(Department department) {
                        return reduce(FluentIterable.from(department.employees).transform(new Function<Employee, Double>() {
                            @Override
                            public Double apply(Employee employee) {
                                return employee.salary();
                            }
                        }), 0d, new F<Double,Double>() {
                            @Override
                            public Double apply(Double aDouble, Double aDouble2) {
                                return aDouble+aDouble2;
                            }
                        });
                    }
                });
    }

    public static void main1(String[] args) {
        //map of department name and total salary
        final ArrayList<Department> departments = new ArrayList<>();
        final Stream<Department> filter = departments.stream().filter(department -> department.employees.size() > 10);

        final Map<String, Double> departmentTotalSalMap = transformValues(
                uniqueIndex(departments, (Department department) -> department.name),
                department -> reduce(FluentIterable.from(department.employees)
                        .transform(employee -> employee.salary()), 0d,
                        (aDouble, aDouble2) -> aDouble+aDouble2));
    }
   
}
