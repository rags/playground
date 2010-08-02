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

namespace RND
{  
  /// <summary>
  /// Summary description for frmGrid.
  /// </summary>
  public class frmGrid : System.Web.UI.Page 
  {
    protected System.Web.UI.WebControls.Button btnAdd;
    protected System.Web.UI.WebControls.Button btnDelete;
    protected System.Web.UI.WebControls.DataGrid DataGrid1;
    
    private void Page_Load(object sender, System.EventArgs e)
    {
      // Put user code to initialize the page here
      if(!IsPostBack)
      {
        bind();
      }
        if(DataGrid1.EditItemIndex>-1)
        {
            DataGridItem item =  DataGrid1.Items[0];//[DataGrid1.EditItemIndex];
            TextBox emailBox = item.Controls[3].Controls[0] as TextBox;
            CustomValidator val = new CustomValidator();
            val.ControlToValidate = emailBox.ID;      
            val.ServerValidate += new ServerValidateEventHandler(ValidateEmail);
            //val.Validate(); 
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
      btnDelete.Click+=new System.EventHandler(btnDelete_Click);
      btnAdd.Click+=new System.EventHandler(btnAdd_Click);
    }
		#endregion
    
    public void bind()
    {
      SqlConnection con = new SqlConnection(ConfigurationSettings.AppSettings["connectionString"]);
      SqlDataAdapter da = new SqlDataAdapter("Select * from Customers",con);
      DataTable dt = new DataTable("Customers");
      da.Fill(dt);
      if(DataGrid1.Attributes["SortOn"]!=null) dt.DefaultView.Sort=DataGrid1.Attributes["SortOn"];
      BoundColumn col = new BoundColumn();
      col.ReadOnly=true;
      col.HeaderText="SL NO.";
      DataGrid1.Columns.AddAt(0,col);        
      TemplateColumn col1 = new TemplateColumn();
      col1.ItemTemplate =LoadTemplate("ItemTemplate.ascx");
      col1.HeaderText="template - from ascx";
      DataGrid1.Columns.Add(col1);
      //E.Item.Cells[0].Text= E.Item.DataSetIndex + 1; 
      //http://www.dotnetbips.com/displayarticle.aspx?id=84
      //http://www.dotnetbips.com/displayarticle.aspx?id=85
      TemplateColumn col2 = new TemplateColumn();
      col2.HeaderText  = "template - from code";
      col2.ItemTemplate = new CTemplateColumn("Customer_Name");
      DataGrid1.Columns.Add(col2);      
      DataGrid1.DataSource=dt.DefaultView;
      //next 2 lines to check if the pageindex is greater than noof pages when records are deleted from DB
      double actualPageCount = Math.Ceiling(dt.Rows.Count / (double)DataGrid1.PageSize);
      if(DataGrid1.CurrentPageIndex>=actualPageCount) DataGrid1.CurrentPageIndex =(int)actualPageCount - 1;
      DataGrid1.DataBind(); 
    }
    
    public void Edit(Object sender, DataGridCommandEventArgs e) 
    {
      DataGrid1.EditItemIndex = (int)e.Item.ItemIndex;      
      bind();
      try
      {
        DataGridItem item =  DataGrid1.Items[e.Item.ItemIndex];        
        TextBox emailBox = item.Controls[3].Controls[0] as TextBox;
        CustomValidator val = new CustomValidator();
        val.ControlToValidate = emailBox.ID;
        val.ClientValidationFunction="validateEmail";
//        val.ServerValidate += new ServerValidateEventHandler(ValidateEmail);
        item.Controls[3].Controls.Add(val);
        LinkButton updateLnk = item.Controls[5].Controls[0] as LinkButton;
        //updateLnk.CausesValidation=false;
      }
      catch{}
    }
    
    public void ValidateEmail(object sender,ServerValidateEventArgs args)
    {
        string x = args.Value;
        if(x.Length>0) args.IsValid = true;
        else args.IsValid=false;
        Response.Write("Server validation");
    }

    public void Cancel (object sender,DataGridCommandEventArgs e)
    {
      DataGrid1.EditItemIndex=-1;
      bind();
    }
    
    public void Sort(object sender,DataGridSortCommandEventArgs  e)
    {
      DataGrid1.Attributes.Add("SortOn", e.SortExpression); //STORE THE SORT EXPRESSION SOMEWHERE like Session,viewstate,attr of grid
      DataGrid1.EditItemIndex=-1;
      bind();
    }

    public void Delete(object sender,DataGridCommandEventArgs e)
    {
      string key = DataGrid1.DataKeys[e.Item.ItemIndex].ToString() ;            
      DeleteRecord(key);
      bind();      
    }
    
    public void PageChange(object sender,DataGridPageChangedEventArgs e)
    {
      DataGrid1.CurrentPageIndex=e.NewPageIndex;
      DataGrid1.EditItemIndex=-1;
      bind();               
    }
    
    public void ChangeHeader(object sender ,DataGridItemEventArgs  e)
    {
      DataGridItem item = e.Item;
      if(item.ItemType==ListItemType.Header)
      {
        TableRow header = (TableRow)item;   //header row    
        header.Cells[0].Text += header.Cells[0].Text + ":)"; //modify 1st column header
      }
      if(item.ItemType==ListItemType.Footer)
      {
        TableCell  footer = (TableCell)item.Controls[0];
        footer.Text="This is footer";
      }
      if(item.ItemType == ListItemType.Item || item.ItemType == ListItemType.AlternatingItem)
      {
        item.Cells[0].Text= (item.DataSetIndex + 1).ToString(); 
      }      
    }
  
  public void CustomizePager(object sender ,DataGridItemEventArgs  e)
  {   
    DataGridItem item = e.Item;
     //cantt do it here. can set a heading but not modify it. i.e here o/p will be heading=:) and not heading +=:)
//     if(item.ItemType==ListItemType.Header)
//     {
//       TableRow header = (TableRow)item;   //header row    
//       header.Cells[0].Text += header.Cells[0].Text + ":)"; //modify 1st column header
//     }
//     if(item.ItemType==ListItemType.Footer)
//     {
//       TableCell  footer = (TableCell)item.Controls[0];
//       footer.Text="This is footer";
//     }
     if(item.ItemType!=ListItemType.Pager) return;
     TableCell pager = (TableCell)item.Controls[0];//pager is tr; pager.control[0] is a td in which page nos are populated      
     for (int i = 0; i < pager.Controls.Count; i ++)//loop thru all the elements in pager
     {
       Control pagerItem = pager.Controls[i];
       //Note: every odd item is an &nbsp; ;even items hold page nos ..... current page no is a label and other are link buttons
       if(i%2!=0) 
       {
         LiteralControl spacer = pagerItem as LiteralControl;
         spacer.Text += "<span style='color: #cccccc'>|</span>&nbsp;";
         continue;
       }       
       if (pagerItem is LinkButton)
       {
         LinkButton btnOtherPageNo = (LinkButton)pagerItem;
         btnOtherPageNo.ForeColor=Color.CornflowerBlue;         
         btnOtherPageNo.Style["TEXT-DECORATION"]="none";
       }
       else
       {
         Label curPageNo = (Label)pagerItem;         
         curPageNo.ForeColor=Color.Crimson; 
       }
     }
  }
    private void  getPager(Control control,ArrayList arr)
    {        
      foreach(Control ctrl in control.Controls  )
      {
        DataGridItem  item = ctrl  as DataGridItem;
        if(item!=null && item.ItemType==ListItemType.Pager) 
        {
          arr.Add(item);
        }                  
        getPager(ctrl,arr);        
      }      
    }
  
    public void Update(object sender,DataGridCommandEventArgs e)
    {
      DataTable dt = new DataTable("Customers");      
      SqlDataAdapter da = new SqlDataAdapter("Select * from Customers",ConfigurationSettings.AppSettings["connectionString"]);
      new SqlCommandBuilder().DataAdapter=da;        
      da.Fill(dt);
      int index = e.Item.ItemIndex + DataGrid1.CurrentPageIndex * DataGrid1.PageSize;
      DataRow dr = dt.Rows[index];
      dr["Logo_Path"]=((TextBox)e.Item.Cells[1].Controls[0]).Text;
      dr["URL"]=((TextBox)e.Item.Cells[2].Controls[0]).Text;
      dr["Record_Status"]=((TextBox)e.Item.Cells[3].Controls[0]).Text;          
      da.Update(new DataRow[] {dr});            
      dt.AcceptChanges();
      DataGrid1.EditItemIndex=-1;
      if(DataGrid1.Attributes["SortOn"]!=null) dt.DefaultView.Sort=DataGrid1.Attributes["SortOn"];
      DataGrid1.DataSource=dt.DefaultView;
      DataGrid1.DataBind();       
      da.Dispose();
      dt.Dispose();        
    }

    private void btnAdd_Click(object sender, System.EventArgs e)
    {
      SqlCommand com= new SqlCommand("insert into Customers (Customer_name,Logo_Path,URL) values('"+Request.Form["txtCustomer"]+"','"+Request.Form["txtLogo"]+"','"+Request.Form["txtURL"]+"')" ,new SqlConnection( ConfigurationSettings.AppSettings["connectionString"]));
      com.Connection.Open();
      com.ExecuteNonQuery();
      bind();
    }

    private void btnDelete_Click(object sender, System.EventArgs e)
    {      
      string [] idsToDelete = Request.Form["gridChkBox"].Split(new char[] {','});
      foreach(string id in idsToDelete) DeleteRecord(id);
      bind();
    }

    private void DeleteRecord(string intRecordID)
    {
      SqlCommand com= new SqlCommand("Delete from Customers where Customer_Number=" +intRecordID,new SqlConnection( ConfigurationSettings.AppSettings["connectionString"]));
      com.Connection.Open();
      com.ExecuteNonQuery();      
    }
  }

  public class CTemplateColumn:ITemplate
  {
    private string colname;

    public CTemplateColumn(string cname)
    {
      colname=cname;
    }

    //must implement following method
    public void InstantiateIn(Control container)
    {
      LiteralControl l = new LiteralControl();
      l.DataBinding += 
        new EventHandler(this.OnDataBinding);
      container.Controls.Add(l);
    }

    public void OnDataBinding(object sender, EventArgs e)
    {
      LiteralControl l = (LiteralControl) sender;
      DataGridItem container = 
        (DataGridItem) l.NamingContainer;
      l.Text = 
        ((DataRowView)
        container.DataItem)[colname].ToString();
    }
  }

}