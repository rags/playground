package fp.v2;

import fp.Employee;

import java.util.ArrayList;


interface Predicate {
    boolean satisfies(Employee employee);
}

public class EmployeeList extends ArrayList<Employee> {
   public EmployeeList filter(Predicate predicate){
       final EmployeeList employees = new EmployeeList();
       for (Employee employee : employees) {
           if (predicate.satisfies(employee)){
               employees.add(employee);
           }
       }
       return employees;
   }
}
