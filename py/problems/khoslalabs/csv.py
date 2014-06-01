'''
CSV Parser

Develop a program to demonstrate your implementation of a CSV parsing framework which can be used to generically parse given CSV file into Java beans and prints out information about parsed objects using toString(). The program should follow OOAD open-closed principle to avoid/minimize modification of code when new types are added in future.

You should accept input from STDIN and print the output to STDOUT.

Assume following input format and study sample inputs given below:

Data-type 
Header-Row
Data-Row-1
Data-Row-2
....
Data-Row-N

The first line indicates the entity type, 2nd line is comma separate list of column names, 3rd line onwards is the comma separated data values.

Test Case 1 Input

Type:Employee
name,age,salary
Ashok,36,20000
Kishor,30,15000
Bharath,25,30000

Expected Output

Name : Ashok;Age : 36
Name : Kishor;Age : 30
Name : Bharath;Age : 25

Test Case 2 Input

Type:Department
code,name
acc,accounts
prl,payroll

Expected Output

Code : acc;Name : accounts
Code : prl;Name : payroll

Your solution should parse the input into Java Beans (POJOs). For example, in test case 1, you will be make use of following Java bean (if you chose Java as programming language, and equivalent if you were using other language).

class Employee {

    private String name;
    private int age;
    private int salary;

    public Employee() {
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public int getSalary() {
        return this.salary;
    }

    public String toString() {
        return "Name : " + this.name + ";" + "Age : " + this.age;
    }
}

You can create a similar bean for Department as required for test case 2.

NOTE: The tool will test both the above two test inputs and also a third test input which is combination (both test case inputs present in same file, one after the other) of two inputs. The expectation is that program should be able to process combination of two inputs and hence, prove it is generic.

In Java, you can start with below code. This example is given here as many Java programmers have faced issues in using multiple Java classes in the solution window.

/* IMPORTANT: class must not be public. */

/*
 * uncomment this if you want to read input.
import java.io.BufferedReader;
import java.io.InputStreamReader;
*/

class TestClass {
    public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */

        System.out.println(new Employee());
    }
}

class Employee {

    private String name;
    private int age;
    private int salary;

    public Employee() {
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return this.age;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public int getSalary() {
        return this.salary;
    }

    public String toString() {
        return "Name : " + this.name + ";" + "Age : " + this.age;
    }
}

class Department {

    private String code;
    private String name;

    public Department() {
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getCode() {
        return this.code;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public String toString() {
        return "Code : " + this.code + ";" + "Name : " + this.name;
    }
}
'''
import sys
if sys.version.startswith("3."):
    raw_input = input

class CsvRecord:
    def __str__(self):
        return ";".join(field.title() + ' : ' + str(value) for field, value in self.__dict__.items())
        
class Employee:
    def __str__(self):
        return "Name : " + self.name + ";Age : " + str(self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = int(value)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = float(value)

class Department:
    def __str__(self):
        return "Code : " + self.code + ";Name : " + self.name

'''
1. use the class name to get the correspondind class
   a. use globals if module information isnt available
   b. load the module and get the class from the module
2. create an anonymous object (of type CsvRecord) if type isnt defined 
'''        
class Class:
    def __init__(self, full_qualified_name, fields):
        if '.' in full_qualified_name:
            index = full_qualified_name.rindex('.')
            try:
                self.clazz = getattr(__import__(full_qualified_name[:index]), full_qualified_name[index + 1:])
            except (ImportError, AttributeError):
                self.clazz = CsvRecord
        elif full_qualified_name in globals():
            self.clazz = globals()[full_qualified_name]
        else:
            self.clazz = CsvRecord
        self.fields = fields

    def new_instance(self, values):
        obj = self.clazz()
        for i in range(len(self.fields)):
            print( self.fields[i], values[i])
            setattr(obj, self.fields[i], values[i])
        return obj

def main():
    clazz = None
    objects = []
    while True:
        try:
            line = raw_input().strip()
            if line.startswith("Type:"):
                clazz = Class(line[len("Type:"):], raw_input().strip().split(","))
                continue
            objects.append(clazz.new_instance(line.split(",")))
        except EOFError:
            break
    for obj in objects:
        print(obj)
    
    
if __name__ == '__main__':
    main()

############################## Tests ##############################

def should_parse_csv_unknown_class():
    clazz = Class("foo.bar.DoesntExist", ["blah1", "blah2"])
    obj = clazz.new_instance([1, "foo"])
    assert 1 == obj.blah1
    assert "foo" == obj.blah2
    assert "Blah1 : 1"  in str(obj)
    assert "Blah2 : foo" in str(obj)

def should_parse_csv_fully_qualified():
    clazz = Class("csv.Employee", ["name", "age", "salary"])
    obj = clazz.new_instance(["blahName", "23", "10000"])
    assert obj.salary == 10000.0
    assert obj.age == 23
    assert "Name : blahName;Age : 23" == str(obj)

def should_parse_dept():
    clazz = Class("Department", ["code", "name"])
    obj = clazz.new_instance(["acc", "accounts"])
    assert "Code : acc;Name : accounts" == str(obj)
