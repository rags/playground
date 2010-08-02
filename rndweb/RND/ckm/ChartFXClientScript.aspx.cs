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
using SoftwareFX.ChartFX;
using SoftwareFX.ChartFX.Internet;
using SoftwareFX.ChartFX.Borders;
using SoftwareFX.ChartFX.Data;
using SoftwareFX.ChartFX.Internet.Server;
using SoftwareFX.ChartFX.Internet.Server.GalleryObj;

namespace RND.ckm
{
  /// <summary>
  /// Summary description for ChartFXClientScript.
  /// </summary>
  public class ChartFXClientScript : System.Web.UI.Page
  {
    protected string strChart;
    private void Page_Load(object sender, System.EventArgs e)
    {
      SoftwareFX.ChartFX.Internet.Server.Chart Chart1 = new SoftwareFX.ChartFX.Internet.Server.Chart(this);
      Chart1.Gallery = SoftwareFX.ChartFX.Gallery.Bar;
      Chart1.Chart3D = true;
    
      SoftwareFX.ChartFX.Internet.Server.TitleDockable title = Chart1.Titles[0];
      title.Alignment = System.Drawing.StringAlignment.Center;
      title.Font=new System.Drawing.Font("Times New Roman",12,System.Drawing.FontStyle.Bold);
      title.Text = "Place your mouse over a bar";
      title.TextColor = System.Drawing.Color.Black; 
    
      Chart1.BorderObject = new ImageBorder(ImageBorderType.Colonial);

      // Pass the data to ChartFX
      Chart1.OpenData(SoftwareFX.ChartFX.COD.Values, 2, 4);
      Chart1.Value[0, 0] = 70.00;
      Chart1.Value[1, 0] = 77.00;

      Chart1.Value[0, 1] = 53.34;
      Chart1.Value[1, 1] = 45;

      Chart1.Value[0, 2] = 57.95;
      Chart1.Value[1, 2] = 55.07;

      Chart1.Value[0, 3] = 28.96;
      Chart1.Value[1, 3] = 81.45;

      Chart1.Value[0, 4] = 30.19;
      Chart1.Value[1, 4] = 60.9;
      Chart1.CloseData(SoftwareFX.ChartFX.COD.Values);
    
      Chart1.Legend[0] = "Jan";
      Chart1.Legend[1] = "Feb";
      Chart1.Legend[2] = "Mar";
      Chart1.Legend[3] = "Apr";
      Chart1.Legend[4] = "May";
    
      // Please be aware that the 4th parameter of GetHTMLTag is needed for client events.
      // also note that MainClient should be set to false
      Chart1.MainClient = false;
      Chart1.ToolBar = true;
      Chart1.ToolBarObj[0] = (int) CommandID.ExportFile;
      strChart = Chart1.GetHtmlTag(500,350,".Net","Chartfx1");
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
