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
using System.Net;
using System.IO;

namespace RND.Handlers_Modules
{
	/// <summary>
	/// Summary description for HttpClient.
	/// </summary>
	public class HttpClient : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.Button Button1;
    
		private void Page_Load(object sender, System.EventArgs e)
		{            
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
            this.Button1.Click += new System.EventHandler(this.Button1_Click);
            this.Load += new System.EventHandler(this.Page_Load);

        }
		#endregion

        private void Button1_Click(object sender, System.EventArgs e)
        {
            byte [] arr = System.Text.Encoding.ASCII.GetBytes(Request.Form["txtXML"]);
            HttpWebRequest req = (HttpWebRequest) WebRequest.Create("http://localhost/rnd/Server.aspx");            
            req.Method = "POST";
            req.ContentType = "application/x-www-form-urlencoded";            
            req.ContentLength = arr.Length;
            Stream reqStream = req.GetRequestStream();
            reqStream.Write(arr,0,arr.Length);
            reqStream.Flush();
            reqStream.Close();                        
            WebResponse resp =  req.GetResponse();
            if(!req.HaveResponse)
            {
                Response.Write("no resp");
                return;
            }            
            Stream respStream = resp.GetResponseStream();
            arr = new byte[resp.ContentLength];            
            respStream.Read(arr,0,arr.Length);
            respStream.Close(); 
            Response.Clear();
            Response.ContentType="text/xml";
            Response.Write(System.Text.Encoding.ASCII.GetString(arr,0,arr.Length));
            Response.End();        
        }
	}
}
