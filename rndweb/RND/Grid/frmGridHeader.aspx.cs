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

namespace RND.Grid
{
	/// <summary>
	/// Summary description for frmGridHeader.
	/// </summary>
	public class frmGridHeader : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.DataGrid grid;
    
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
            DataTable table = new DataTable();
            table.Columns.Add("col1");
            table.Columns.Add("col2");
            table.Columns.Add("col3");
            table.Columns.Add("col4");
            //table.Rows.Add(new object[] {"a","b","c","d"});
            grid.DataSource = table;
            grid.DataBind();
            DataGridItem footer = GetFooter(grid);
		}
        private DataGridItem GetFooter(DataGrid grid)
        {
            Control table = grid.Controls[0];
            DataGridItem footer = table.Controls[table.Controls.Count-1] as DataGridItem;
            if(footer.ItemType==ListItemType.Footer) return footer;
            return null;
        }
        public void created(object sender ,DataGridItemEventArgs  e)
        {        
            if(e.Item.ItemType == ListItemType.Footer &&  grid.Items.Count==0) 
            {                
                Control /*DataGridTable*/ table = grid.Controls[0];
                DataGridItem  tr = new DataGridItem(0,0,ListItemType.Item);
                TableCell  td = new TableCell();
                td.ColumnSpan = table.Controls[0].Controls.Count;//no of cols on header
                td.Text = "No records";
                td.HorizontalAlign = HorizontalAlign.Center; 
                tr.Controls.Add(td);
                table.Controls.Add(tr);//controls[0]=table
            } 
        }

        public void bound(object sender ,DataGridItemEventArgs  e)
        {        
            //if(e.Item.ItemType == ListItemType.Footer) {x = grid.Items.Count; }
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
