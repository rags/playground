using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.IO;
using ADODB;

namespace WindowsApplication2
{
	/// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.Container components = null;

		public Form1()
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
				if (components != null) 
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
            // Form1
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
            this.ClientSize = new System.Drawing.Size(292, 273);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);

        }
		#endregion

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
////			DataTable dt1,dt2;
////            DataSet ds = new DataSet("MyDataBase");
////            dt1 = getTable1();
////            ds.Tables.Add(dt1);
////            dt2 = getTable2();
////            ds.Tables.Add(dt2);
////            ///dt.ChildRelations.Add(dt.Columns["DepartmentID"],empCol);
////            ds.Relations.Add(dt2.Columns["DepartmentID"],dt1.Columns["DepartmentID"]);
////            string s=string.Empty ;
////            StringWriter sw = new StringWriter();
////            ds.WriteXmlSchema(sw);
////            MessageBox.Show(sw.GetStringBuilder().ToString());
////            ds.WriteXml(sw);
////            MessageBox.Show(sw.GetStringBuilder().ToString());
            //new Form2().Show();
//            string[] columns = new String[dt1.Columns.Count];
//            ADODB.RecordsetClass r = new ADODB.RecordsetClass();            
//            for(int i=0;i<dt1.Columns.Count;i++)
//            {
//                columns[i] = dt1.Columns[i].ColumnName;
//            }
//            foreach(DataRow dr in dt1.Rows )
//            {
//                r.AddNew(columns,dr.ItemArray );
//            }
//            
            
            Application.Run(new Form2());
		}

        private static DataTable getTable1()
        {
            DataTable dt = new DataTable("Employee");            
            dt.Columns.Add("EmployeeID",typeof(int));           
            dt.Columns.Add("EmployeeName",typeof(string));
            dt.Columns.Add("Age",typeof(int));
            dt.Columns.Add("Salary",typeof(int));
            dt.Columns.Add("DepartmentID",typeof(int));
            dt.PrimaryKey=new DataColumn[] { dt.Columns["EmployeeID"]};
            dt.Rows.Add(new object[] {1,"Emp1",25,10000,1});
            dt.Rows.Add(new object[] {2,"Emp2",25,10000,1});
            dt.Rows.Add(new object[] {3,"Emp3",25,10000,2});
            dt.AcceptChanges();
            return dt;

        }        
        private static DataTable getTable2()
        {
            DataTable dt = new DataTable("Department");            
            dt.Columns.Add("DepartmentID",typeof(int));           
            dt.Columns.Add("DepartmentName",typeof(string));            
            dt.PrimaryKey=new DataColumn[] { dt.Columns["DepartmentID"]};            
            dt.Rows.Add(new object[] {1,"Dept1"});
            dt.Rows.Add(new object[] {2,"Dept2"});
            dt.Rows.Add(new object[] {3,"Dept3"});
            dt.AcceptChanges();
            return dt;
        }
        private void Form1_Load(object sender, System.EventArgs e)
        {
            
        }
	}
}
