using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;
using System.IO;

namespace ExcelControl
{
	/// <summary>
	/// Summary description for UserControl1.
	/// </summary>
	public class ExcelControl : System.Windows.Forms.UserControl
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;
        private Excel.Application excelApp; 
        
		public ExcelControl()
		{
			// This call is required by the Windows.Forms Form Designer.
			InitializeComponent();
			// TODO: Add any initialization after the InitComponent call            
            try
            {
                excelApp = new Excel.ApplicationClass();
                excelApp.Visible = true;
                Excel.Workbook book = excelApp.Workbooks.Open(@"C:\Documents and Settings\raghunandanr\Desktop\Benefit Design Modeler V3.28_ Blank.xls",Type.Missing,false,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing,Type.Missing);
                this.CreateGraphics().DrawString("ok ok",new System.Drawing.Font("Arial",25),Brushes.GreenYellow,10,10);
                book.Close(false,Type.Missing,Type.Missing);
            }
            catch(Exception ex)
            {
                this.CreateGraphics().DrawString(ex.Message,new System.Drawing.Font("Arial",16),Brushes.Chocolate,10,10);
            }            
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if( components != null )
					components.Dispose();
			}
			base.Dispose( disposing );
		}

		#region Component Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify 
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
            // 
            // ExcelControl
            // 
            this.BackColor = System.Drawing.SystemColors.ControlDark;
            this.Name = "ExcelControl";
            this.Size = new System.Drawing.Size(304, 264);            
        }
        #endregion

        protected override void OnPaint(PaintEventArgs pe)
        {      
            Graphics g = pe.Graphics;
            g.DrawString(Text,Font, new SolidBrush(ForeColor),2,2);
            Pen pen = new Pen(ForeColor);
            if(drawType==PencilType.Circle) g.DrawEllipse(pen,Math.Min(startX,endX),Math.Min(startY,endY),Math.Abs(startX-endX),Math.Abs(startY-endY));
            else if(drawType==PencilType.Rectangle) g.DrawRectangle(pen,Math.Min(startX,endX),Math.Min(startY,endY),Math.Abs(startX-endX),Math.Abs(startY-endY));

        }

    }
}
