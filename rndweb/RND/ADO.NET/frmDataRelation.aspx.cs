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
	/// Summary description for frmDataRelation.
	/// </summary>
	public class frmDataRelation : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.CheckBoxList DropDownList1;
    protected System.Web.UI.WebControls.Label Label1;
    protected System.Web.UI.WebControls.DataGrid DataGrid1;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      if(!IsPostBack)
      {
        DataTable dt1=new DataTable("Employee"),dt2=new DataTable("Department");
        DataColumnCollection dc1=dt1.Columns,dc2=dt2.Columns;
        dc1.Add("EmployeeID",typeof(int));
        dc1.Add("Name",typeof(string));
        dc1.Add("DepartmentID",typeof(int));
        dc2.Add("DepartmentID",typeof(int));
        dc2.Add("Name",typeof(string));
         
        //dt1.PrimaryKey=new DataColumn[] {dc1["EmployeeID"]};
        //dt2.PrimaryKey=new DataColumn[] {dc2["DepartmentID"]};
        dt2.DisplayExpression=dt1.DisplayExpression="DepartmentID";       
        DataRow dr = dt1.NewRow();
        dr.ItemArray=new object[]{1,"rags",10};
        dt1.Rows.Add(dr);
        dr = dt1.NewRow();
        dr.ItemArray=new object[]{2,"rags1",10};
        dt1.Rows.Add(dr);
        dr = dt1.NewRow();
        dr.ItemArray=new object[]{3,"rags3",10};
        dt1.Rows.Add(dr);
        dr = dt1.NewRow();
        dr.ItemArray=new object[]{5,"rags5",11};
        dt1.Rows.Add(dr);
        dr = dt1.NewRow();
        dr.ItemArray=new object[]{4,"rags4",11};
        dt1.Rows.Add(dr);
        dt1.AcceptChanges();
        dr = dt2.NewRow();
        dr.ItemArray=new object[]{10,"dept1"};
        dt2.Rows.Add(dr);
        dr = dt2.NewRow();
        dr.ItemArray=new object[]{11,"dept2"};
        dt2.Rows.Add(dr);
        dr = dt2.NewRow();
        dr.ItemArray=new object[]{12,"dept3"};
        dt2.Rows.Add(dr);
        dt2.AcceptChanges();
        DataSet dst = new DataSet("CompanyDS");
        dst.Tables.AddRange(new DataTable[] {dt1,dt2});       
        dst.Relations.Add("DeptEmp",dc2["DepartmentID"],dc1["DepartmentID"]);
        DropDownList1.DataSource=dt2;
        DropDownList1.DataTextField="Name";
        DropDownList1.DataValueField="DepartmentID";
        DropDownList1.DataBind();        
        //strl.Attributes.Add("onclick","alert()");
        Session["dst"]=dst;
        //dst.WriteXml(Server.MapPath("XML/xmlfile1.xml"),XmlWriteMode.WriteSchema);        
        BindGrid();
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
      this.DropDownList1.SelectedIndexChanged += new System.EventHandler(this.DropDownList1_SelectedIndexChanged);
      this.Load += new System.EventHandler(this.Page_Load);

    }
		#endregion

    private void DropDownList1_SelectedIndexChanged(object sender, System.EventArgs e)
    {
      BindGrid();
    }

    void BindGrid()
    {

      DataView dv = ((DataSet)Session["dst"]).Tables["Employee"].DefaultView;
//      dv.RowFilter="DepartmentID=" + DropDownList1.SelectedItem.Value;
//      DataGrid1.DataSource=dv;      
//      DataGrid1.AutoGenerateColumns=true;                        
//      DataGrid1.DataBind();
    }
    protected string GetDeptName(object o)
    {
      DataRowView drv = o as DataRowView;
      return drv.Row.GetParentRow("DeptEmp")["NAME"].ToString();
    }
	}
}
