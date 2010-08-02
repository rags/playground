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
//using SoftwareFX.ChartFX.Borders;
using SoftwareFX.ChartFX.Olap.Server;
//using SoftwareFX.ChartFX.CategBar.Server;
using SoftwareFX.ChartFX.Internet.Server;
using System.Text;
 

namespace RND
{
	/// <summary>
	/// Summary description for frmChart.
	/// </summary>
	public class frmChart1: System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.TextBox txtQuery;
    protected System.Web.UI.WebControls.Button btnShow;

    protected string outstr;
    
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      Chart Chart1 = new Chart();
      Chart1.Import(FileFormat.BinaryTemplate,@"c:\xxx.xml");
      if(IsPostBack)
      {
        Chart1.Palette=Chart1.Palette;
        return;
      }
      btnShow.Attributes.Add("onclick","x()");
      string query = txtQuery.Text;
      if(String.Empty.Equals(query))
      {
        query=txtQuery.Text="select filter({{[Measures].[Ta Units]},{[Measures].[Ta Wrkload]}},[Measures].[Ta Amount]>1000000 and [Measures].[Ta Units]>5000 ) on rows," +
                                              "{filter(toggledrillstate({[AgeRange].[All AgeRange]},{[AgeRange].[All AgeRange]}),[Measures].[Ta Amount]>1000000 and [Measures].[Ta Units]>5000)} on columns" +
                                              " from [Claims cube]";
      }      
      //Chart1.ClearData(SoftwareFX.ChartFX.ClearDataFlag.AllData);
      SoftwareFX.ChartFX.Olap.Server.OlapExtension Olap1=new SoftwareFX.ChartFX.Olap.Server.OlapExtension();
      SoftwareFX.ChartFX.Olap.Server.AdoMultiDimensionalData AdoMD1=new SoftwareFX.ChartFX.Olap.Server.AdoMultiDimensionalData();
      try
      {
        AdoMD1.Connect("Provider=MSOLAP; Datasource=localhost; Initial Catalog=FoodMart 2000;", query);
        Olap1.DataSource = AdoMD1;			                
        Chart1.Extensions.Clear();
        Chart1.Extensions.Add(Olap1);        
        Chart1.PersonalizedFlags=SoftwareFX.ChartFX.PersonalizedFlags.AutoLoad;// & SoftwareFX.ChartFX.PersonalizedFlags.AutoSave;
      }
      catch
      {
        ;
      }
      Chart1.Palette="Default.ModernBusiness";
      outstr = Chart1.GetHtmlTag(400,400,".NET","Chart1");
      Chart1.Export(FileFormat.Jpeg,@"c:\xxx.jpg");

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

    private void Chart1_Personalized(object sender, SoftwareFX.ChartFX.Internet.Server.PersonalizedEventArgs e)
    {
      
    }
	}
}
