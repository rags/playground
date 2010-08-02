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
using System.Reflection;
using Excel;
using ACRODISTXLib;
using System.Runtime.InteropServices;

namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmExcelToPdf.
	/// </summary>
	public class frmExcelToPdf : System.Web.UI.Page
	{
        protected System.Web.UI.WebControls.HyperLink xxx;
    
        delegate  void X();
		private void Page_Load(object sender, System.EventArgs e)
		{
			//X _x = new X(x);            
            //_x.EndInvoke(_x.BeginInvoke(null,null));
            x();
            //System.Collections.Specialized.NameValueCollection coll = (System.Collections.Specialized.NameValueCollection)System.Configuration.ConfigurationSettings.GetConfig("ragsSections/ragsSection");
            //Response.Write(coll["key1"]);
		}

        private void x()
        {
            Excel.Application app = new ApplicationClass();
            try
            {
                //app.ActivePrinter = "Acrobat Distiller";
                Workbooks workBooks = app.Workbooks;
                Workbook workBook = (Workbook )workBooks.GetType().InvokeMember("Open",BindingFlags.InvokeMethod,null,workBooks,new object[]{@"C:\Documents and Settings\raghunandanr\Desktop\Template Format for PDF Transcription1.xls"});
                workBook.PrintOut(1,Type.Missing,1,false,"Acrobat Distiller",true,true,@"C:\Documents and Settings\raghunandanr\Desktop\Template Format for PDF Transcription1.ps");
                workBook.Close(false,Type.Missing,Type.Missing);
                PdfDistiller dist = new PdfDistillerClass();
                //dist.bSpoolJobs = 1;
                dist.bShowWindow = 0;
                dist.OnJobFail += new _PdfEvents_OnJobFailEventHandler(Fail);
                dist.FileToPDF(@"C:\Documents and Settings\raghunandanr\Desktop\Template Format for PDF Transcription1.ps",null,null);                                                                
                Marshal.ReleaseComObject(dist);
                dist=null;
            }
            catch(Exception ex){Response.Write(ex.Message);}
            finally
            {
                app.Quit();
                Marshal.ReleaseComObject(app);            
                app = null;
                GC.Collect();
                GC.WaitForPendingFinalizers();
            }
        }

        private void Fail(string x,string y)
        {
            Response.Write(x + "<br>" + y);
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
