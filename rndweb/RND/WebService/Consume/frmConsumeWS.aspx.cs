using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Web;
using System.Web.SessionState;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.HtmlControls;
using RND.com.teachatechie;

namespace RND.WebService.Consume
{
	/// <summary>
	/// Summary description for frmConsumeWS.
	/// </summary>
	public class frmConsumeWS : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.DropDownList cboFontStyle;
    protected System.Web.UI.WebControls.DropDownList cboFontSize;
    protected System.Web.UI.WebControls.DropDownList cboFontFamily;
    protected System.Web.UI.WebControls.TextBox txtImgText;
    protected System.Web.UI.WebControls.DropDownList cboBackgroundColor;
    protected System.Web.UI.WebControls.DropDownList cboForegroundColor;
    protected System.Web.UI.WebControls.Button btnGetImage;
    protected System.Web.UI.WebControls.ValidationSummary valSummary;
    protected System.Web.UI.WebControls.RequiredFieldValidator valImgText;
    protected System.Web.UI.WebControls.Image img;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
      if(!IsPostBack)
      {
        TextToImage objTextToImage = new TextToImage();        
        cboFontStyle.DataSource=objTextToImage.LoadFontStyles();
        cboFontStyle.DataBind();
        cboFontSize.DataSource=objTextToImage.LoadFontSizes();
        cboFontSize.DataBind();
        cboFontFamily.DataSource=objTextToImage.LoadFontFamily();
        cboFontFamily.DataBind();
        cboBackgroundColor.DataSource=cboForegroundColor.DataSource=objTextToImage.LoadColors();
        cboBackgroundColor.DataBind();        
        cboForegroundColor.DataBind();
      }      
		}

		#region Web Form Designer generated code
		override protected void OnInit(EventArgs e)
		{
			//
			// CODEGEN: This call is required by the ASP.NET Web Form Designer.
			//
			InitializeComponent();
			base.OnInit(e);
		}
		
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{    
      this.btnGetImage.Click += new System.EventHandler(this.btnGetImage_Click);
      this.Load += new System.EventHandler(this.Page_Load);

    }
		#endregion

    private void btnGetImage_Click(object sender, System.EventArgs e)
    {
      img.ImageUrl= (new TextToImage().RenderText(cboFontStyle.SelectedItem.Value,cboFontSize.SelectedItem.Value,cboFontFamily.SelectedItem.Value,txtImgText.Text,cboBackgroundColor.SelectedItem.Value,cboForegroundColor.SelectedItem.Value));
    }
	}
}
