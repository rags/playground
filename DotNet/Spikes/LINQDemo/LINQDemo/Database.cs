using System;
using System.Collections.Generic;
using System.Data;
using System.Data.DLinq;
using System.Data.Odbc;
using System.Data.OleDb;
using System.Data.SqlClient;
using System.Text;
using System.Xml;
using System.Xml.XLinq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Data.Common;
using System.Query;
using System.IO;

using System.Diagnostics;

namespace LINQDemo
{
    [TestClass]
    class Database
    {
        

        [Table(Name="Employee")]
        class Employee
        {
            [Column]
            public string Name=null;
            [Column]
            public int Age;
            [Column]
            public int DepartmentId;
            [Column]
            public char Sex;
            [Column(Id=true)]
            public int? EmployeeId=null;


            public override string ToString()
            {
                return Name + " " + Age + " " + Sex;
            }

            /*
            private EntityRef<Department> _department;
[Association(Storage="_department", ThisKey="DepartmentID")]
	        public Department Department 
            {
		        get { return this._department.Entity; }
		        set { this._department.Entity = value; }
	        }*/
        }
        
        [Table(Name="Department")]
        class Department
        {
            [Column(Id=true)]
            public int DepartmentId;
            [Column]
            public string Name=null;
          	
	        
/*
            private EntitySet<Employee> _employees=null;
            [Association(Storage="_employees", OtherKey="DepartmentId")]
	        public EntitySet<Employee> Employees 
	        {
		        get { return this._employees; }
		        set { this._employees.Assign(value); }
	        }
*/
  
        }
        private DataContext _context;
        [TestInitialize]
        public void Init()
        {
            
            _context = new DataContext(@"C:\Spikes\LinqDemo\LinqDemo\Employee.mdf");
            //_context = new DataContext(new SqlConnection( @"Data Source=tcp:.\SQLExpress,1433;Initial Catalog=C:\Spikes\LinqDemo\LinqDemo\Employee.mdf;Integrated Security=SSPI;"));
            _context.AcceptChanges();
        }
        [TestMethod]
        public void Test()
        {
            
            Table<Department> departmentTable = _context.GetTable<Department>();
            var departments = from department in departmentTable select department;
            foreach (var department in departments)
            {
                Console.WriteLine(department.DepartmentId + " " +   department.Name);
            }
            
            Table<Employee> employeeTable = _context.GetTable<Employee>();
            var employees = from employee in employeeTable select employee;
            foreach (var employee in employees)
            {
                Console.WriteLine(employee.EmployeeId + " " +employee.Name + " " + employee.DepartmentId);
            }
            
        }
        
        [TestMethod]
        public void DataSetTest()
        {
            var table = _context.GetTable<Department>().Take(2).ToDataTable();
            foreach (DataRow row in table.Rows)
            {
                Console.WriteLine(row[0] + " " + row[1]);
            }
        }
        
        
        [TestMethod]
        public void TestJoin()
        {
            var records = from e in _context.GetTable<Employee>() join d in _context.GetTable<Department>()  on e.DepartmentId equals d.DepartmentId select new {e,d};
            
            foreach (var record in records)
            {
                Console.WriteLine(record.e.Name + " " + record.e.Age + " " + record.e.Sex + " " + record.d.Name);
            }
            
        }
        
        [TestMethod]
        public void TestXml()
        {
            
            var companyXml = new XElement("company",
                                              from d in  _context.GetTable<Department>() 
                                              select new XElement("department",
                                                                        new XAttribute("name",d.Name.Trim()),
                                                                        from e in _context.GetTable<Employee>() 
                                                                        where e.DepartmentId==d.DepartmentId                                                                         
                                                                        select new XElement("employee", 
                                                                                                new XAttribute("name",e.Name.Trim()),new XElement("age",e.Age))));
            Console.WriteLine(companyXml);
        }
       

    }
}
