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
using System.Diagnostics;

namespace RND
{
	/// <summary>
	/// Summary description for frmDebugTrace.
	/// </summary>
	public class frmDebugTrace : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// this is page's trace will be appended to page if trace=true in page directive
      //this trace is diff from diagnostics trace
      Trace.Write("cat1","msg1");  
      Trace.Warn("cat1","warn1");
      //will be displayed in debug and release mode - see output window
      TextWriterTraceListener list;
      System.Diagnostics.Trace.Listeners.Add(list = new TextWriterTraceListener(Server.MapPath("./TraceLog.txt")));//also write it to a file      
      System.Diagnostics.Trace.Assert(false,"ha ha ha","he ha he heheh");//when fasle the text is written
      System.Diagnostics.Trace.WriteIf(true,"cat1","msg2");
      System.Diagnostics.Trace.Write("this","is not page tazce");
      System.Diagnostics.Trace.Listeners.Remove(list);      
      list.Close();
      list.Dispose();
      //will not be displayed in debug mode
      Debug.WriteLine("cat1","debugmsg1");
      Debug.Assert(false,"ok","ok ok");
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
