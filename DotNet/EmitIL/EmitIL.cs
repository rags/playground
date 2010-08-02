using System;
using System.Reflection;
using System.Reflection.Emit;

namespace EmitIL
{
    class MyEmit
    {
    
        private static void Main()
        {
            AssemblyName name = new AssemblyName();
            name.Name = "Printer";
            //.assembly Printer{}
            AssemblyBuilder printerBuilder = AppDomain.CurrentDomain.DefineDynamicAssembly(name, AssemblyBuilderAccess.Save);
            //namespace PrinterSpace
            //{
            //class printer : System.Object
            //{
            TypeBuilder printerClass = printerBuilder.DefineDynamicModule("Printer", "Printer.dll").DefineType("PrinterSpace.Printer", TypeAttributes.Public);
            Type typeDateTime = typeof(DateTime);
            Type typeObject = typeof(object);
            //private DateTime time;
            FieldBuilder fieldTime = printerClass.DefineField("time", typeDateTime, FieldAttributes.Private);
            
            //public Printer()
            //{
            ConstructorBuilder defPrinterConst = printerClass.DefineConstructor(MethodAttributes.Public, CallingConventions.Standard, null);
            ILGenerator ilGen = defPrinterConst.GetILGenerator();
            
            ilGen.Emit(OpCodes.Ldarg_0);//load this
            ilGen.Emit(OpCodes.Call, typeObject.GetConstructor(new Type[0]));//base(); i.e System.Object's constructor
            /*********************************************this.time = DateTime.Now;*****************************************/
            ilGen.Emit(OpCodes.Ldarg_0);            
            MethodInfo dateTimeNow = typeDateTime.GetMethod("get_Now", BindingFlags.Static | BindingFlags.Public | BindingFlags.GetProperty, null, CallingConventions.Standard, new Type[]{}, null);
            ilGen.Emit(OpCodes.Call, dateTimeNow);
            ilGen.Emit(OpCodes.Stfld, fieldTime);
            /*********************************************end this.time = DateTime.Now;*****************************************/
            ilGen.Emit(OpCodes.Ret);//return;
            //} - end of default const

            //public Printer(DtaeTime time)
            //{
            ilGen = printerClass.DefineConstructor(MethodAttributes.Public, CallingConventions.Standard, new Type[]{typeDateTime}).GetILGenerator();
            /****************************************************this.base()*************************************/
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Call, typeObject.GetConstructor(new Type[]{}));
            /***************************************************************************************************/
            /*xxxxxxxxxxxxxxxxxxxxxxxx this.time = time; xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Ldarg_1);
            ilGen.Emit(OpCodes.Stfld, fieldTime);
            ilGen.Emit(OpCodes.Ret);
            /*xxxxxxxxxxxxxxxxxxxxxxxxxxx end this.time = time; xxxxxxxxxxxxxxxxxxxxxxxxxxx*/
            //}   - end of constructor

            //Public DateTime Time
            //{
            //get
            //{
            PropertyBuilder propTime = printerClass.DefineProperty("Time", PropertyAttributes.None, typeDateTime, new Type[]{typeDateTime});
            MethodBuilder getTime = printerClass.DefineMethod("get_Time", MethodAttributes.Public | MethodAttributes.HideBySig | MethodAttributes.SpecialName, CallingConventions.Standard, typeDateTime, null);
            ilGen = getTime.GetILGenerator();
            /******************************************************* <return this.time;> **********************************/
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Ldfld, fieldTime);
            /******************************************************* </return this.time;> **********************************/
            ilGen.Emit(OpCodes.Ret);
            propTime.SetGetMethod(getTime);
            //}

