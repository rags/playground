package fp;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        final ArrayList<Employee> employees = new ArrayList<>();
        final ArrayList employees1 = employees;
        employees1.add("foo");
        employees1.add(123);
        for (Object o : employees) {
            System.out.println(o);
        }
    }
}
