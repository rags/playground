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
using System.Xml;

namespace RND
{
	/// <summary>
	/// Summary description for frmAddToWebConfig.
	/// </summary>
	public class frmAddToWebConfig : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
			//int x = new Random().Next(), y = new Random(). Next();
            //Response.Write("&lt;add key=\"" + x + "\" value=\"" + y + "\"/>");
			//System.Configuration.ConfigurationSettings.AppSettings.Add(x.ToString(),y.ToString());
			
            XmlDocument doc = new XmlDocument();
            doc.Load(Server.MapPath(@".\web.config"));
            XmlNode appSetings = doc.SelectSingleNode("configuration/appSettings");
            XmlElement nodeAdd = doc.CreateElement("add");
            nodeAdd.SetAttribute("key","myKey");
            nodeAdd.SetAttribute("value","myVal");
            appSetings.AppendChild(nodeAdd);
            doc.Save(Server.MapPath(@".\web.config"));
            Response.Write("Works like a charm!");

            //System.Collections.Specialized.NameValueCollection coll = (System.Collections.Specialized.NameValueCollection)System.Configuration.ConfigurationSettings.GetConfig("ragsSections/ragsSection");
            //Response.Write(coll["key1"]);
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
