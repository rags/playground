using System;
using System.Collections.Generic;
using System.Expressions;
using System.Query;
using System.Runtime.CompilerServices;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LINQDemo
{
 [TestClass]
    class Class1
    {
     
     [TestMethod]
     public void TestInf()
     {
         var s = "Hello world";
         int i = s.Length;
         var x = i++;
         Console.WriteLine(s +" " + i);
     }
     
     [TestMethod]
     public void init()
     {
         var x = new Employee
         {
             Id = 12,
             Name = "foo",
             Age=23
         }
         ;
         Console.WriteLine(x.Name);
       
     }
     
     [TestMethod]
    public void CollectionInit()
     {
         var strs = new List<Employee>
         {
             new Employee
         {
             Id = 12,
             Name = "foo",
             Age=23
         },
             new Employee
         {
             Id = 12,
             Name = "foo",
             Age=23
         },new Employee
         {
             Id = 12,
             Name = "foo",
             Age=23
         }
             
         }
         ;
         
     }
     
     [TestMethod]
     public void Anon()
     {
         var x = new {Sex='m',Age=23,Name = "asfsf"}
         ;
         
         var _x = new {Name = "asfsf",Sex='m',Age=23}
         ;
         Assert.AreEqual(x.GetType(),_x.GetType());
         
     }
     
     [TestMethod]
     public void ExtEtxt()
     {
         Assert.AreEqual("FOO","foo".Capitalize());
         Assert.AreEqual("FOO",Ext.Capitalize("foo"));
     }
     
     [Extension]
    public static class Ext
    {
        [Extension]
        public static string Capitalize(string str)
    {
        return str.ToUpper();
    }
    }
     
     delegate int del1();
     delegate void del2();
     [TestMethod]
    public void lambda()
    {
         del1 bar = this.bar(3);
         Console.WriteLine(bar());
         Console.WriteLine(bar());
         Console.WriteLine(this.bar(4)());
         
         
    }

     private del1 bar(int i)
     {
           return ()=>i;
        
        
     }
     
     public void lambda1()
     {
         Console.WriteLine(((Func<int,int,int>)(x,int y)=>
         x* y)(2,3));
     }
     
     public void lambda2()
     {
         Expression<Func<int,int,int>> exp = (x,int y)=> x* y;
         exp.Compile()(2, 3);
     }
     
     
     /*public static class Ext2
    {
        public static string Capitalize(this string str)
    {
        return str.ToUpper();
    }
    }*/
    
    }
}
