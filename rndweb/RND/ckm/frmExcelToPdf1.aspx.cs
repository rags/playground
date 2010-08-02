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
using ACRODISTXLib;

namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmExcelToPdf.
	/// </summary>
	public class frmExcelToPdf1 : System.Web.UI.Page
	{
        private void Page_Load(object sender, System.EventArgs e)
        {
            PdfDistiller dist = new PdfDistillerClass();
            dist.bSpoolJobs = 1;
            dist.bShowWindow = 0;
            dist.FileToPDF(@"C:\Documents and Settings\raghunandanr\Desktop\measure list.ps",null,null);
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
