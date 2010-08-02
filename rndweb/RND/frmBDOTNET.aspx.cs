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
using System.IO;
using System.Text.RegularExpressions;

namespace RND
{
	/// <summary>
	/// Summary description for frmBDOTNET.
	/// </summary>
	public class frmBDOTNET : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
			XmlDocument xmlDoc = new XmlDocument();
			//xmlDoc.LoadXml("<root><tablename ID="1"  Text ="Sample\Store\M\3" /><tablename ID="1"  Text ="Sample\Store\M" /><tablename ID="1"  Text ="Sample\Store\M\1" /><tablename ID="1"  Text ="Sample\Store\M\2" /><tablename ID="2"  Text ="Sample\Time" /><tablename ID="2"  Text ="Sample\Time\1" /></root>");
			xmlDoc.Load(@"c:\temp\xml.xml");
//			StringWriter sw;
//			XmlTextWriter xmlWrite = new XmlTextWriter(sw = new StringWriter());
//			xmlWrite.WriteStartElement("Treenode");
			XmlDocument xmlDoc1 = new XmlDocument();
			xmlDoc1.LoadXml("<Treenode/>");
			XmlNodeList records = xmlDoc.DocumentElement.ChildNodes;
			for(int i=0;i<records.Count;)
			{
				XmlNode  curRec = records[i];
				string /*text = curRec.Attributes["Text"],*/id=curRec.Attributes["ID"].Value;
				Add(xmlDoc,xmlDoc1,id/*,text*/);
				//XmlElement newNode = xmlDoc1.CreateElement("treenode");
				//newNode.SetAttribute("text",curRec.Attributes["Text"]);
			}
			xmlDoc1.Save(@"c:\out.xml");
		}
		
		void Add(XmlDocument docFrom,XmlDocument docTo,string id/*,string text*/)
		{
			XmlNodeList nodeList = docFrom.SelectNodes("root/tablename[@ID='"+id+"']");
			
			string [] text = new string[nodeList.Count];
			foreach(XmlNode curNode in nodeList)
			{
				string curText = curNode.Attributes["Text"].Value;
				Match match = Regex.Match(curText,"\\\\\\d+$");
				int index = 0;
				if(match.Success) index = int.Parse(match.Value.Substring(1));
				text[index] = curText;
				docFrom.DocumentElement.RemoveChild(curNode);
			}
			XmlDocumentFragment docFrag = docTo.CreateDocumentFragment();
			XmlNode parentNode = docFrag;
			foreach(string str in text)
			{
				XmlElement newNode = docTo.CreateElement("treenode");
				newNode.SetAttribute("text",str);
				parentNode.AppendChild(newNode);
				parentNode = newNode;
			}
			docTo.DocumentElement.AppendChild(docFrag);
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
