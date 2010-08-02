using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;

namespace WindowsApplication1
{
	/// <summary>
	/// Summary description for MyWebControl.
	/// </summary>
	public class MyWebControl : System.Windows.Forms.Control
	{
		public MyWebControl()
		{
		}

		protected override void OnPaint(PaintEventArgs pe)
		{
			// TODO: Add custom paint code here

			// Calling the base class OnPaint
			base.OnPaint(pe);
      pe.Graphics.DrawString(Text, 
        Font, 
        new SolidBrush(ForeColor), 
        ClientRectangle);

		}
	}
}
