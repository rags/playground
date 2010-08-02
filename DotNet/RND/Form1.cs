using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using MAPI;
using System.Reflection;

namespace WindowsApplication1
{
	/// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		public Form1()
		{
			//
			// Required for Windows Form Designer support
			//
			InitializeComponent();

			//
			// TODO: Add any constructor code after InitializeComponent call
			//
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );	
		}

		#region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			// 
			// Form1
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.ClientSize = new System.Drawing.Size(292, 273);
			this.Name = "Form1";
			this.Text = "Form1";
			this.Load += new System.EventHandler(this.Form1_Load);

		}
		#endregion
    [System.Runtime.InteropServices.DllImport("Project1.dll")]
    static extern string x();
		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			//Application.Run(new frmCtrlConsumer());
      MAPI.Session session = new SessionClass();
      session.GetType().InvokeMember("Logon",BindingFlags.InvokeMethod,null,session,new Object[]{});
      AddressLists addrs=null;
      try
      {
        addrs = (AddressLists)session.AddressLists;
      }
      catch(Exception ex)
      {
        MessageBox.Show(ex.Message);return;
      }
      int addrCnt = (int) addrs.Count;
      string x="";
      for(int i=1;i<=addrCnt;i++)
      {
        AddressList curAddr = (AddressList) addrs.get_Item(i);
        x += (string)curAddr.Name + ":\n" ;
        AddressEntries entries = (AddressEntries)curAddr.AddressEntries;
        int entryCnt = (int)entries.Count;
        for(int j=1;j<=entryCnt;j++)
        {
          AddressEntry curEntry = (AddressEntry)entries.get_Item(j);
          string address;
          try{address = (string)curEntry.Address;}catch{address="<null>";}
          x +=  (string)curEntry.Name+ ": " + address  +" -> " + (int)curEntry.DisplayType +"\n";
        }        
      }
      MessageBox.Show(x);
		}

		private void Form1_Load(object sender, System.EventArgs e)
		{
      MessageBox.Show(x());
			//x();
            //strManip();            
      //y()   
   
//      MessageBox.Show((GetTrue() ||GetFalse()).ToString());
//      MessageBox.Show(( GetFalse()&&GetTrue()).ToString());
//      return;

//      string[] a = new string[2];
//      MessageBox.Show("[" +a[0] + "]" + (a[1]==null).ToString() + (string.Empty.Equals(a[1])).ToString() + ("".Equals(a[1])).ToString());
		}
    bool GetTrue()
    {
      MessageBox.Show("true called");
      return true;
    }
    bool GetFalse()
    {
      MessageBox.Show("false called");
      return false;
    }
//        void x()
//        {
//            int x,y;
//            x=y=0;
//            x+=y+=1;
//            MessageBox.Show(x + " " + y); // 1 1
//            x+=y+=2;
//            MessageBox.Show(x + " " + y);//4 3
//            x=y+=2;
//            MessageBox.Show(x + " " + y);//4 3
//        }
        void strManip()
        {
            string str = "01234567";    
            int startInd=2,endInd=7;
            //MessageBox.Show(str.Substring(i,str.Length-(i+1)));
            MessageBox.Show(slice(str,startInd,endInd));
            MessageBox.Show(string.Join(", ", "[ad].[adad],[adad].sf,[dgdf].[d].[dg],[dgd]".Split(new char[] {']',','})));            
            MessageBox.Show(string.Join(" : ",System.Text.RegularExpressions.Regex.Split("[ad].[adad],[adad].sf,[dgdf].[d].[dg],[dgd]","],")));            
        }
        string slice(string str,int start,int end)
        {
                return str.Substring(start,end-(start));
        }
    void y()
    {
      MessageBox.Show(((int)ADODB.SchemaEnum.adSchemaCommands).ToString());
      MessageBox.Show(((int)ADODB.SchemaEnum.adSchemaFunctions ).ToString());
      MessageBox.Show(((int)ADODB.SchemaEnum.adSchemaReferentialContraints).ToString());
      MessageBox.Show(((int)ADODB.SchemaEnum.adSchemaSets ).ToString());            
    }
	}
}
