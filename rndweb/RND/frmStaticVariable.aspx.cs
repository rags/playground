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

namespace RND
{
	/// <summary>
	/// Summary description for frmStaticVariable.
	/// </summary>
	public class frmStaticVariable : System.Web.UI.Page
	{
    static int x = 10;
    [ThreadStatic]static int y = 10;
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      Response.Write("[" + System.Threading.Thread.CurrentThread.Name +  "] x : " + x++);
      Response.Write(";y : " + y++);
      Response.Write("<br>Pooled? : " + System.Threading.Thread.CurrentThread.IsThreadPoolThread);
      Response.Write("<br>apartment : " + System.Threading.Thread.CurrentThread.ApartmentState);
      try
      {
        if(string.Empty.Equals(System.Threading.Thread.CurrentThread.Name+string.Empty)) System.Threading.Thread.CurrentThread.Name = x + " "  +y;        
      }
      catch{}
      if(y%50==0) 
      {
        Response.End();
        System.Threading.Thread.CurrentThread.Abort();         
      }
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
