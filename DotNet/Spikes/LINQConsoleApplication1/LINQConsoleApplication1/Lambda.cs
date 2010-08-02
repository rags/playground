using System;
using System.Collections.Generic;
using System.Text;
using System.Query;
using System.Xml.XLinq;
using System.Data.DLinq;

namespace LINQConsoleApplication1
{
    class Lambda
    {
        delegate T foo<T>(T t);
        delegate T2 bar<T1,T2>(T1 t,T2 t1);
        static void Main(string[] args)
        {
            var i = 5;
            i++;
            lambda();
            Console.WriteLine(((foo<int>)blah => blah*blah)(4));
            Console.WriteLine(((bar<int,int>)(blah,blah1) => (blah>blah1)?blah:blah1)(4,5));
            Console.ReadLine();
        }

        private static void lambda()
        {
            foo<int> foo1 = delegate(int x)
                                {
                                    return ++x;
                                };
            foo<int> foo2 = x => 245;
            Console.WriteLine(foo1(3));
            Console.WriteLine(foo2(4));
            Console.WriteLine(((foo<int>)x => --x)(4));
        }
    }
}
