using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Text;

namespace LINQDemo
{
    struct Employee
    {
        int _id;
        string _name;
        int _age;
        int _sal;
        
       
        public int Id
        {
            get { return _id; }
            set { _id = value; }
        }

        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public int Age
        {
            get { return _age; }
            set { _age = value; }
        }


        public int Salary
        {
            get { return _sal; }
            set { _sal = value; }
        }
    }
    
    class EmployeeCollection : Collection<Employee>
    {
        public static EmployeeCollection Get()
        {
            return new EmployeeCollection() 
            {
                new Employee(){Salary=32000,Id=1,Name="Raghu",Age=25},
                new Employee(){Salary=20000,Id=2,Name="Deve Gowda",Age=50},
                new Employee(){Salary=25000,Id=3,Name="Goobe",Age=34},
                new Employee(){Salary=35000,Id=4,Name="Tom",Age=45},
                new Employee(){Salary=27000,Id=5,Name="Dick",Age=36},
                new Employee(){Salary=40000,Id=6,Name="Harry",Age=59}
            };
            
        }
        
        public static EmployeeCollection GetLongMethod()
        {
            EmployeeCollection collection = new EmployeeCollection();
            
            Employee employee = new Employee();
            employee.Id = 1;
            employee.Name="Raghu";
            employee.Age=25;
            collection.Add(employee); 
            
            employee = new Employee();
            employee.Id = 2;
            employee.Name="Deve Gowda";
            employee.Age=50;
            collection.Add(employee); 
            
            employee = new Employee();
            employee.Id = 3;
            employee.Name="Goobe";
            employee.Age=34;
            collection.Add(employee); 
            
            employee = new Employee();
            employee.Id = 4;
            employee.Name="Tom";
            employee.Age=45;
            collection.Add(employee); 
            
            employee = new Employee();
            employee.Id = 5;
            employee.Name="Dick";
            employee.Age=36;
            collection.Add(employee); 
            
            employee = new Employee();
            employee.Id = 6;
            employee.Name="Harry";
            employee.Age=59;
            collection.Add(employee); 
            
            return collection;            
        }
    }
}
