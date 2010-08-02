using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;



namespace RND
{
  /// <summary>
  /// Summary description for ExcelControl.
  /// </summary>
  /// csc /t:library /out:ExcelControl.dll /r:C:\Inetpub\wwwroot\RND\bin\Interop.Excel.dll ExcelControl.cs

  public class ExcelControl: System.Windows.Forms.Control
  {
    private AxOWC.AxSpreadsheet excel;    
    public ExcelControl()
    {
//      Excel.Application _excel = new Excel.ApplicationClass();
//      _excel.Visible=true;
      System.Resources.ResourceManager resources = new System.Resources.ResourceManager(typeof(ExcelControl));
      this.excel = new AxOWC.AxSpreadsheet();
      ((System.ComponentModel.ISupportInitialize)(this.excel)).BeginInit();
      this.SuspendLayout();
      this.excel.Enabled = true;
      this.excel.Location = new System.Drawing.Point(96, 184);
      this.excel.Name = "axSpreadsheet1";
      this.excel.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axSpreadsheet1.OcxState")));
      this.excel.Size = new System.Drawing.Size(576, 288);
      this.excel.TabIndex = 1;      
      this.Controls.AddRange(new System.Windows.Forms.Control[] {
                                                                  this.excel});      
      ((System.ComponentModel.ISupportInitialize)(this.excel)).EndInit();      
      
    }
    public string getHTML()
    {
      return  excel.HTMLData ;      
    }
  }
}