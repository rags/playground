using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Xml;
using System.Xml.Xsl;
using System.IO;

namespace XML_Transformer
{
	/// <summary>
	/// Summary description for Form1.
	/// </summary>
	public class Form1 : System.Windows.Forms.Form
	{
    private System.Windows.Forms.TextBox txtXMLFile;
    private System.Windows.Forms.OpenFileDialog openFileDialog1;
    private System.Windows.Forms.TextBox txtXSLFile;
    private System.Windows.Forms.Button btnBrowseXML;
    private System.Windows.Forms.Button btnBrowseXSL;
    private System.Windows.Forms.Button btnTransform;
    private System.Windows.Forms.Button btnSave;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.Label label2;
    private System.Windows.Forms.RichTextBox txtOut;
    private System.Windows.Forms.SaveFileDialog saveFileDialog1;
    private System.Windows.Forms.MainMenu mainMenu1;
    private System.Windows.Forms.MenuItem menuItem3;
    
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
      this.txtXMLFile = new System.Windows.Forms.TextBox();
      this.txtXSLFile = new System.Windows.Forms.TextBox();
      this.btnBrowseXML = new System.Windows.Forms.Button();
      this.btnBrowseXSL = new System.Windows.Forms.Button();
      this.btnTransform = new System.Windows.Forms.Button();
      this.btnSave = new System.Windows.Forms.Button();
      this.label1 = new System.Windows.Forms.Label();
      this.label2 = new System.Windows.Forms.Label();
      this.txtOut = new System.Windows.Forms.RichTextBox();
      this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
      this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
      this.mainMenu1 = new System.Windows.Forms.MainMenu();
      this.menuItem3 = new System.Windows.Forms.MenuItem();
      this.SuspendLayout();
      // 
      // txtXMLFile
      // 
      this.txtXMLFile.Location = new System.Drawing.Point(96, 24);
      this.txtXMLFile.Name = "txtXMLFile";
      this.txtXMLFile.Size = new System.Drawing.Size(432, 20);
      this.txtXMLFile.TabIndex = 9;
      this.txtXMLFile.Text = "";
      // 
      // txtXSLFile
      // 
      this.txtXSLFile.Location = new System.Drawing.Point(96, 56);
      this.txtXSLFile.Name = "txtXSLFile";
      this.txtXSLFile.Size = new System.Drawing.Size(432, 20);
      this.txtXSLFile.TabIndex = 1;
      this.txtXSLFile.Text = "";
      // 
      // btnBrowseXML
      // 
      this.btnBrowseXML.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
      this.btnBrowseXML.Location = new System.Drawing.Point(544, 24);
      this.btnBrowseXML.Name = "btnBrowseXML";
      this.btnBrowseXML.Size = new System.Drawing.Size(22, 23);
      this.btnBrowseXML.TabIndex = 2;
      this.btnBrowseXML.Text = "...";
      this.btnBrowseXML.Click += new System.EventHandler(this.btnBrowseXML_Click);
      // 
      // btnBrowseXSL
      // 
      this.btnBrowseXSL.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
      this.btnBrowseXSL.Location = new System.Drawing.Point(544, 56);
      this.btnBrowseXSL.Name = "btnBrowseXSL";
      this.btnBrowseXSL.Size = new System.Drawing.Size(22, 23);
      this.btnBrowseXSL.TabIndex = 3;
      this.btnBrowseXSL.Text = "...";
      this.btnBrowseXSL.Click += new System.EventHandler(this.btnBrowseXSL_Click);
      // 
      // btnTransform
      // 
      this.btnTransform.Location = new System.Drawing.Point(128, 96);
      this.btnTransform.Name = "btnTransform";
      this.btnTransform.TabIndex = 4;
      this.btnTransform.Text = "&Transform";
      this.btnTransform.Click += new System.EventHandler(this.btnTransform_Click);
      // 
      // btnSave
      // 
      this.btnSave.Location = new System.Drawing.Point(328, 96);
      this.btnSave.Name = "btnSave";
      this.btnSave.TabIndex = 5;
      this.btnSave.Text = "&Save";
      this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
      // 
      // label1
      // 
      this.label1.Location = new System.Drawing.Point(16, 24);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(64, 16);
      this.label1.TabIndex = 6;
      this.label1.Text = "XML File:";
      // 
      // label2
      // 
      this.label2.Location = new System.Drawing.Point(16, 56);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(64, 16);
      this.label2.TabIndex = 7;
      this.label2.Text = "XSL File:";
      // 
      // txtOut
      // 
      this.txtOut.Location = new System.Drawing.Point(0, 136);
      this.txtOut.Name = "txtOut";
      this.txtOut.Size = new System.Drawing.Size(600, 304);
      this.txtOut.TabIndex = 8;
      this.txtOut.Text = "";      
      // 
      // saveFileDialog1
      // 
      this.saveFileDialog1.FileName = "doc1";
      // 
      // mainMenu1
      // 
      this.mainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
                                                                              this.menuItem3});
      // 
      // menuItem3
      // 
      this.menuItem3.Index = 0;
      this.menuItem3.Text = "&About";
      this.menuItem3.Click += new System.EventHandler(this.menuItem3_Click);
      // 
      // Form1
      // 
      this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
      this.ClientSize = new System.Drawing.Size(600, 458);
      this.Controls.AddRange(new System.Windows.Forms.Control[] {
                                                                  this.txtOut,
                                                                  this.label2,
                                                                  this.label1,
                                                                  this.btnSave,
                                                                  this.btnTransform,
                                                                  this.btnBrowseXSL,
                                                                  this.btnBrowseXML,
                                                                  this.txtXSLFile,
                                                                  this.txtXMLFile});
      this.MaximumSize = new System.Drawing.Size(608, 485);
      this.Menu = this.mainMenu1;
      this.Name = "Form1";
      this.Text = "XML Transformer";
      this.ResumeLayout(false);

    }
		#endregion

		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new Form1());
		}

    private void btnBrowseXML_Click(object sender, System.EventArgs e)
    {
      openFileDialog1.Filter="XML files(*.xml)|*.xml|All files(*.*)|*.*";      
      openFileDialog1.ShowDialog();
      txtXMLFile.Text=openFileDialog1.FileName;
    }

    private void btnBrowseXSL_Click(object sender, System.EventArgs e)
    {
      openFileDialog1.Filter="XSL files(*.xsl)|*.xsl|All files(*.*)|*.*";      
      openFileDialog1.ShowDialog();
      txtXSLFile.Text=openFileDialog1.FileName;
    }

    private void btnTransform_Click(object sender, System.EventArgs e)
    {
        XmlDocument xmlDoc = new XmlDocument();
        XslTransform xslDoc = new XslTransform();
      try
      {
        xmlDoc.Load(txtXMLFile.Text);
      }
      catch(Exception ex)
      {
        MessageBox.Show("Error loading \""+txtXMLFile.Text+"\". Check if it is a valid xml file\nDetails:\n" + ex.Message,"Load error");
        txtXMLFile.Focus();
        return;
      }
      try
      {
        xslDoc.Load(txtXSLFile.Text);
      }
      catch(Exception ex)
      {
        MessageBox.Show("Error loading \""+txtXSLFile.Text+"\". Check if it is a valid xsl file\nDetails:\n" + ex.Message,"Load error");
        txtXSLFile.Focus();
        return;
      }
      StringWriter sw = new StringWriter();
      try
      {
        xslDoc.Transform(xmlDoc,null,sw);
      }
      catch(Exception ex)
      {
          MessageBox.Show("Transform falied!!!\nDetails:\n" + ex.Message,"Tranformation error");
      }
      txtOut.Text=sw.GetStringBuilder().ToString();
    }

    private void btnSave_Click(object sender, System.EventArgs e)
    {
      if(string.Empty.Equals(txtOut.Text)) return;
      saveFileDialog1.Filter="HTML file(*.htm)|*.htm,*.html|All files(*.*)|*.*";
      saveFileDialog1.FileName="Output";
      saveFileDialog1.ShowDialog();
      
       
      try
      {
        StreamWriter   sw = new StreamWriter(saveFileDialog1.FileName);
        sw.NewLine="\r\n";        
        sw.Write(txtOut.Text);        
        sw.Close();
      }
      catch(Exception ex)
      {
        MessageBox.Show("Error saving the output to \""+saveFileDialog1.FileName+"\".\nDetails:\n" + ex.Message,"Error saving");  
      }
      
    }



    private void menuItem3_Click(object sender, System.EventArgs e)
    {
       MessageBox.Show("Developer: Raghunandan R,\n\t   Nous InfoSystems.\nEmail:\t  rags_@msn.com","About XML Transformer");    
    }

    
	}
}
