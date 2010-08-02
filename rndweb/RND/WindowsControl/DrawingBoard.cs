using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;
using System.Diagnostics;

namespace RND.WindowsControl 
{
	/// <summary>
  /// csc /target:library /out:DrawingBoard.dll /resource:./Pencil.bmp DrawingBoard.cs
	/// </summary>
  public enum PencilType{Circle,Rectangle}
	[ToolboxBitmap(typeof(DrawingBoard),"Pencil.bmp")]
	public class DrawingBoard : System.Windows.Forms.Control
	{
    Button btnForeGround,btnBackGround,btnCircle,btnRect;    
    PencilType drawType;
    int startX,startY,endX,endY;    
    public DrawingBoard()
    {      
        btnForeGround = new Button();
        btnForeGround.Left=100;
        btnForeGround.Text="Fore color";        

        btnBackGround = new Button();
        btnBackGround.Left=10;
        btnBackGround.Text="Back color";

        btnCircle = new Button();
        btnCircle.Left=190;
        btnCircle.Text="Circle";
        
        btnRect = new Button();
        btnRect.Left=280;
        btnRect.Text="Rectangle";

        btnCircle.Top=btnRect.Top=btnBackGround.Top=btnForeGround.Top=470;
        this.Controls.AddRange(new Control [] {btnForeGround,btnBackGround,btnCircle,btnRect});
        this.ForeColor = Color.Black;
        this.BackColor = Color.White;

        btnBackGround.Click += new EventHandler(HandleColorChange);
        btnForeGround.Click +=new EventHandler(HandleColorChange);        
        btnRect.Click +=new EventHandler(SetDrawingType);        
        btnCircle.Click +=new EventHandler(SetDrawingType);        

    }
    
    protected override void OnMouseDown(MouseEventArgs e)
    {
      startX = e.X;
      startY = e.Y;
    }

    protected override void OnMouseUp(MouseEventArgs e)
    {
      endX = e.X;
      endY = e.Y;
      this.Refresh();
    }
    
    protected override void OnDragOver(DragEventArgs e)
    {
      endX = e.X;
      endY = e.Y;      
      TextWriterTraceListener list;
      Debug.Listeners.Add(list=new TextWriterTraceListener(System.Web.HttpContext.Current.Server.MapPath("../TraceLog1.txt")));
      Debug.Write("x: " +startX + " y: "+ startY + "; x1: " + endX  + " y1: " +endY + DateTime.Now.ToString());
      Debug.Listeners.Remove(list);      
      list.Close();
      list.Dispose();
      this.Refresh();
    }
    
    protected override void OnPaint(PaintEventArgs pe)
    {      
      Graphics g = pe.Graphics;
      g.DrawString(Text,Font, new SolidBrush(ForeColor),2,2);
      Pen pen = new Pen(ForeColor);
      if(drawType==PencilType.Circle) g.DrawEllipse(pen,Math.Min(startX,endX),Math.Min(startY,endY),Math.Abs(startX-endX),Math.Abs(startY-endY));
      else if(drawType==PencilType.Rectangle) g.DrawRectangle(pen,Math.Min(startX,endX),Math.Min(startY,endY),Math.Abs(startX-endX),Math.Abs(startY-endY));

    }

    public void SetDrawingType(object sender,EventArgs args)
    {
      Button btnSender = (Button)sender;
      drawType = (sender==btnCircle)?PencilType.Circle:PencilType.Rectangle;
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
