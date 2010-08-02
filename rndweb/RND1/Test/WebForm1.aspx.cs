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

namespace InternalCommand_Client
{
	/// <summary>
	/// Summary description for WebForm1.
	/// </summary>
	public class WebForm1 : System.Web.UI.Page
	{
		protected SoftwareFX.ChartFX.Internet.Server.Chart Chart1;
		SoftwareFX.ChartFX.Olap.Server.OlapExtension Olap1;
		SoftwareFX.ChartFX.Olap.Server.AdoMultiDimensionalData AdoMD1;
		string mdx;
		string connStr;
	
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here

		
			connStr = "Provider=msolap; Data Source=ntech32; Initial Catalog=FoodMart 2000;";
			
			//mdx = "with member [Measures].[Total Store Sales] as 'Sum(YTD(),[Measures].[Store Sales])'select ";
			//mdx += "{[Measures].[Total Store Sales]} on columns, {TopCount([Product].[Product Department].members,5, [Measures].[Total Store Sales])} on rows ";
			//mdx += "from Sales where ([Time].[1997].[Q2].[4])";
      

        mdx = "select filter({{[Measures].[Ta Units]},{[Measures].[Ta wrkload]}},[Measures].[Ta Amount]>0 ";
        mdx  += " and [Measures].[Ta Units]>0 ) on rows, ";
        mdx  += "{filter(toggledrillstate({[AgeRange].[All AgeRange]}, ";
        mdx  += "{[AgeRange].[All AgeRange]}),[Measures].[Ta Amount]>1000000 and [Measures].[Ta Units]>5000)} on columns ";
        mdx  += " from [Claims cube]";

			Olap1 = new SoftwareFX.ChartFX.Olap.Server.OlapExtension();
			AdoMD1 = new SoftwareFX.ChartFX.Olap.Server.AdoMultiDimensionalData();
			AdoMD1.Connect(connStr, mdx);
			Olap1.DataSource = AdoMD1;
			
			Chart1.Extensions.Add(Olap1);
			
			//Must set MainClinet to False to use client events
			Chart1.MainClient = false;
			
			
			Chart1.HtmlTag = ".NET";
			Chart1.ToolBar = true;


			
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
