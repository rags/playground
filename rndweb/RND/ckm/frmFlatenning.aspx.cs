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
using ADODB;
using ADOMD;
using System.Text;


namespace RND
{
	/// <summary>
	/// Summary description for frmFlatenning.
	/// </summary>
	public class frmFlatenning : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.TextBox txtQuery;
    protected System.Web.UI.WebControls.Button btnShow;
    protected System.Web.UI.WebControls.TextBox txtServer;
    protected System.Web.UI.WebControls.TextBox txtCatalog;
    public StringBuilder strView;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
      string query = txtQuery.Text;
      strView = new StringBuilder();
      if(String.Empty.Equals(query))
      {
//        query=txtQuery.Text="SELECT {{[Store].[All Stores],[Store].[All Stores].[USA],[Store].[All Stores].[USA].[CA],[Store].[All Stores].[USA].[OR],[Store].[All Stores].[USA].[WA]}*{[Gender].[All Gender].[F],[Gender].[All Gender].[M]}*{[Marital Status].[All Marital Status].[M],[Marital Status].[All Marital Status].[S]}*{[Product].[All Products].[Drink],[Product].[All Products].[Food],[Product].[All Products].[Non-Consumable]}} ON ROWS, " +
//          "{{[Measures].[Unit Sales],[Measures].[Store Cost],[Measures].[Store Sales],[Measures].[Sales Count],[Measures].[Store Sales Net],[Measures].[Profit],[Measures].[Sales Average]}*{[Education Level].[All Education Level].[Bachelors Degree],[Education Level].[All Education Level].[Graduate Degree],[Education Level].[All Education Level].[High School Degree],[Education Level].[All Education Level].[Partial College],[Education Level].[All Education Level].[Partial High School]}*{[Time].[1997].[Q1],[Time].[1997].[Q2],[Time].[1997].[Q3],[Time].[1997].[Q4]}} ON COLUMNS " +
//          "FROM [Sales]";
        return;
      }
      ConnectionClass conn = new ConnectionClass();
      conn.Open("Provider=MSOLAP; Datasource="+txtServer.Text +"; Initial Catalog="+txtCatalog.Text +";","",string.Empty,(int)ADODB.ConnectOptionEnum.adConnectUnspecified);
      CellsetClass cs = new CellsetClass();
      cs.Open(query,conn);
    
      strView.Append("<table border=1>");
      
      Axis axisX= cs.Axes[0];
      int dimCountX=axisX.DimensionCount;
      int posCountX=axisX.Positions.Count;
      Positions posX = axisX.Positions;
 
      Axis axisY= cs.Axes[1];
      int dimCountY=axisY.DimensionCount;
      int posCountY=axisY.Positions.Count;
      Positions posY = axisY.Positions;

      for(int i=0;i<dimCountX;i++)
      {
        strView.Append("<tr>");
        strView.Append("<th colspan="+dimCountY+">&nbsp;</th>");
        string lastCaption=posX[0].Members[i].Caption;
        int colspan=1;
        for(int j=1;j<posCountX;j++ )
        {
          Position pos = posX[j];
          if(lastCaption.Equals(pos.Members[i].Caption)) 
          {            
            colspan++;            
          }
          else
          {
            strView.Append("<th colspan="+colspan+">" +posX[j-1].Members[i].Caption + "</th>");
            colspan=1;
            lastCaption=pos.Members[i].Caption;
          }
          if(j==posCountX-1) strView.Append("<th colspan="+colspan+">" +pos.Members[i].Caption + "</th>");
        }
        strView.Append("</tr>");
      }


      string[]  lastCaptions = new string[dimCountY];            
      
      for(int j=0;j<posCountY;j++ )
      {
        Position  pos=posY[j];
        strView.Append("<tr>");
        for(int i=0;i<dimCountY;i++)
        {   
          if(pos.Members[i].Caption.Equals(lastCaptions[i])) 
          {
            strView.Append("<th>&nbsp;</th>");
            continue;            
          }          
          strView.Append("<th >" +pos.Members[i].Caption +   "</th>" );                                        
          lastCaptions[i]=pos.Members[i].Caption ;
        }
        for(int k=0;k<posCountX;k++)
        {
          object[] coords=new object[]{k,j};
          Cell cell = cs.get_Item(ref coords);
          strView.Append("<td>"+cell.FormattedValue +  "</td>");
        }
        strView.Append("</tr>");
      }
            
      strView.Append("</table>");
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
