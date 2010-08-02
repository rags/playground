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
using System.Text;
 

namespace RND
{
	/// <summary>
	/// Summary description for frmChart.
	/// </summary>
	public class frmChart : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.TextBox txtQuery;
    protected SoftwareFX.ChartFX.Internet.Server.Chart Chart1;
    protected System.Web.UI.WebControls.Button btnShow;
    
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      //if(IsPostBack) return;
      Response.Write("CurDir: " +Server.MapPath("/ChartFX6"));
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
        Chart1.MainClient = false;        
        //Chart1.Gallery= SoftwareFX.ChartFX.Gallery.Surface;
      //  Chart1.Palette =
//"Default.Alternate";
// "Default.ChartFX6";
// "Default.EarthTones";
// "Default.ModernBusiness";
// "Default.Windows";
// "DarkPastels.Pastels";
// "DarkPastels.AltPastels";
// "HighContrast.HighContrast";
//"ChartFX5.ChartFX5";


//        Chart1.ToolBar = true;
        //Chart1.PersonalizedFlags=SoftwareFX.ChartFX.PersonalizedFlags.AutoLoad & SoftwareFX.ChartFX.PersonalizedFlags.AutoSave & SoftwareFX.ChartFX.PersonalizedFlags.EnableRestore;
      }
      catch
      {
        ;
      }
      //Chart1.Palette="Default.ModernBusiness";
      //Chart1.FileMask=SoftwareFX.ChartFX.FileMask.Template;
      Chart1.Export(SoftwareFX.ChartFX.Internet.Server.FileFormat.BinaryTemplate,@"c:\xxx.xml");
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
