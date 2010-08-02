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
using System.Web.Mail;

namespace RND
{
	/// <summary>
	/// Summary description for frmSendMail.
	/// </summary>
	public class frmSendMail : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.TextBox txtTo;
        protected System.Web.UI.WebControls.TextBox txtCC;
        protected System.Web.UI.WebControls.TextBox txtBCC;
        protected System.Web.UI.WebControls.TextBox txtFrom;
        protected System.Web.UI.WebControls.TextBox txtSubject;
        protected System.Web.UI.WebControls.CheckBox chkSendAs;
        protected System.Web.UI.WebControls.Button btnSend;
        protected System.Web.UI.WebControls.TextBox txtBody;
  
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
      this.btnSend.Click += new System.EventHandler(this.btnSend_Click);
      this.Load += new System.EventHandler(this.Page_Load);

    }
		#endregion

        private void btnSend_Click(object sender, System.EventArgs e)
        {    
            SendMail(txtTo.Text ,txtBCC.Text,txtCC.Text,txtFrom.Text,(chkSendAs.Checked)?MailFormat.Html:MailFormat.Text,txtSubject.Text,txtBody.Text,"164.164.150.215");
        }
        private static bool SendMail(string to,string bcc,string cc,string from,MailFormat  format,string subject,string body,string server)
        {
            MailMessage msg = new MailMessage();
            msg.To = to;
            msg.Bcc=bcc;
            msg.Cc=cc;
            msg.From=from;
            msg.BodyFormat= format;
            msg.Subject=subject;
            msg.Body=body;      
            SmtpMail.SmtpServer=server;
            try
            {
                SmtpMail.Send(msg);        
            }
            catch(Exception e)
            {
            HttpContext.Current.Response.Write(e.Message);
            }
            return true;
        }
	}
}
