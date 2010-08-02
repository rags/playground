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
using System.Xml.XPath;

namespace RND.XML
{
	/// <summary>
	/// Summary description for frmNavigator.
	/// </summary>
	public class frmNavigator : System.Web.UI.Page
	{
    protected System.Web.UI.HtmlControls.HtmlGenericControl frame1;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here      
      XPathNavigator  nav = new XPathDocument(Server.MapPath("Emp.xml")).CreateNavigator();
      Response.Write("Nodetype: [" +nav.NodeType  + "]");
      
      if(!IsPostBack) frame1.Attributes.Add("src","emp.xml");
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
