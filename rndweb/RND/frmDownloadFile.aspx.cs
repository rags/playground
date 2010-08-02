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
using System.IO;

namespace RND
{
	/// <summary>
	/// Summary description for frmDownloadFile.
	/// </summary>
	public class frmDownloadFile : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{                
                string path = Server.MapPath(Request.QueryString["url"]);
                //System.IO.FileInfo file = new System.IO.FileInfo(path);
			    Response.Clear();                
                Response.AddHeader("Content-Disposition", "attachment; filename=" + Path.GetFileName(path));
                //Response.AddHeader("Content-Length",   file.Length.ToString()) ;
                Response.ContentType = "application/octet-stream";
                Response.WriteFile(path);
                Response.End();
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
