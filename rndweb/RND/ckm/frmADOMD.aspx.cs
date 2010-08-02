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


namespace RND
{
	/// <summary>
	/// Summary description for frmADoMD.
	/// </summary>
	public class frmADoMD : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      string query = "SELECT {{[Store].[All Stores],[Store].[All Stores].[USA],[Store].[All Stores].[USA].[CA],[Store].[All Stores].[USA].[OR],[Store].[All Stores].[USA].[WA]}*{[Gender].[All Gender].[F],[Gender].[All Gender].[M]}*{[Marital Status].[All Marital Status].[M],[Marital Status].[All Marital Status].[S]}*{[Product].[All Products].[Drink],[Product].[All Products].[Food],[Product].[All Products].[Non-Consumable]}} ON ROWS, " +
                              "{{[Measures].[Unit Sales],[Measures].[Store Cost],[Measures].[Store Sales],[Measures].[Sales Count],[Measures].[Store Sales Net],[Measures].[Profit],[Measures].[Sales Average]}*{[Education Level].[All Education Level].[Bachelors Degree],[Education Level].[All Education Level].[Graduate Degree],[Education Level].[All Education Level].[High School Degree],[Education Level].[All Education Level].[Partial College],[Education Level].[All Education Level].[Partial High School]}*{[Time].[1997].[Q1],[Time].[1997].[Q2],[Time].[1997].[Q3],[Time].[1997].[Q4]}} ON COLUMNS " +
                              "FROM [Sales]";
      ConnectionClass conn = new ConnectionClass();
      conn.Open("Provider=MSOLAP; Datasource=localhost; Initial Catalog=FoodMart 2000;","",string.Empty,(int)ADODB.ConnectOptionEnum.adConnectUnspecified);
      CellsetClass cs = new CellsetClass();
      cs.Open(query,conn);
      Response.Write("<table border=1>");
      for(int i=0;i<cs.Axes[0].DimensionCount;i++)
      {
        Response.Write("<tr>");
        for(int j=0;j<cs.Axes[1].DimensionCount;j++) Response.Write("<th>&nbsp;</th>");
        //string lastCaption= string.Empty;//cs.Axes[0].Positions[0].Members[i].Caption;
        int colspan=1;
        for(int j=0;j<cs.Axes[0].Positions.Count;j++ )
        {
          Position pos = cs.Axes[0].Positions[j];
//          if(lastCaption.Equals(pos.Members[i].Caption)) 
//          {
//            Response.Write("<th>&nbsp;</th>");
//            //colspan++;            
//          }
//          else
//          {
            //Response.Write("<th colspan="+colspan+">" +cs.Axes[0].Positions[j-1].Members[i].Caption + "</th>");
            //colspan=1;
            Response.Write("<th colspan="+colspan+">" +cs.Axes[0].Positions[j].Members[i].Caption + "</th>");
//            lastCaption=pos.Members[i].Caption;
//          }
          //if(j==cs.Axes[0].Positions.Count-1) Response.Write("<th colspan="+colspan+">" +cs.Axes[0].Positions[j].Members[i].Caption + "</th>");
        }
        Response.Write("</tr>");
      }
//      string[]  lastCaptions = new string[cs.Axes[1].DimensionCount];
      for(int j=0;j<cs.Axes[1].Positions.Count;j++)
      {
        Position pos = cs.Axes[1].Positions[j];
        Response.Write("<tr>");
        for(int i=0;i<cs.Axes[1].DimensionCount;i++)
        {   
//          if(pos.Members[i].Caption.Equals(lastCaptions[i])) 
//          {
//            Response.Write("<th>&nbsp;</th>");
//            continue;
//          }
          Response.Write("<th>" +pos.Members[i].Caption +   "</th>" );                    
//          lastCaptions[i]=pos.Members[i].Caption ;
        }
        for(int k=0;k<cs.Axes[0].Positions.Count;k++)
        {
          object[] coords=new object[]{k,j};
          Cell cell = cs.get_Item(ref coords);
          Response.Write("<td>"+cell.FormattedValue +  "</td>");
        }
        Response.Write("</tr>");
      }
            
      Response.Write("</table>");
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
