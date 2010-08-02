using System;
class x:IDisposable
{
 public void Dispose()
 {
    Console.Write("called");
 }
 public static void Main()
 {
    
    using(new x()){}
 }
}

