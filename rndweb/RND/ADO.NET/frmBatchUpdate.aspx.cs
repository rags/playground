using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Web;
using System.Web.SessionState;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.HtmlControls;
using System.Configuration;

namespace RND.ADO.NET
{
	/// <summary>
	/// Summary description for frmBatchUpdate.
	/// </summary>
	public class frmBatchUpdate : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            update1();
		}

        void update1()
        {
            SqlCommand comm = new SqlCommand("insert into tblEmployee(EmployeeName,Sex,Age,DepartmentId) value(@a,'@b',@c,@d)",new SqlConnection(ConfigurationSettings.AppSettings["connectionString"]));
            comm.Connection.Open();
            comm.Prepare();
            comm.Parameters.Add(new SqlParameter("@a","'Ragz'"));
            comm.Parameters.Add(new SqlParameter("@b","M"));
            comm.Parameters.Add(new SqlParameter("@c",23));
            comm.Parameters.Add(new SqlParameter("@d",1));            
            comm.ExecuteNonQuery();
            comm.Connection.Close();
        }

        void update2()
        {
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