            //set
            //{
            MethodBuilder setTime = printerClass.DefineMethod("set_Time_NAME_CHANGED"/*changed the name here*/,MethodAttributes.Public | MethodAttributes.HideBySig | MethodAttributes.SpecialName, CallingConventions.Standard, typeof(void), new Type[]{typeDateTime});
            ilGen = setTime.GetILGenerator();
            /******************************************************* <this.time = value;> **********************************/   
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Ldarg_1);
            ilGen.Emit(OpCodes.Stfld, fieldTime);
            /******************************************************* </this.time = value;> **********************************/   
            ilGen.Emit(OpCodes.Ret);
            propTime.SetSetMethod(setTime);
            //}
            //}- end of Time property

            Type typeString = typeof(string);
            MethodInfo writeLineInfo = typeof(Console).GetMethod("WriteLine", BindingFlags.Static | BindingFlags.Public | BindingFlags.InvokeMethod, null, CallingConventions.Any, new Type[]{typeof(string)}, null);
            //public static Print(string msg)
            //{            
            MethodBuilder statPrint = printerClass.DefineMethod("Print", MethodAttributes.Public | MethodAttributes.Static | MethodAttributes.HideBySig, CallingConventions.Standard, typeof(void), new Type[]{typeString});
            ilGen = statPrint.GetILGenerator();
            /******************************************************* <WriteLIne(msg);> ************************************/
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Call, writeLineInfo);
            /******************************************************* </WriteLIne(msg);> ************************************/
            ilGen.Emit(OpCodes.Ret);
            //}

            //private print
            //{
            MethodBuilder privatePrint = printerClass.DefineMethod("Print", MethodAttributes.Private, CallingConventions.Standard, typeof(void), null);
            ilGen = privatePrint.GetILGenerator();
            //<WriteLine(this.time);>
            ilGen.Emit(OpCodes.Ldarg_0);//load this
            ilGen.Emit(OpCodes.Ldflda, fieldTime);//load this.time
            ilGen.Emit(OpCodes.Call, typeDateTime.GetMethod("ToString", new Type[0]));//this.time.ToSting();
            ilGen.Emit(OpCodes.Call, writeLineInfo);//write(this.time.ToSting());
            //</WriteLine(this.time);>
            ilGen.Emit(OpCodes.Ret);
            //}

            Type typeInt = typeof(int);
            //public void Print(string msg,int times)            
            MethodBuilder publicPrint = printerClass.DefineMethod("Print", MethodAttributes.Public , CallingConventions.Standard, typeof(void), new Type[]{typeString, typeInt});
            ilGen = publicPrint.GetILGenerator();
            //{
            ilGen.DeclareLocal(typeInt);//int i;
            //<this.Print();>
            ilGen.Emit(OpCodes.Ldarg_0);
            ilGen.Emit(OpCodes.Call, privatePrint);
            //</this.Print();>
            Label lblBeginLoop = ilGen.DefineLabel();
            Label lblEndLoop = ilGen.DefineLabel();
            //for(
            //<i=0>
            ilGen.Emit(OpCodes.Ldc_I4_0);
            ilGen.Emit(OpCodes.Stloc_0);
            //</i=0>;.....
            ilGen.Emit(OpCodes.Br_S, lblEndLoop);//go to end
            //{ 
            ilGen.MarkLabel(lblBeginLoop);//begin:
            //<WriteLIne(msg);>
            ilGen.Emit(OpCodes.Ldarg_1);
            ilGen.Emit(OpCodes.Call, writeLineInfo);
            //</WriteLIne(msg);>
            //<i++>
            ilGen.Emit(OpCodes.Ldloc_0);
            ilGen.Emit(OpCodes.Ldc_I4_1);
            ilGen.Emit(OpCodes.Add);
            ilGen.Emit(OpCodes.Stloc_0);
            //</i++>
            ilGen.MarkLabel(lblEndLoop);//end:
            //i<times; i.e <if(i<times) goto begin;>
            ilGen.Emit(OpCodes.Ldloc_0);
            ilGen.Emit(OpCodes.Ldarg_2);
            ilGen.Emit(OpCodes.Blt_S, lblBeginLoop);
            //<if(i<times) goto begin;>
            ilGen.Emit(OpCodes.Ret);
            //} end print
            printerClass.CreateType();
            //}end class
            printerBuilder.Save("Printer.dll");//make printer.dll
            //}end namespace

            name = new AssemblyName();
            name.Name = "MyAsm";
            //.assembly MyAsm{}
            AssemblyBuilder asmBuilder = AppDomain.CurrentDomain.DefineDynamicAssembly(name, AssemblyBuilderAccess.RunAndSave);

            //class Test            
            TypeBuilder myClass = asmBuilder.DefineDynamicModule("test", "test.exe").DefineType("Test", TypeAttributes.AutoClass | TypeAttributes.BeforeFieldInit, null, PackingSize.Unspecified);
            //{
            //public static void Main() - or MYMain() names doesnt matter            
            MethodBuilder main = myClass.DefineMethod("MyMain", MethodAttributes.Public| MethodAttributes.Static , CallingConventions.Standard, typeof(void), null);
            ilGen = main.GetILGenerator();
            //{
            ilGen.DeclareLocal(printerClass);//Printer objPrinter;
            LocalBuilder v_1 = ilGen.DeclareLocal(typeDateTime);//v_1
            //<objPrinter = new Printer();>
            ilGen.Emit(OpCodes.Newobj, defPrinterConst);
            ilGen.Emit(OpCodes.Stloc_0);
            //</objPrinter = new Printer();>
            
            //<objPrinter.Time = DateTime.Now.AddHours(5);>
            ilGen.Emit(OpCodes.Ldloc_0);
            ilGen.Emit(OpCodes.Call, dateTimeNow);
            ilGen.Emit(OpCodes.Stloc_1);
            ilGen.Emit(OpCodes.Ldloca_S, v_1);
            ilGen.Emit(OpCodes.Ldc_R8, 5.0);
            ilGen.Emit(OpCodes.Call, typeDateTime.GetMethod("AddHours"));
            ilGen.Emit(OpCodes.Call, setTime);
            //<objPrinter.Time = DateTime.Now.AddHours(5);>

            //Printer.Print("Hello");
            ilGen.Emit(OpCodes.Ldstr, "Hello");
            ilGen.Emit(OpCodes.Call, statPrint);
            
            //<objPrinter.Print("Hiya");>
            ilGen.Emit(OpCodes.Ldloc_0);
            ilGen.Emit(OpCodes.Ldstr, "Hiya");
            ilGen.Emit(OpCodes.Ldc_I4_S, 20);
            ilGen.Emit(OpCodes.Callvirt, publicPrint);
            //<objPrinter.Print("Hiya");>

            //<objPrinter.GetType().InvokeMember("Print",BindingFlags.NonPublic|BindingFlags.Instance|BindingFlags.InvokeMethod,null,objPrint,null); >
            ilGen.Emit(OpCodes.Ldloc_0);
            ilGen.Emit(OpCodes.Callvirt, typeof(object).GetMethod("GetType"));
            ilGen.Emit(OpCodes.Ldstr, "Print");//method name
            ilGen.Emit(OpCodes.Ldc_I4, 292);//BindingFlags
            ilGen.Emit(OpCodes.Ldnull);//binder
            ilGen.Emit(OpCodes.Ldloc_0);//target
            ilGen.Emit(OpCodes.Ldnull);//args[]
            ilGen.Emit(OpCodes.Call, typeof(Type).GetMethod("InvokeMember", new Type[]{typeString, typeof(BindingFlags), typeof(Binder), typeof(object), typeof(object[])}));
            ilGen.Emit(OpCodes.Pop);//remove return value from invoke member from the stack
            //</objPrinter.GetType().InvokeMember>
            ilGen.Emit(OpCodes.Ret);//return;
            asmBuilder.SetEntryPoint(main);//set this function as entry point
            //}end of main
            myClass.CreateType();
            //}end of class
            asmBuilder.Save("Test.exe");//make test.exe            
        }
    }

}
