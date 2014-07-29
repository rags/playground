package fp.v1;

import fp.Employee;

import java.util.ArrayList;

public class EmployeeList extends ArrayList<Employee> {

    public fp.v2.EmployeeList employeesFromDepartment(String departmentName){
        final fp.v2.EmployeeList employees = new fp.v2.EmployeeList();
        for (Employee employee : employees) {
            if (departmentName.equals(employee.department())){
                employees.add(employee);
            }
        }
        return employees;
    }

    public fp.v2.EmployeeList employeesSalaryGreaterThan5000(String departmentName){
        final fp.v2.EmployeeList employees = new fp.v2.EmployeeList();
        for (Employee employee : employees) {
            if (employee.salary()>5000){
                employees.add(employee);
            }
        }
        return employees;
    }

    public fp.v2.EmployeeList employeesAgeLessThan30(String departmentName){
        final fp.v2.EmployeeList employees = new fp.v2.EmployeeList();
        for (Employee employee : employees) {
            if (employee.age()<30){
                employees.add(employee);
            }
        }
        return employees;
    }
    public fp.v2.EmployeeList employeesAgeGreaterThan40AndSalaryGreaterThan10000(String departmentName){
        final fp.v2.EmployeeList employees = new fp.v2.EmployeeList();
        for (Employee employee : employees) {
            if (employee.age()>40 && employee.salary()>10000){
                employees.add(employee);
            }
        }
        return employees;
    }
}
