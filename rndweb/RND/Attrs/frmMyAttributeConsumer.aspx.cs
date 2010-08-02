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

namespace RND.Attrs
{
	/// <summary>
	/// Summary description for frmMyAttributeConsumer.
	/// </summary>
	[MyAttribute(10,Y=45)]
	public class frmMyAttributeConsumer : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here                        
            Type thisType = this.GetType();
            object[] attrs = thisType.GetCustomAttributes(typeof(MyAttribute),true);
            foreach(MyAttribute attr in attrs)
            {
                Response.Write("x : " + attr.X + ";y : " + attr.Y);
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
