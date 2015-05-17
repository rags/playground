package fp;

import java.util.ArrayList;
import java.util.List;

public class Flawed {
    public static void main(String[] args) {
        final ArrayList<Employee> employees = new ArrayList<>();
        generics(employees);
        for (Object o : employees) {
            System.out.println(o);
        }
    }


    private static void generics(List employees) {
        employees.add("foo");
        employees.add(123);
    }
}
