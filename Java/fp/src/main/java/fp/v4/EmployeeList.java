package fp.v4;

import com.google.common.base.Predicate;
import fp.Employee;

import java.util.ArrayList;

import static com.google.common.collect.Iterables.filter;


public class EmployeeList extends ArrayList<Employee> {

    public static void main(String[] args) {
        final Iterable<Employee> filtered = filter(new EmployeeList(), new Predicate<Employee>() {
            @Override
            public boolean apply(Employee employee) {
                return employee.age() > 30;
            }
        });
    }

}
