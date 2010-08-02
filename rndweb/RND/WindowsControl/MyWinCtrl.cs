using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;

namespace RND.WindowsControl 
{
	/// <summary>
	/// Summary description for MyWinCtrl.
  /// csc /target:library /out:MyWinCtrl.dll MyWinCtrl.cs - for compiling
	/// </summary>
	public class MyWinCtrl : System.Windows.Forms.Control
	{
    public MyWinCtrl()
    {
      FontDialog dialog = new FontDialog();
      dialog.ShowDialog();
      Font = dialog.Font;
      ColorDialog colDialog = new ColorDialog(); 
      colDialog.ShowDialog();
      ForeColor = colDialog.Color;      
    }
    protected override void OnPaint(PaintEventArgs pe)
    {      
      pe.Graphics.DrawString(Text,Font, new SolidBrush(ForeColor),2,2);
    }
	}
}
