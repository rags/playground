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
	/// Summary description for frmRepeater.
	/// </summary>
	public class frmRepeater : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.Label blb;
        protected System.Web.UI.WebControls.Button btn;
        protected System.Web.UI.WebControls.DropDownList cbo;
        protected System.Web.UI.WebControls.DataGrid grid;
        protected System.Web.UI.WebControls.Repeater repeater;
    
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            if(!IsPostBack) 
            {
                blb.Text="Title";
                ArrayList arr = new ArrayList();
                arr.Add("Sfsf");arr.Add(0);arr.Add(56.68);arr.Add(34);            
                repeater.DataSource = arr;
                repeater.DataBind();
                string[] arr1 = new string[] {"x","y","z"};
                cbo.DataSource = arr1;
                cbo.DataBind();
                grid.DataSource = arr1;
                grid.DataBind();
                ViewState["xxx"]="xxx";
                return;
            }
            Response.Write("[" +ViewState["xxx"] +"]");
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
            this.cbo.SelectedIndexChanged += new System.EventHandler(this.cbo_SelectedIndexChanged);
            this.Load += new System.EventHandler(this.Page_Load);

        }
		#endregion

        public void x(object sender,EventArgs e)        
        {
            Control container = ((Repeater)sender).NamingContainer;
        }

        public void y(object sender,RepeaterItemEventArgs e)        
        {
            Control container = ((Repeater)sender).NamingContainer;
        }

        private void cbo_SelectedIndexChanged(object sender, System.EventArgs e)
        {
            Response.Write("fired!");
        }
	}
}
