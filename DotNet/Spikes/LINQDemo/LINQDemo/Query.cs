using System;
using System.Data.DLinq;
using System.Query;
using System.Collections.Generic;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
    [TestClass]
    class Query
    {
        [TestMethod]
        public void TestSelect()
        {
            var emps = EmployeeCollection.Get().Where(e=>e.Age>40).Select(e=>e);
            Assert.AreEqual(3,emps.Count(e=>true));
            foreach (var emp in emps)
            {
                Console.WriteLine(emp.Name);
            }
        } 
        
        [TestMethod]
        public void TestSelect1()
        {
            var emps = from e in EmployeeCollection.Get() where 
            e.Name.Length > 4 select e ;  
            Assert.AreEqual(4,emps.Count(e=>true));
            
            foreach (var emp in emps)
            {
                Console.WriteLine(emp.Name);
            }
        }
    }
}
