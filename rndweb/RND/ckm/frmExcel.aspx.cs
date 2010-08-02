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
using OWC;

namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmExcel.
	/// </summary>
    public class frmExcel : System.Web.UI.Page
    {
        protected string excelHtml;
        private void Page_Load(object sender, System.EventArgs e)
        {
            // Put user code to initialize the page here             
            excelHtml = CDSAdomd.GetExcelHtml(CDSAdomd.GetCellSet("Provider=MSOLAP; Datasource=localhost; Initial Catalog=PsiMedicaTestCubes;","SELECT {[Measures].[Episodes], [Measures].[Payment], [Measures].[Payment per Episode]} ON COLUMNS, {[Primary Diagnosis].[All Primary Diagnosis]} ON ROWS FROM VCEpisodes"));
            OWC.Spreadsheet s = new SpreadsheetClass();
            s.HTMLData = CDSAdomd.GetExcelHtml(CDSAdomd.GetCellSet("Provider=MSOLAP; Datasource=localhost; Initial Catalog=PsiMedicaTestCubes;","SELECT {[Measures].[Episodes], [Measures].[Payment], [Measures].[Payment per Episode]} ON COLUMNS, {[Primary Diagnosis].[All Primary Diagnosis]} ON ROWS FROM VCEpisodes"));            
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
  public class CDSAdomd
  {
    public static CellsetClass GetCellSet(string ASConnStr,string MDX)
    {
      ConnectionClass conn=null;      
      try
      {
        conn = new ConnectionClass();
        CellsetClass cst = new CellsetClass();
        cst.ActiveConnection=conn;
        conn.Open(ASConnStr,"","",(int)ConnectModeEnum.adModeUnknown);
        cst.Open(MDX,conn);
        return cst;
      }
      catch{return null;}
    }
    
    public static string GetExcelHtml(Cellset cellSet)
    {
      StringBuilder strBuilder = new StringBuilder();
      ArrayList aryRows = new ArrayList();
      string csw;
      //************************************************************************************
      //*** Set Dimension Counts minus 1 for Both Axes to intDC0, intDC1
      //*** Set Position Counts minus 1 for Both Axes to intPC0, intPC1
      //************************************************************************************
      int intDC0 = cellSet.Axes[0].DimensionCount-1;
      int intDC1 = cellSet.Axes[1].DimensionCount-1;

      int intPC0 = cellSet.Axes[0].Positions.Count - 1;
      int intPC1 = cellSet.Axes[1].Positions.Count - 1;
					
      //************************************************************************************
      //*** Create HTML Table structure to hold MDX Query return Record set
      //************************************************************************************     
      strBuilder.Append("<Table width=100% border=1  bordercolor=#CCCCCC bordercolordark=#CCCCCC bordercolorlight=#CCCCCC cellspacing=1>");
					
      //************************************************************************************
      //*** Loop to create Column header for all Dimensions based
      //*** on Count of Dimensions for Axes[0]
      //************************************************************************************
      for(int h=0; h <= intDC0; h++)
      {
        strBuilder.Append("<TR  bgcolor=#FFFFFF>");

        //************************************************************************************
        //*** Loop to create spaces in front of Column headers
        //*** to align with Row headers
        //************************************************************************************
        for(int c=0; c <= intDC1; c++)
        {
          strBuilder.Append("<TD  bgcolor=#FFFFFF></TD>");
        }

        //************************************************************************************
        //*** Check current dimension to see if equal to Last Dimension
        //*** If True: Write Table header titles normally to HTML output with out ColSpan value 
        //*** If False: Write Table header titles with ColSpan values to HTML output
        //************************************************************************************
        if( h == intDC0)
        {

          //************************************************************************************
          //*** Iterate through Axes[0] Positions writing member captions to table header
          //************************************************************************************
          for(int i = 0; i <= intPC0; i++)
          {
            strBuilder.Append("<TH style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\">");
            //strBuilder.Append("<TH  bgcolor=#FFFFFF>");
            strBuilder.Append("<span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;");
            strBuilder.Append(cellSet.Axes[0].Positions[i].Members[h].Caption);
            strBuilder.Append("</span>");
            strBuilder.Append("</TH>");
          }
        }
        else
        {			
          //************************************************************************************
          //*** Iterate through Axes[0] Positions writing member captions to table header
          //*** taking into account for the span of columns for duplicate member captions
          //************************************************************************************
          int CaptionCount = 1;
          string LastCaption = cellSet.Axes[0].Positions[0].Members[h].Caption;
          strBuilder.Append("<TH style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #FFFFFF\" ");
          for(int t=1; t<=intPC0; t++)
          {
				
            //************************************************************************************
            //*** Check to see if LastCaption is equal to current members caption
            //*** If True: Add one to CaptionCount to increase Colspan value
            //*** If False: Write Table header titles with ColSpan values to HTML output
            //*** using current CaptionCount for Colspan and LastCaption for header string
            //************************************************************************************
            if(LastCaption == cellSet.Axes[0].Positions[t].Members[h].Caption)
            {
              CaptionCount = CaptionCount+1;
						
              //************************************************************************************
              //*** Check if at last position
              //*** If True: Write HTML to finish table row using current
              //*** CaptionCount and LastCaption
              //************************************************************************************
              if(t == intPC0)
              {
                strBuilder.Append(" style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\" colspan=" + CaptionCount + "><span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;" + LastCaption + "</span></TH>");
              }
            }		
            else
            {
              strBuilder.Append(" style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\" colspan=" + CaptionCount + "><span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;" + LastCaption + "</span></TH><TH ");
              CaptionCount=1;
              LastCaption=cellSet.Axes[0].Positions[t].Members[h].Caption;
            }
          }
        }
        strBuilder.Append("</TR>");
      }
				
      //************************************************************************************
      //*** Iterate through Axes[1] Positions first writing member captions 
      //*** to table row headers then writing cell set data to table structure
      //************************************************************************************
      int intArray=0;

      //************************************************************************************
      //*** Set value of Array for row header formatting
      //************************************************************************************
      for(int a=1; a <= intDC1; a++)
      {
        intArray = intArray+(intPC1+1);
      }
      intArray = intArray-1;
      //ReDim aryRows[intArray];
      int Marker=0;

      //************************************************************************************
      //*** Use Array values for row header formatting to provide
      //*** spaces under beginning row header titles
      //************************************************************************************
      for(int j = 0; j <= intPC1; j++)
      {
        int iCellRow = cellSet.Axes[1].Positions[j].Ordinal;
        strBuilder.Append("<TR  bgcolor=#FFFFFF>");
        for(int h=0; h <= intDC1; h++)
        {
          if( h==intDC1)
          {
            strBuilder.Append("<TD style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\"><B>");
            //strBuilder.Append("<TD   bgcolor=#FFFFFF><B>");
            strBuilder.Append("<span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;");
            strBuilder.Append(cellSet.Axes[1].Positions[j].Members[h].Caption);
            strBuilder.Append("</span>");
            strBuilder.Append("</B></TD>");
          }
          else
          {
            aryRows.Insert(Marker,cellSet.Axes[1].Positions[j].Members[h].Caption);
            if(Marker < intDC1)
            {
              strBuilder.Append("<TD style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\"><B>");
              //strBuilder.Append("<TD  bgcolor=#FFFFFF><B>");
              strBuilder.Append("<span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;");
              strBuilder.Append(cellSet.Axes[1].Positions[j].Members[h].Caption);
              strBuilder.Append("</span>");
              strBuilder.Append("</B></TD>");
              Marker = Marker + 1;
            }
            else
            {
              if(aryRows[Marker].ToString().Equals(aryRows[Marker - intDC1].ToString()))
              {
                strBuilder.Append("<TD  bgcolor=#FFFFFF>&nbsp;</TD>");
                Marker = Marker + 1;
              }
              else
              {
                strBuilder.Append("<TD style=\"BACKGROUND-COLOR: #4E86D9;COLOR: #ffffff\"><B>");
                //strBuilder.Append("<TD  bgcolor=#FFFFFF><B>");
                strBuilder.Append("<span style='FONT-SIZE:10px;FONT-FAMILY:verdana;'>&nbsp;");
                strBuilder.Append(cellSet.Axes[1].Positions[j].Members[h].Caption);
                strBuilder.Append("</span>");
                strBuilder.Append("</B></TD>");
                Marker = Marker + 1;
              }
            }
          }
        }
				
        //************************************************************************************
        //*** Alternates Cell background color
        //************************************************************************************
        if((j+1)%2 == 0)
        {
          //csw = "#cccccc";
          csw = "#eeffee";
        }
        else
        {
          //csw = "#ccffff";
          csw = "#eeeeee";
        }
        for(int k = 0; k <= intPC0; k++)
        {
          strBuilder.Append("<TD align=right bgcolor=");
          strBuilder.Append(csw);
          strBuilder.Append(">");
          strBuilder.Append("<span style='FONT-SIZE:10px;FONT-FAMILY:verdana;FONT-SIZE:10px;FONT-FAMILY:verdana;'>");
          int iCellCol = cellSet.Axes[0].Positions[k].Ordinal;          
          object[] coords = new object[] {iCellCol,iCellRow};
          ADOMD.Cell cell = cellSet.get_Item(ref coords);
          //************************************************************************************
          //*** FormattedValue property pulls data
          //************************************************************************************
          strBuilder.Append(cell.FormattedValue);
          strBuilder.Append("</span>");
          strBuilder.Append("</TD>");
        }
        strBuilder.Append("</TR>");
      }
      strBuilder.Append("</Table>");
      return strBuilder.ToString();
    }
  }
}
