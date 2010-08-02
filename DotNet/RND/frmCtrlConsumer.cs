using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;

namespace WindowsApplication1
{
	/// <summary>
	/// Summary description for frmCtrlConsumer.
	/// </summary>
	public class frmCtrlConsumer : System.Windows.Forms.Form
	{
    private System.Windows.Forms.Button button1;
    private SOMEthing.DrawingBoard drawingBoard1;
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		public frmCtrlConsumer()
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
      this.button1 = new System.Windows.Forms.Button();
      this.drawingBoard1 = new SOMEthing.DrawingBoard();
      this.SuspendLayout();
      // 
      // button1
      // 
      this.button1.Location = new System.Drawing.Point(368, 480);
      this.button1.Name = "button1";
      this.button1.TabIndex = 1;
      this.button1.Text = "button1";
      this.button1.Click += new System.EventHandler(this.button1_Click);
      // 
      // drawingBoard1
      // 
      this.drawingBoard1.Location = new System.Drawing.Point(160, 136);
      this.drawingBoard1.Name = "drawingBoard1";
      this.drawingBoard1.Size = new System.Drawing.Size(528, 264);
      this.drawingBoard1.TabIndex = 2;
      this.drawingBoard1.Text = "hello";
      // 
      // frmCtrlConsumer
      // 
      this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
      this.ClientSize = new System.Drawing.Size(832, 517);
      this.Controls.AddRange(new System.Windows.Forms.Control[] {
                                                                  this.drawingBoard1,
                                                                  this.button1});
      this.Name = "frmCtrlConsumer";
      this.Text = "hello";
      this.ResumeLayout(false);

    }
		#endregion

    private void button1_Click(object sender, System.EventArgs e)
    {
      //MessageBox.Show(excelControl1.getHTML());      
    }
	}
}
