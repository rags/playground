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
using Microsoft.AnalysisServices.AdomdClient;
using System.Configuration;
using System.Text;
using System.Text.RegularExpressions;

namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmADOMD_NET.
	/// </summary>
	public class frmADOMD_NET : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.DataGrid DataGrid1;    
		private void Page_Load(object sender, System.EventArgs e)
		{
			AdomdConnection conn = new AdomdConnection(ConfigurationSettings.AppSettings["adomdConn"]);            
            conn.Open();
            AdomdCommand comm = new AdomdCommand(@"SELECT  {{[Age Range_Member].[Age Range].Members}*{[Gender_Employee].[Gender_Employee].Members}} on rows, {{[Measures].[Member Months],[Measures].[Allowed]} * {[Benefit Plan].[Benefit Plan Type].Members}} on columns from [RCBigMainCube]",conn);
            CellSet cst = comm.ExecuteCellSet();
            CubeDef def = conn.Cubes["RCBigMainCube"];            
            conn.Close();
            Dimension dim = def.Dimensions["Age Range_Member"];
            StringBuilder str = new StringBuilder(),
                                   strTmp = new StringBuilder();
            int axisRow = 1,axisCol = 0;
            int i,j,k; // indexers
            string tmpPrev,tmpCur;//temp string to hjold previous and current value
            HierarchyCollection rowHierarchy = cst.Axes[axisRow].Set.Hierarchies,
                                               colHierarchy = cst.Axes[axisCol].Set.Hierarchies;
            TupleCollection rowTuples = cst.Axes[axisRow].Set.Tuples,
                                       colTuples =  cst.Axes[axisCol].Set.Tuples;
            int rowHierCnt = rowHierarchy.Count,
                  colHierCnt = colHierarchy.Count,
                  rowTuplCnt = colTuples.Count,
                  colTuplCnt = colTuples.Count;
            
            str.Append("<table class=\"tableStyle\" cellspacing=\"0\">");

            /********************************************Write the column header*************************************************/
            /***************Write col dimensions*****************/
                    str.Append("<tr nowrap class=\"trStyle\">");
                    for(j=0;j<rowHierCnt;j++)  str.Append("<td nowrap class=\"tdStyle\">&nbsp;</td>");                    
                    for(j=0;j<colHierCnt;j++)
                    {
                        string dimName = colHierarchy[j].UniqueName;
                        str.Append("<td nowrap class=\"thStyle\"><b>");
                        if("Measures".Equals(dimName))
                            str.Append(dimName);
                        else 
                            str.Append(Regex.Match(colTuples[0].Members[j].LevelName,@"(?<=\]\.\[)[^\]]+(?=\]$)").Value);
                        str.Append("</b></td>");                    
                    }
                    str.Append("</tr>");
            /***************Write col dimensions*****************/
            for(i=0;i<colHierCnt;i++)
            {            
                str.Append("<tr nowrap class=\"trStyle\">");
                for(j=0;j<rowHierCnt;j++)   str.Append("<td nowrap class=\"tdStyle\">&nbsp;</td>");
                tmpPrev = string.Empty;                
                for(k=0;k<colTuplCnt;k++)
                {
                    tmpCur =  colTuples[k].Members[i].Caption;
                    if(tmpPrev.Equals(tmpCur)) tmpCur = "&nbsp;";   
                    else tmpPrev = tmpCur;
                    strTmp.Append("<td nowrap class=\"thStyle\"><b>");
                    strTmp.Append(tmpCur);
                    strTmp.Append("</b></td>");                    
                }
            
                str.Append("</tr>");
            }
            str.Append(strTmp.ToString());
            /********************************************End of write the column header*************************************************/
            for(i=0;i<rowTuplCnt;i++)
            {
                str.Append("<tr nowrap class=\"trStyle\">");
                tmpPrev = string.Empty;
                for(j=0;j<rowHierCnt;j++)
                {
                    tmpCur =  rowTuples[i].Members[j].Caption;
                    if(tmpPrev.Equals(tmpCur)) tmpCur = "&nbsp;";   
                    else tmpPrev = tmpCur;
                    str.Append("<td nowrap class=\"thStyle\"><b>");
                    str.Append(tmpCur);
                    str.Append("</b></td>");                    
                }
                for(k=0; k<colTuplCnt;k++)
                {
                    tmpCur = cst.Cells[k,i].FormattedValue;
                    str.Append("<td nowrap class=\"tdStyle\">");
                    str.Append((tmpCur.Length == 0)?"&nbsp;" : tmpCur);
                    str.Append("</td>");
                }
                str.Append("</tr>");
            }
            str.Append("<table/>");
            Response.Write(str.ToString());
//            conn.Close();
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
