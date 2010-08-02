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
//using Excel;
using System.Reflection;
using System.Runtime.InteropServices;
using Word;

namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmPrintWordDoc.
	/// </summary>
	public class frmPrintWordDoc : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
            /*
            Excel.Application app = new ApplicationClass();
            Workbooks workBooks = app.Workbooks;
            Workbook workBook = (Workbook )workBooks.GetType().InvokeMember("Open",BindingFlags.InvokeMethod,null,workBooks,new object[]{@"C:\Documents and Settings\raghunandanr\Desktop\Template Format for PDF Transcription1.xls"});
            workBook.PrintOut(Type.Missing,Type.Missing,1,false,Type.Missing,false,true,Type.Missing);
            workBook.Close(false,Type.Missing,Type.Missing);
            app.Quit();
            Marshal.ReleaseComObject(app);            
            app = null;
            GC.Collect();
            GC.WaitForPendingFinalizers();
            */
            Word.Application app=null;
            try
            {
                app = new ApplicationClass();
                //Document doc = new DocumentClass();
                Document doc  = (Document)typeof(Documents).InvokeMember("Open",BindingFlags.InvokeMethod,null,app.Documents,new object[]{@"C:\Documents and Settings\raghunandanr\Desktop\Word_template_prototype.doc"});                                
                object myTrue = true;
                object myFalse = false;
                object missingValue = Type.Missing;
                object range = WdPrintOutRange.wdPrintCurrentPage;
                object items = WdPrintOutItem.wdPrintDocumentContent;
                object copies = "1";
                object pages = "1";
                object pageType = WdPrintOutPages.wdPrintAllPages;
    
                doc.PrintOut(ref myTrue, ref myFalse, ref range,
                    ref missingValue, ref missingValue, ref missingValue,
                    ref items, ref copies, ref pages, ref pageType, ref myFalse,
                    ref myTrue, ref missingValue,  ref myFalse, ref missingValue,
                    ref missingValue, ref missingValue, ref missingValue);                
               typeof(Document).InvokeMember("Close",BindingFlags.InvokeMethod,null,doc,new object[]{});
            }
            catch(Exception ex)
            {
                Response.Write(ex.Message);
                try
                {
                    if(app!=null)
                    {
                        typeof(Word.Application).InvokeMember("Quit",BindingFlags.InvokeMethod,null,app,new object[]{});
                        Marshal.ReleaseComObject(app);            
                        app = null;
                        GC.Collect();
                        GC.WaitForPendingFinalizers();
                    }
                }
                catch{}
            }


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
