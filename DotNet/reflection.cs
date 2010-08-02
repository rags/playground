using System;
using System.Reflection;
class Reflect
{
    public static void Main()
    {
    //  Assembly asm1 = Assembly.LoadFile(@"e:\rags\rnd\dotnet\temp\Component.dll");
      Assembly asm = Assembly.LoadFile(@"e:\rags\rnd\dotnet\Consumer.dll");      
      AppDomain.CurrentDomain.Load(asm.FullName);
      asm.GetType("Consumer").InvokeMember("Function",BindingFlags.InvokeMethod | BindingFlags.Static | BindingFlags.Public ,null,null,new object[0]);
    }
}
