using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Windows.Forms;



namespace RND.ckm
{
	/// <summary>
	/// Summary description for ExcelControl.
	/// </summary>
  /// csc /t:library /out:ExcelControl.dll /r:C:\Inetpub\wwwroot\RND\bin\Interop.Excel.dll ExcelControl.cs

	public class ExcelControl: System.Windows.Forms.Control
	{
		public ExcelControl()
		{
			Excel.Application _excel = new Excel.ApplicationClass();
      _excel.Visible=true;
		}
	}
}


