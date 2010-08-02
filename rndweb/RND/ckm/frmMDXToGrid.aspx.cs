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
using System.Data.OleDb;


namespace RND
{
	/// <summary>
	/// Summary description for WebForm1.
	/// </summary>
	public class WebForm1 : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.DataGrid DataGrid1;
    public string str=string.Empty;
    
		private void Page_Load(object sender, System.EventArgs e)
		{			
            OleDbConnection  cn = new OleDbConnection("Provider=MSOLAP; Datasource=LocalHost; Initial Catalog=FoodMart 2000;uid=sa");
            OleDbDataAdapter da = new OleDbDataAdapter("select Order({[Store].Members},PROFIT,desc)  on rows, {Crossjoin({[All products]},{ [Store Cost],[Store Sales]})} on columns from Sales ",cn);      
            DataTable dt = new DataTable();
            da.Fill(dt);
            DataGrid1.AutoGenerateColumns=false;
            GenerateCols(dt,DataGrid1);
            DataGrid1.DataSource=dt.DefaultView;
            DataGrid1.DataBind();
    }
    private void GenerateCols(DataTable dt,DataGrid dg)
    {
      foreach(DataColumn dc in dt.Columns)
      {
      BoundColumn bc = new BoundColumn();
      bc.HeaderText=dc.ColumnName;
      bc.DataField=dc.ColumnName;
      dg.Columns.Add(bc);
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
