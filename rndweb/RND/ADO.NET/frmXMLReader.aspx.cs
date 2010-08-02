using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
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
	/// Summary description for frmXMLReader.
	/// </summary>
	public class frmXMLReader : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      SqlCommand comm = new SqlCommand(
                                                                           "select * from tblEmployee inner join tblDepartment as tblDepartment on " +
                                                                           "tblEmployee.DepartmentID = tblDepartment.DepartmentID for xml auto",
                                                                           new SqlConnection(System.Configuration.ConfigurationSettings.AppSettings["connectionString1"])
                                                                         ); 
      comm.Connection.Open();
      //XmlReader reader = comm.ExecuteXmlReader();
      string xml = comm.ExecuteScalar().ToString();
      Response.ContentType="text/xml";
      Response.Write("<root>");
      //Response.Write(reader.ReadOuterXml());
      Response.Write(xml);
      Response.Write("</root>");
      comm.Connection.Close();
      Response.End();                
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
