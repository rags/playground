using System.Reflection;
using System.Reflection.Emit;
using System;
class HelloWorldEmitter
{
    public static void Main()
    {
      AssemblyName name = new AssemblyName();
      name.Name="HelloWorld";
      //.assembly HelloWorld{}
      AssemblyBuilder asmBuilder = AppDomain.CurrentDomain.DefineDynamicAssembly(name,AssemblyBuilderAccess.RunAndSave);
      ModuleBuilder mod = asmBuilder.DefineDynamicModule ("HelloWorld","HelloWorld.exe");//.module HelloWorld.exe
      //.class private auto ansi initbeforefield Helloworld
      TypeBuilder myClass =  mod.DefineType("HelloWorld",TypeAttributes.AutoClass | TypeAttributes.AnsiClass | TypeAttributes.BeforeFieldInit,null,PackingSize.Unspecified);            
      //.method public hidebysig static void Main() cil managed
      MethodBuilder method = myClass.DefineMethod("Main",MethodAttributes.Public |  MethodAttributes.Static | MethodAttributes.HideBySig ,CallingConventions.Standard,typeof(void),null);            
      ILGenerator ilGen =  method.GetILGenerator();      
      ilGen.Emit(OpCodes.Ldstr,"Hello World");      //ldstr      "Hello World"
      MethodInfo writeLineInfo = typeof(System.Console).GetMethod
                                                                                               (
                                                                                                  "WriteLine" ,
                                                                                                  BindingFlags.Static | BindingFlags.Public | BindingFlags.InvokeMethod,
                                                                                                  null,
                                                                                                  CallingConventions.Any | CallingConventions.VarArgs ,
                                                                                                  new Type[] {typeof(string)},null                                                                                                 
                                                                                                );      
      ilGen.EmitCall(OpCodes.Call,writeLineInfo,null);//call       void [mscorlib]System.Console::Write(string)
      ilGen.Emit(OpCodes.Ret);//ret
      asmBuilder.SetEntryPoint(method);//make .entrypoint        
      myClass.CreateType();
      Console.WriteLine("Run before save:");            
       myClass.InvokeMember("Main", BindingFlags.InvokeMethod  |  BindingFlags.Static | BindingFlags.Public  ,null, null,null);
      asmBuilder.Save("HelloWorld.exe");      
      Console.WriteLine("HelloWorld.exe saved...\nRun after save:");           
     AppDomain.CurrentDomain.ExecuteAssembly("HelloWorld.exe");
    }
}
