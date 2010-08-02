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
using System.Security.Cryptography;


namespace RND.ckm
{
	/// <summary>
	/// Summary description for frmEncryption.
	/// </summary>
	public class ClsFrmEncryption : System.Web.UI.Page
	{
    protected System.Web.UI.WebControls.TextBox txtIn;
    protected System.Web.UI.WebControls.TextBox txtOut;
    protected System.Web.UI.WebControls.Button btnEncrypt;
    protected System.Web.UI.WebControls.Button btnDecrypt;
    protected System.Web.UI.WebControls.TextBox txtKey;
  
		private void Page_Load(object sender, System.EventArgs e)
		{
			// Put user code to initialize the page here
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
      this.txtOut.TextChanged += new System.EventHandler(this.txtOut_TextChanged);
      this.btnEncrypt.Click += new System.EventHandler(this.btnEncrypt_Click);
      this.btnDecrypt.Click += new System.EventHandler(this.btnDecrypt_Click);
      this.Load += new System.EventHandler(this.Page_Load);

    }
		#endregion

    private void btnEncrypt_Click(object sender, System.EventArgs e)
    {
      txtOut.Text = ClsFrmEncryption.Encrypt(txtIn.Text,txtKey.Text);
    }

    private void btnDecrypt_Click(object sender, System.EventArgs e)
    {
      txtOut.Text = ClsFrmEncryption.Decrypt(txtIn.Text,txtKey.Text);
    }
    public static string Encrypt(string strToEncrypt,string key)
    {
      SymmetricAlgorithm algo = SymmetricAlgorithm.Create();      
      byte [] IV = System.Text.Encoding.UTF8.GetBytes("crhystalplauneto");
      ICryptoTransform trans = algo.CreateEncryptor(System.Text.Encoding.UTF8.GetBytes(key),IV);
      
      byte[] input  = System.Text.Encoding.UTF8.GetBytes(strToEncrypt);
      
      byte[] output =  trans.TransformFinalBlock(input,0,input.Length);

      return Convert.ToBase64String(output);
    }
    public static string Decrypt(string strToDecrypt,string key)
    {
      SymmetricAlgorithm algo = SymmetricAlgorithm.Create();      
      byte [] IV = System.Text.Encoding.UTF8.GetBytes("cryhstalplauneto");
      ICryptoTransform trans = algo.CreateDecryptor(System.Text.Encoding.UTF8.GetBytes(key),IV);
      
      byte[] input  = Convert.FromBase64String(strToDecrypt);
      
      byte[] output =  trans.TransformFinalBlock(input,0,input.Length);

      return System.Text.Encoding.UTF8.GetString(output);
    }
    
    private void txtOut_TextChanged(object sender, System.EventArgs e)
    {
    
    }
	}
}
