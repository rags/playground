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
	/// Summary description for frmRND.
	/// </summary>
	public class frmRND : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.HyperLink lnkCustomer;
    protected System.Web.UI.HtmlControls.HtmlGenericControl  xxx;
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            xxx.Attributes.Add("href",@"/pickm/xxx.css");
      try
      {
        Response.Write("[" + Convert.ToInt32(Convert.DBNull) + "]");    
      }
      catch(Exception ex) {Response.Write(ex.Message);}
      try
      {
        Response.Write("[" + Convert.DBNull.ToString()+ "]<br>");
        Response.Write("[" + Convert.DBNull as string + "]");
      }
      catch(Exception ex) {Response.Write(ex.Message);}
        System.Diagnostics.Process.Start("cmd.exe",@" /c dir>C:\DOCUME~1\RAGHUN~1\Desktop\dir.txt").WaitForExit();
      //Response.Write("Session: " + Session.SessionID);
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
