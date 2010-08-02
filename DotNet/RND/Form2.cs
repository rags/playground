using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Text.RegularExpressions;

namespace WindowsApplication1
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
      string mdx = " SELECT NON EMPTY    {{[Gender].[All Gender]}*{[Age].[All AgeRange]}} ON ROWS, NON EMPTY      toggledrillstate({[Measures].[Gross charges],[Measures].[Units],[Measures].[Workload],[Measures].[DFS],[Measures].[CNP],[Measures].[Payment]},{[Measures].[Units]}) ON COLUMNS FROM [PsiMedicaDemoCube]";      
      int selInd=Search(mdx,"SELECT"),rowInd=Search(mdx,"ON ROWS,");
      string rowClause=mdx.Substring(selInd + 7,rowInd-selInd-7),colClause=mdx.Substring(rowInd+9,rowInd=Search(mdx,"ON COLUMNS")-rowInd-9);
      MessageBox.Show(colClause + "\n" + rowClause);
      this.Close();
      
    }
    
    public static int Search(string toBeSrched,string srchStr)
    {
      int i=0;
      int length = toBeSrched.Length;
      while(i<length)      
      {
        if(toBeSrched.IndexOf(srchStr,i)==i) return i;
        else i=GetNewStartIndex(toBeSrched,i);      
      }
      return -1;
    }
    public static int GetNewStartIndex(string str,int i)
    {
      if(str[i]!='[') return ++i;
      while(str[i]!=']' &&i<str.Length)
      {
        i++;          
        if(str[i]=='[') i=GetNewStartIndex(str,i) +1;          
      }
      return i;      
    }
	}
}
