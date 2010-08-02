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
using System.Resources;
using System.Threading;
using System.Globalization;

namespace RND.Localization
{
	/// <summary>
	/// Summary description for frmResource.
	/// </summary>
	public class frmResource : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{      
      Thread.CurrentThread.CurrentCulture = CultureInfo.CreateSpecificCulture(Request.UserLanguages[0]);
      Thread.CurrentThread.CurrentUICulture = new CultureInfo(Request.UserLanguages[0]);
      ResourceManager res = new ResourceManager("RND.frmResource.aspx",typeof(frmResource).Assembly);
      Response.Write(res.GetString("msg"));
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
