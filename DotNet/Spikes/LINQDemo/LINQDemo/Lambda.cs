using System;
using System.Expressions;
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
        
        [TestMethod]
        public void Expression_()
        {
            Expression<Func<int,int>> exp = x=>
            x* x ;
            
            Console.WriteLine(exp.Body);
            Console.WriteLine(exp.GetType());
            Console.WriteLine(exp);
            Console.WriteLine(exp.Compile()(3));
            BinaryExpression body = (BinaryExpression) exp.Body;
            var res =
                Expression.Lambda<Func<int, int>>(Expression.Multiply(body, exp.Parameters[0]),
                                                  exp.Parameters).Compile()(3);
            Console.WriteLine(res);
        }
        
        [TestMethod]
        public void Expression1()
        {
            Expression<Func<int>> exp1 = ()=>1 ;
            Expression<Func<int,int>> exp2 = (int x)=>x ;
            
            Console.WriteLine(exp1);
            Console.WriteLine(exp2);
        }
        
        delegate void delegatefoo();
        [TestMethod]
        public void StatementDel()
        {
            delegatefoo foo = ()=>
            {
                Console.WriteLine("Hello");
                Console.WriteLine(" World");
                Console.WriteLine(123);
            }
            ;
            foo();
        }
        
    }
}