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
using System.Xml.Schema;
using System.IO;

namespace RND.XML
{
	/// <summary>
	/// Summary description for frmValidatingReader.
	/// </summary>
	public class frmValidatingReader : System.Web.UI.Page
	{		
		public  void ShowCompileErrors(object sender, ValidationEventArgs args)
		{
			Response.Write("Validation Error: "+args.Message+"<br>" );
		}

		private void Page_Load(object sender, System.EventArgs e)
		{		
			XmlValidatingReader reader = null;
			XmlSchemaCollection myschema = new XmlSchemaCollection();
			ValidationEventHandler eventHandler = new ValidationEventHandler(ShowCompileErrors );
			try
			{
			
				String xmlFrag = @"<?xml version='1.0' ?>
                                                <item>
                                                <xxx:price xmlns:xxx='xxx' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' 
                                                xsi:schemaLocation='test.xsd'></xxx:price>
                                                </item>";
                    /*"<author xmlns='urn:bookstore-schema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>" +
											"<first-name>Herman</first-name>" +
											"<last-name>Melville</last-name>" +
											"</author>";*/
                string xsd = @"<?xml version='1.0' encoding='UTF-8'?> 
<xsd:schema xmlns:xsd='http://www.w3.org/2001/XMLSchema' targetNamespace='xxx'>
<xsd:element name='price' type='xsd:integer' xsd:default='12'/>
</xsd:schema>";


				//Create the XmlParserContext.
				XmlParserContext context = new XmlParserContext(null, null, "", XmlSpace.None);
				//Implement the reader. 
				reader = new XmlValidatingReader(xmlFrag, XmlNodeType.Element, context);
				//Add the schema.
				myschema.Add("xxx", new XmlTextReader(new StringReader(xsd)));
                
				//Set the schema type and add the schema to the reader.
				reader.ValidationType = ValidationType.Schema;
				reader.Schemas.Add(myschema);
				while (reader.Read()){Response.Write(reader.Value);}
				Response.Write("<br>Completed validating xmlfragment<br>");
			}
			catch (XmlException XmlExp)
			{
				Response.Write(XmlExp.Message + "<br>");
			}

			catch(XmlSchemaException XmlSchExp)
			{
				Response.Write(XmlSchExp.Message + "<br>");
			}
			catch(Exception GenExp)
			{
				Response.Write(GenExp.Message + "<br>");
			}
			finally
			{}
            XmlDocument doc;            
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
