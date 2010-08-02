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

namespace RND.Attrs.AOP
{
	/// <summary>
	/// Summary description for frmLogTest.
	/// </summary>    
	

	public class frmLogTest : System.Web.UI.Page
	{
        [LogEnable(@"c:\log.txt")]
        class LogConsumer : ContextBoundObject
        {
            //[LogEnable(@"c:\log.txt")]
            public int x=3;
            //[LogEnable(@"c:\log.txt")]
            public string xx = "ha ha ha";
            //[LogEnable(@"c:\log.txt")]
            public LogConsumer() {}
            public int Method1(int x)
            {
                return ++x;
            }
            public string Method2(string s)
            {
                return s + "muhahaaaaa";
            }
        }
    
		private void Page_Load(object sender, System.EventArgs e)
		{
			LogConsumer consumer = new LogConsumer();
            int x = consumer.Method1(consumer.x);
            string str = consumer.Method2(consumer.xx);
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
