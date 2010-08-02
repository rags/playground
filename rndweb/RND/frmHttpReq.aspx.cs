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


namespace RND
{
	/// <summary>
	/// Summary description for frmHttpReq.
	/// </summary>
	public class frmHttpReq : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.Button Button1;
    protected System.Web.UI.WebControls.TextBox txtURL;
    protected System.Web.UI.WebControls.TextBox txtServer;
    protected System.Web.UI.HtmlControls.HtmlGenericControl container;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
     
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
      WebClient client = new WebClient();      
      client.BaseAddress=txtServer.Text;      
      try
      {
        byte [] respArr = client.DownloadData(txtURL.Text);
        container.InnerText=System.Text.Encoding.UTF8.GetString(respArr);
        System.Drawing.Image img = System.Drawing.Image.FromFile(@"C:\inetpub\wwwroot\PICKM\img\psimedica\Gen\demo_title.jpg");
        //byte file = img.
        System.IO.MemoryStream stream =  new System.IO.MemoryStream();
        img.Save(stream,System.Drawing.Imaging.ImageFormat.Jpeg);
        respArr = stream.ToArray();
        container.InnerText += "<br>----------------------------------<br>" + System.Text.Encoding.UTF8.GetString(respArr);
      }
      catch(Exception ex)
      {
        container.InnerText=ex.Message;
      }
    }
	}
}