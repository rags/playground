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
using ADOMD;
using ADODB;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml;
using System.Xml.Xsl;
using System.IO;

namespace RND
{
  /// <summary>
  /// Summary description for DimMeaTree.
  /// </summary>
  public class DimMeaTree : System.Web.UI.Page
  {
    protected string outputHTML;
  
    private void Page_Load(object sender, System.EventArgs e)
    {
      ConnectionClass con = new ADODB.ConnectionClass();          
      con.Open("Location=localhost;Initial Catalog=PsiMedicaCubes;Provider=MSOLAP;",string.Empty,string.Empty,(int)ConnectModeEnum.adModeUnknown);
      CatalogClass cat = new ADOMD.CatalogClass();
      cat.ActiveConnection = con;      
      outputHTML = TransformXMLStream(GetTreeXML(cat,con),Server.MapPath("xsl/tree.xsl"));
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
    private string GetTreeXML(CatalogClass cat,ConnectionClass con)
    {     
      string cube = "PsiMedicaDemoCube";
      StringBuilder strDimBldr = new StringBuilder("<ContentMenu>");          
      CubeDef cubeDef = cat.CubeDefs[cube];
      Member mebr = cubeDef.Dimensions["Payor"].Hierarchies[0].Levels["(All)"].Members["HI-TECH CORP (HMO)"];
      for (int i=0; i<cubeDef.Dimensions.Count; i++) 
      {
        // Write out the field or level names.
        Dimension curDim = cubeDef.Dimensions[i];
        string sFolderCaption = "";        
        for (int j=0;j< curDim.Hierarchies.Count; j++) 
        {
          sFolderCaption = curDim.Name;
          if (curDim.Hierarchies[j].Name != "") sFolderCaption += "." + curDim.Hierarchies[j].Name;
                  
          strDimBldr.Append("<MenuItem id=\"" + curDim.Hierarchies[j].UniqueName + "\"  type=\"dimension\" dimension=\"" + curDim.UniqueName + "\" FieldList=\"1\" name=\"" + sFolderCaption + "\">");                      
//          for (int l=0;l<curDim.Hierarchies[j].Levels.Count; l++)
//          {
//            strDimBldr.Append("<MenuItem id=\"" + curDim.Hierarchies[j].Levels[l].UniqueName + "\"  type=\"level\" dimension=\"" + curDim.Hierarchies[j].UniqueName + "\" source=\"FieldList\" dragEnabled=\"1\" level=\"1\" name=\"" + curDim.Hierarchies[j].Levels[l].Caption + "\">");
//            for (int k=0;k<curDim.Hierarchies[j].Levels[l].Members.Count; k++)
//            {
//              strDimBldr.Append("<MenuItem id=\"" + curDim.Hierarchies[j].Levels[l].Members[k].UniqueName + "\" type=\"member\" dimension=\"" + curDim.Hierarchies[j].UniqueName + "\" source=\"FieldList\" dragEnabled=\"1\" member=\"1\" name=\"" + curDim.Hierarchies[j].Levels[l].Members[k].Caption + "\" />");
//            }
//            strDimBldr.Append("</MenuItem>");
//          }
          strDimBldr.Append("</MenuItem>");          
        }
      }
      Recordset rst=null;
      try
      {              
        try
        {
          rst = (Recordset) con.GetType().InvokeMember(
            "OpenSchema",
            System.Reflection.BindingFlags.InvokeMethod ,
            null,
            con,
            new object[] {SchemaEnum.adSchemaSets,new object[]{"PsiMedcaCubes",null,cube}}
            );
        }
        catch
        {}
            
        if (rst.RecordCount>0) 
        {      
              
          // Write out the folder name for Named Sets
          strDimBldr.Append("<MenuItem id=\"Named Sets\" name=\"Named Sets\">");          
              
          while (! rst.EOF) 
          {                  
            // Write out the named set if the function CreateVirtualDimension is not included - this was the means
            // by which 7.0 cubes create virtual dimensions and these should not be included twice.                  
            if (rst.Fields["EXPRESSION"].Value.ToString().IndexOf("CreateVirtualDimension") < 0)
            {
              // The funny replace expression on the dimensions is to add square brackets for
              // named sets with multiple dimensions.       
              strDimBldr.Append("<MenuItem id=\"set" + rst.Fields["SET_NAME"] + "\"  type=\"set\" source=\"FieldList\" dragEnabled=\"1\" set=\"" + rst.Fields["EXPRESSION"] + "\"  dimension=\"[" + Regex.Replace(rst.Fields["DIMENSIONS"].Value.ToString(), @",","],[") + "]\" name=\"" + rst.Fields["SET_NAME"].Value.ToString() + "\"/>");
            }
            rst.MoveNext();
          }
          strDimBldr.Append("</MenuItem>");  
        }
        
        rst = null;
      }
      catch(Exception ex) 
      {
        // Reserved. Don\"t report the error for now. Most likely caused by a 7.0/2000 version problem.
        strDimBldr.Append(ex.ToString());
      }						
      strDimBldr.Append("</ContentMenu>");
      System.Xml.XmlDocument doc = new System.Xml.XmlDocument();
      strDimBldr.Replace("&","&amp;");      
      return strDimBldr.ToString();      
    }
    public static string TransformXMLStream(string xmlStream,string xslPath)
    {
      XmlDocument xmlDoc = new XmlDocument();
      XslTransform xslDoc = new XslTransform();
      xmlDoc.LoadXml(xmlStream);
      xslDoc.Load(xslPath);
      StringWriter sw = new StringWriter();      
      xslDoc.Transform(xmlDoc,null,sw);
      return sw.GetStringBuilder().ToString();
    }                
  }
}