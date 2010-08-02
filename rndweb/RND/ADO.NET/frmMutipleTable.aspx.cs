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
using System.Data.SqlClient;

namespace RND
{
	/// <summary>
	/// Summary description for frmMutipleTable.
	/// </summary>
	public class frmMutipleTable : System.Web.UI.Page
	{
		protected System.Web.UI.WebControls.DataGrid dgEmployee;
		protected System.Web.UI.WebControls.DataGrid dgDepartment;
		protected System.Web.UI.WebControls.DataGrid dgEmployee1;
		protected System.Web.UI.WebControls.DataGrid dgDepartment1;
	
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here			
			SqlDataAdapter adapter = new SqlDataAdapter("uspGetData",System.Configuration.ConfigurationSettings.AppSettings["connectionString"]);
			DataSet ds = new DataSet("RND");
			adapter.Fill(ds);
			dgEmployee.DataSource=ds.Tables[0].DefaultView;
			dgDepartment.DataSource=ds.Tables[1].DefaultView;
			dgDepartment.DataBind();
			dgEmployee.DataBind();
			//////////////////////////////////////
			
			SqlConnection conn =  new SqlConnection(System.Configuration.ConfigurationSettings.AppSettings["connectionString"]);
			conn.Open();
			SqlCommand comm = new SqlCommand("uspGetData",conn);
			SqlDataReader reader = comm.ExecuteReader();
			dgEmployee1.DataSource=reader;
			dgEmployee1.DataBind(); //bind b4 nextresult
			reader.NextResult();
			dgDepartment1.DataSource=reader;
			dgDepartment1.DataBind();
			//dgEmployee1.DataBind(); //bind b4 nextresult

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
