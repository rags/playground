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

namespace RND1
{
	/// <summary>
	/// Summary description for frmConsumeMyService.
	/// </summary>
	public class frmConsumeMyService : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            Response.Write("Session: " + Session.SessionID);
      localhost.MyService service = new localhost.MyService();
      service.CookieContainer = new System.Net.CookieContainer();
      string init = service.returnSession("hi");
      string second =service.returnSession("hello");
      string third =service.returnSession("what?");
      Response.Write("[" +init + "]<br>[" + second + "]<br>[" +third + "]");
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
