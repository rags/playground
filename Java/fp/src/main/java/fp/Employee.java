package fp;

import java.math.BigDecimal;

public class Employee {
    private String name;
    private int age;
    private double salary;
    private String department;

    public Employee(String name, int age, double salary, String department) {
        this.name = name;
        this.age = age;
        this.salary = salary;
        this.department = department;
    }

    public String getName() {
        return name;
    }

    public int age() {
        return age;
    }

    public double salary() {
        return salary;
    }

    public String department() {
        return department;
    }
}
