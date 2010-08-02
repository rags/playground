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
	/// Summary description for frmEvent.
	/// </summary>
	public class frmEvent : System.Web.UI.Page
	{
		public delegate void MyEventHandler(object msg);
		public event MyEventHandler handler;
		public event MyEventHandler handler1;

		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
			handler += new MyEventHandler(StringHandler);
			handler1 += new MyEventHandler(IntHandler);
			string msg = Request.QueryString["msg"];
			try
			{
				int no = int.Parse(msg);
				handler1(no);
			}
			catch
			{
				handler(msg);
			}
			finally
			{
				MyEventHandler mydelegate  = new MyEventHandler(DelegateHandler);
				mydelegate(msg);
			}
		    }
		public void DelegateHandler(object msg) 
		{
			Response.Write("<br>hi from delegate itself......... " + msg + "isnt a gr8 msg!");
		}
		public void StringHandler(object msg)
		{
			Response.Write("You've chosen string : " + msg);
		}
		public void IntHandler(object msg)
		{
			Response.Write("You've chosen int: " + msg);
		}

		#region Web Form Designer generated code
		override protected void OnInit(EventArgs e)
		{
			//
			// CODEGEN: This call is required by the ASP.NET Web Form Designer.
			//
            Response.Flush();
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
