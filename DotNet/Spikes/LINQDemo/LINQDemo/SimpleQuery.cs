using System;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Query;

namespace LINQDemo
{
    [TestClass]
    internal class SimpleQuery
    {
        private List<string> _list;

        [TestInitialize]
        public void Init()
        {
            _list = new List<String>
            {
                "This",
                "is",
                "a",
                "...",
                " test"
            };
        }

        [TestMethod]
        public void TestSimpleQuery()
        {
            var selectedList = from str in _list where str.Length > 2 select str;
            Assert.AreEqual(3, selectedList.Count());
            _list.Add("someStr");
            Assert.AreEqual(4, selectedList.Count());
        }
        
        
        
        [TestMethod]
        public void Maptest()
        {
            var selectedList = from str in _list where str.Length < 3 select str;
            var charCnt = selectedList.Aggregate(0,(cnt,s)=>cnt + s.Length);
            Assert.AreEqual(15,charCnt);
        }
        
        
        
        
        [TestMethod]
        public void Avg()
        {
            Assert.AreEqual(41.5,EmployeeCollection.Get().Average(e=>e.Age));
        }
 
        [TestMethod]
        public void Lettest()
        {
            var intlist = new List<int> {1,2,3}
            ;
            var list = from x in intlist let y=x++  let x1=x let z=x--  select
            new
            {
               x,y,Z=y.ToString(),z,x1,x2=x
            }
            ;
            intlist.Add(4);
            intlist.Add(5);
            foreach (var item in list)
            {
                Console.WriteLine(item.x + " " + item.y + " " + item.Z + " " + item.z + " " + item.x1 + " " + item.x2) ;
            }
        }
 
        [TestMethod]
        public void Sum()
        {
            Assert.AreEqual(
                EmployeeCollection.Get().Aggregate(0,(sum,e)=>sum + ((e.Age>40)?e.Salary:0)),
                            EmployeeCollection.Get().Where(e=>e.Age>40).Sum(e=>e.Salary));
            
        }
    }
}