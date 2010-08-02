using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;

namespace WindowsApplication2
{
	/// <summary>
	/// Summary description for Form2.
	/// </summary>
	public class Form2 : System.Windows.Forms.Form
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		public Form2()
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
				if(components != null)
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
            // Form2
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
            this.ClientSize = new System.Drawing.Size(292, 273);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);

        }
		#endregion

        private void Form2_Load(object sender, System.EventArgs e)
        {
            ADODB.RecordsetClass rs = new ADODB.RecordsetClass();
            ADODB.ConnectionClass cn = new ADODB.ConnectionClass();
                cn.Open("Provider=MSOLAP; Datasource=LocalHost; Initial Catalog=FoodMart 2000","sa","",(int)ADODB.ConnectOptionEnum.adConnectUnspecified);
            rs.ActiveConnection=cn;
            rs.Open("select Order({[Store].Members},PROFIT,desc)  on rows, {Crossjoin({[All products]},{ [Store Cost],[Store Sales]})} on columns from Sales ",cn,ADODB.CursorTypeEnum.adOpenDynamic ,ADODB.LockTypeEnum.adLockUnspecified,1);
            MessageBox.Show(rs.Fields[0].Name); 
            MessageBox.Show(rs.GetString(ADODB.StringFormatEnum.adClipString ,rs.RecordCount,"  ","\n","<null>"));
            //object obj = rs.GetRows(-1,1,null);
//            rs.MoveFirst();
//            String str=string.Empty;
//            while(rs.EOF)
//            {
//                foreach(ADODB.Field f in rs.Fields )
//                {
//                str  += f.Value ;
//
//                }
//                str  +="\n";
//                rs.MoveNext();
//            }
//MessageBox.Show(str);
        }
	}
}
