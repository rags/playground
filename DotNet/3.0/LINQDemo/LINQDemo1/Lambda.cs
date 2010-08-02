using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Query;

namespace LINQDemo
{
    [TestClass]
    internal class Lambda
    {
        delegate int foo();
        [TestMethod]
        public void Test()
        {
            Assert.AreEqual(3, ((Func<int>)() => 1+2)());
            Assert.AreEqual(9, ((Func<int,int>)x => x*x)(3));
            Assert.AreEqual(9, ((Func<int,int>)x => x*x)(3));
            foo f = ()=>
            9;
            f += ()=> 10;
            f += ()=> 11;
            Console.WriteLine(f());
            
            foo f1 = 
            delegate()
                {
                    Console.WriteLine(1);
                    return 1;
                };
            
            f1 += 
            delegate()
                {
                    Console.WriteLine(2);
                    return 2;
                };
            Console.WriteLine(f1());
            
        }
        
        

        [TestMethod]
        public void Recursion()
        {
            Assert.AreEqual(120, 
                ((Func<int,object,int>)(x,func)=>x>1?(x*((Func<int,object,int>)func)(x-1,func)):1)
            (5,((Func<int,object,int>)(x,func)=>x>1?(x*((Func<int,object,int>)func)(x-1,func)):1))
                );
            
        }
        
        [TestMethod]
        public void Recursion1()
        {
            Assert.AreEqual(120,((Func<int, int>)  x => ((Func<int, object, int>)(y, func) => y == 0 ? 1 : (y*((Func<int,object,int>)func)(y-1,func)))(x, ((Func<int, object, int>)(y, func) => y == 0 ? 1 : (y*((Func<int,object,int>)func)(y-1,func)))))(5)); 
        } 
        
        [TestMethod]
        public void Recursion2()
        {
            Func<int,object,int> recusiveFact = (x,func)=> x > 1 ? (x*((Func<int, object, int>) func)(x - 1, func)) : 1;
            Func<int,int> fact = x =>
            recusiveFact(x, recusiveFact);
            Assert.AreEqual(120,fact(5));
        }
    }
}