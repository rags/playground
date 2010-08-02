using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
    [TestClass]
    class ObjectInit
    {
        
        class Employee
        {
            int _empId;
            string _empName;


            public int EmployeeId
            {
                get { return _empId; }
                set { _empId = value; }
            }

            public string EmployeeName
            {
                get { return _empName; }
                set { _empName = value; }
            }
        }
        
        [TestMethod]
        public void Test()
        {
            Employee emp = new Employee{EmployeeName="foo",EmployeeId=001};
            Assert.AreEqual("foo",emp.EmployeeName);
            Assert.AreEqual(1,emp.EmployeeId);
        }
        
    }
}
