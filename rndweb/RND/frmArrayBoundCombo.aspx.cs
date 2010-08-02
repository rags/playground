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
	/// Summary description for frmExcel.
	/// </summary>
    public class frmArrayBoundCombo : System.Web.UI.Page
    {
        protected System.Web.UI.WebControls.ListBox ListBox1;
        protected System.Web.UI.WebControls.Button btn;
        protected System.Web.UI.HtmlControls.HtmlSelect Dropdownlist2;
        protected System.Web.UI.WebControls.DropDownList DropDownList1;
    
  
        private void Page_Load(object sender, System.EventArgs e)
        {
            // Put user code to initialize the page here      
            if(!IsPostBack)
            {
                string [][] vals=new string[] [] {
                                                     new string [] {"1","2","3"},
                                                     new string [] {"a","b","c"}};
                Dropdownlist2.DataSource = ListBox1.DataSource=DropDownList1.DataSource=new string [] {"a","b","c"};
                //DropDownList1.Items.Add(new ListItem("",""));
                DropDownList1.DataBind();
                ListBox1.DataBind();
                Dropdownlist2.DataBind();
            }
            Response.Write(Dropdownlist2.DataSource);
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
            this.Load +=new EventHandler(Page_Load); 
        }
        #endregion
    
    }
}
