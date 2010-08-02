using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Web;
using System.Web.Services;
using ADOMD;
using ADODB;
using System.Xml;
using System.Xml.Xsl;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;

namespace RND.WebService
{
	/// <summary>
	/// Summary description for cwsTree.
	/// </summary>
	public class cwsTree : System.Web.Services.WebService
	{
		public cwsTree()
		{
			//CODEGEN: This call is required by the ASP.NET Web Services Designer
			InitializeComponent();
		}

		#region Component Designer generated code
		
		//Required by the Web Services Designer 
		private IContainer components = null;
				
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if(disposing && components != null)
			{
				components.Dispose();
			}
			base.Dispose(disposing);		
		}
		
		#endregion
    [WebMethod]
    public string GetDimensions(string cubeName)
    {
      CubeDef cubeDef = GetCubeDef(cubeName);
      StringBuilder strDimBldr = new StringBuilder("<ContentMenu>");          
      for (int i=0; i<cubeDef.Dimensions.Count; i++) 
      {
        // Write out the field or level names.
        Dimension curDim = cubeDef.Dimensions[i];
        string sFolderCaption = "";        
        sFolderCaption = curDim.Name;
        if (curDim.Hierarchies[0].Name != "") sFolderCaption += "." + curDim.Hierarchies[0].Name;                  
        strDimBldr.Append("<MenuItem id=\"" + curDim.Hierarchies[0].UniqueName + "\"  type=\"dimension\" dimension=\"" + curDim.UniqueName + "\" name=\"" + sFolderCaption + "\" />");                          
      }
      strDimBldr.Append("</ContentMenu>");
      strDimBldr.Replace("&","&amp;");            
      return strDimBldr.ToString();
      //return doc.rer;
    }
    [WebMethod]
    public string GetLevels(string cubeName,string dimName)
    {
      CubeDef cubeDef = GetCubeDef(cubeName);
      Dimension curDim = cubeDef.Dimensions[dimName];
      Levels levels = curDim.Hierarchies[0].Levels;
      StringBuilder strDimBldr = new StringBuilder("<ContentMenu>");                
      for (int l=0;l<levels.Count; l++)
      {
        strDimBldr.Append("<MenuItem id=\"" + levels[l].UniqueName + "\"  type=\"level\" dimension=\"" + curDim.Hierarchies[0].UniqueName + "\" name=\"" + levels[l].Caption + "\" />");          
      }           
      strDimBldr.Append("</ContentMenu>");
      strDimBldr.Replace("&","&amp;");            
      return strDimBldr.ToString();
    }
    [WebMethod]
    public string GetMembers(string cubeName,string dimName,string levelName)
    {
      CubeDef cubeDef = GetCubeDef(cubeName);
      Dimension curDim = cubeDef.Dimensions[dimName];
      Members  members= curDim.Hierarchies[0].Levels[levelName].Members;      
      StringBuilder strDimBldr = new StringBuilder("<ContentMenu>");                
      for (int k=0;k<members.Count; k++)
      {        
        strDimBldr.Append("<MenuItem id=\"" + members[k].UniqueName + "\" type=\"member\" dimension=\"" + curDim.Hierarchies[0].UniqueName + "\" name=\"" + members[k].Caption + "\" hasChild=\""+((members[k].ChildCount==0)?"false":"true")+"\"/>");
      }
      strDimBldr.Append("</ContentMenu>");
      strDimBldr.Replace("&","&amp;");            
      return strDimBldr.ToString();
    }
    
    [WebMethod]
    public string GetChildren(string cubeName,string member)
    {
      Cellset cst = GetCellSet("Location=localhost;Initial Catalog=PsiMedicaCubes;Provider=MSOLAP;","SELECT  AddCalculatedMembers(" + member +".children)  on rows, {} on columns from [" +cubeName + "]");      
      StringBuilder strDimBldr = new StringBuilder("<ContentMenu>");                
      Axis row = cst.Axes[1];
      int loopMax = Math.Min(row.Positions.Count,5000);
      for (int i=0;i<loopMax;i++) 
      {
        Member  curMember = row.Positions[i].Members[0];
        string sLevelName = curMember.LevelName;        
        string DimName = "[" + sLevelName.Substring(1, (Regex.Match(sLevelName,@"].").Index)-1) + "]";        
        strDimBldr.Append("<MenuItem id=\"" + curMember.UniqueName + "\" type=\"member\" dimension=\"" + DimName + "\" name=\"" + curMember.Caption + "\" hasChild=\""+((curMember.ChildCount==0)?"false":"true")+"\" />");        
      }    
      strDimBldr.Append("</ContentMenu>");      
      strDimBldr.Replace("&","&amp;");            
      return strDimBldr.ToString();
    }
    
    public static CubeDef GetCubeDef(string cubeName)
    {
      ConnectionClass con = new ADODB.ConnectionClass();          
      con.Open("Location=localhost;Initial Catalog=PsiMedicaCubes;Provider=MSOLAP;",string.Empty,string.Empty,(int)ConnectModeEnum.adModeUnknown);
      CatalogClass cat = new ADOMD.CatalogClass();
      cat.ActiveConnection = con;      
      return cat.CubeDefs[cubeName];
    }
                
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
	}
}
