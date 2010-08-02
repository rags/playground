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
using MAPI;
using System.Reflection;


namespace RND
{
	/// <summary>
	/// Summary description for frmImportCDoAddr.
	/// </summary>
	public class frmImportCDoAddr : System.Web.UI.Page
	{
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      
      MAPI.Session session = new SessionClass();      
      //session.Logon(
      session.GetType().InvokeMember("Logon",BindingFlags.InvokeMethod,null,session,new Object[]{"raghunandanr@nous.soft.net","raghu123",false});
      AddressLists addrs=null;
      try
      {
        addrs = (AddressLists)session.AddressLists;
      }
      catch(Exception ex)
      {
        Response.Write(ex.Message);Response.End();
      }
      int addrCnt = (int) addrs.Count;
      for(int i=0;i<addrCnt;i++)
      {
        AddressList curAddr = (AddressList) addrs.get_Item(i);
        Response.Write(curAddr.Name +"&nbsp;:" + ((AddressEntry)((AddressEntries)curAddr.AddressEntries).get_Item(0)).Name+ "BR>");
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
