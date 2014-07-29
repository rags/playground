package fp.v3;

import fp.Employee;

import java.util.ArrayList;

public class EmployeeList extends ArrayList<Employee> {

    public static void main(String[] args) {
        new EmployeeList().stream().filter(employee -> employee.age()>3000);
    }

}
