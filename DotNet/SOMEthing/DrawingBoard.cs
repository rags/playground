using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;

namespace SOMEthing
{
	/// <summary>	
  /// csc /target:library /out:DrawingBoard.dll /resource:./Pencil.bmp DrawingBoard.cs
	/// </summary>	
	[ToolboxBitmap(typeof(DrawingBoard),"Pencil.bmp")]
	public class DrawingBoard : System.Windows.Forms.Control
	{    
    Button btnForeGround,btnBackGround;    
    public DrawingBoard()
    {      
      btnForeGround = new Button();
      btnForeGround.Left=100;
      btnForeGround.Text="Fore color";        
      btnBackGround = new Button();
      btnBackGround.Left=10;
      btnBackGround.Text="Back color";
      btnBackGround.Top=btnForeGround.Top=100;
      this.Controls.AddRange(new Control [] {btnForeGround,btnBackGround});
       btnBackGround.Click += new EventHandler(HandleColorChange);
      btnForeGround.Click +=new EventHandler(HandleColorChange);
    }
    protected override void OnPaint(PaintEventArgs pe)
    {      
      pe.Graphics.DrawString(Text,Font, new SolidBrush(ForeColor),2,2);
    }
    public void HandleColorChange(object sender,EventArgs args)
    {
      ColorDialog colDialog = new ColorDialog(); 
      colDialog.ShowDialog();
      Button btnSender = (Button)sender;
      if(btnSender==btnForeGround)
        ForeColor = colDialog.Color;      
      else
        BackColor = colDialog.Color;
      //btnSender.BackColor=colDialog.Color;
    }
	}
}
