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

namespace RND.ViewStateAndSerialization
{
	/// <summary>
	/// Summary description for frmViewStateToSession.
	/// </summary>
	public class frmViewStateToSession : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.Button btnPostBack;
        protected System.Web.UI.WebControls.Label lbl;
        protected System.Web.UI.HtmlControls.HtmlSelect cboTest;
    
        protected override object LoadPageStateFromPersistenceMedium()
        {            
            return new LosFormatter(EnableViewStateMac,ViewStateUserKey).Deserialize(Session["viewState"] as string);
        }

        protected override void SavePageStateToPersistenceMedium(object viewState)
        {            
            StringWriter writer = new StringWriter();
            new LosFormatter(EnableViewStateMac,ViewStateUserKey).Serialize(writer,viewState);
            Session["viewState"] = writer.ToString();
        }


		private void Page_Load(object sender, System.EventArgs e)
		{			
            if(!IsPostBack)
            {
                cboTest.DataSource = new string[] {"item1","item2","item3","item4"};
                cboTest.DataBind();
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
            this.btnPostBack.Click += new System.EventHandler(this.btnPostBack_Click);
            this.Load += new System.EventHandler(this.Page_Load);

        }
		#endregion

        private void btnPostBack_Click(object sender, System.EventArgs e)
        {
            lbl.Text = "not ok ok";            
        }
	}
}
