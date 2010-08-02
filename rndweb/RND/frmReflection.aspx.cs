using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Web;
using System.Web.SessionState;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.HtmlControls;
using System.Reflection;
using System.Reflection.Emit;

namespace RND
{
	/// <summary>
	/// Summary description for frmReflection.
	/// </summary>
	public class frmReflection : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{			
      AssemblyName name = new AssemblyName();
      name.Name="MyAsm";       
      AssemblyBuilder asmBuilder = AppDomain.CurrentDomain.DefineDynamicAssembly(name,AssemblyBuilderAccess.RunAndSave);      
      ModuleBuilder mod = asmBuilder.DefineDynamicModule ("HelloWorld","HelloWorld.exe");        
      TypeBuilder myClass =  mod.DefineType("MyClass",TypeAttributes.AutoClass | TypeAttributes.AnsiClass | TypeAttributes.BeforeFieldInit,null,PackingSize.Unspecified);            
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
      asmBuilder.SetEntryPoint(method);
      myClass.CreateType();
      asmBuilder.Save("HelloWorld.exe");      
		}

		#region Web Form Designer generated code
		override protected void OnInit(EventArgs e)
		{
			//
			// CODEGEN: This call is required by the ASP.NET Web Form Designer.
			//
			InitializeComponent();
			base.OnInit(e);
		}
		
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{    
			this.Load += new System.EventHandler(this.Page_Load);
		}
		#endregion
	}
}
