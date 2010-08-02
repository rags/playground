using System;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.ComponentModel;

namespace RND
{
	/// <summary>
	/// Summary description for Header.
	/// </summary>
	[DefaultProperty("Text"), 
		ToolboxData("<{0}:Header runat=server></{0}:Header>")]
	public class Header : System.Web.UI.WebControls.WebControl
	{
		private string text;
	
		[Bindable(true), 
			Category("Appearance"), 
			DefaultValue("This is the default value")] 
		public string Text 
		{
			get
			{
				return text;
			}

			set
			{
				text = value;
			}
		}

		/// <summary> 
		/// Render this control to the output parameter specified.
		/// </summary>
		/// <param name="output"> The HTML writer to write out to </param>
		protected override void Render(HtmlTextWriter output)
		{
			output.Write(Text);
		}
	}
}
