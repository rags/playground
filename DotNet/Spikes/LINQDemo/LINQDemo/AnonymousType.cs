using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
    [TestClass] 
    internal class AnonymousType
    {
        [TestMethod]
        public void Test()
        {
            var employee1 = new {Name = "emp1", Age = 21, Sex = 'M'};
            var employee2 = new {Name = "emp2", Age = 23, Sex = 'F'};
            Assert.AreEqual(typeof(string),employee1.Name.GetType());
            Assert.AreEqual(typeof(int),employee1.Age.GetType());
            Assert.AreEqual(typeof(char),employee1.Sex.GetType());
            Assert.AreEqual(employee1.GetType(),employee2.GetType());
        }
        
        [TestMethod]
        public void Test2()
        {
            var employee1 = getemp1();
            var employee2 = getemp2();
            Assert.AreNotEqual(employee1.GetType(),employee2.GetType());
        }
        
        public object getemp1()
        {
            return new {Name = "emp1", Age = 21, Sex = 'M'};
        }
        
        public object getemp2()
        {
            return new {Name = "emp1", Age = 21, Sex = 'M'};
        }
        
           class Employee
            {
               string _name;
               int _age;
               char _sex;


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

               public char Sex
               {
                   get { return _sex; }
                   set { _sex = value; }
               }
            }
        [TestMethod]
        public void Test1()
        {
            var employee1 = new {Name = "emp1", Age = 21, Sex = 'M'};
            var employee2 = new Employee{Name = "emp1", Age = 21, Sex = 'M'};
            Assert.AreNotEqual(employee1.GetType(),employee2.GetType());
        }
    }
}