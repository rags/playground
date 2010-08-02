<%@ Page language="c#" Codebehind="frmConsumeWS.aspx.cs" AutoEventWireup="false" Inherits="RND.WebService.Consume.frmConsumeWS" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmConsumeWS</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmConsumeWS" method="post" runat="server">
      <table cellspacing="0" cellpadding="4" frame="box" bordercolor="#dcdcdc" rules="none" style="BORDER-COLLAPSE: collapse">
        <tr>
          <td colspan="2"><asp:ValidationSummary ID="valSummary" Runat="server"  DisplayMode=SingleParagraph/>
          </td>
        </tr>
        <tr>
          <td class="frmHeader" background="#dcdcdc" style="BORDER-RIGHT: white 2px solid">Parameter</td>
          <td class="frmHeader" background="#dcdcdc">Value</td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">FontStyle:</td>
          <td><asp:DropDownList ID="cboFontStyle" Runat="server" /></td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">FontSize:</td>
          <td><asp:DropDownList ID="cboFontSize" Runat="server" /></td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">FontFamily:</td>
          <td><asp:DropDownList ID="cboFontFamily" Runat="server" /></td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">ImageText:</td>
          <td><asp:TextBox ID="txtImgText" Runat="server" /><asp:RequiredFieldValidator ControlToValidate=txtImgText ID="valImgText" Runat="server" ErrorMessage="Enter image text">*</asp:RequiredFieldValidator></td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">BackgroundColor:</td>
          <td><asp:DropDownList ID="cboBackgroundColor" Runat="server" /></td>
        </tr>
        <tr>
          <td class="frmText" style="FONT-WEIGHT: normal; COLOR: #000000">ForegroundColor:</td>
          <td><asp:DropDownList ID="cboForegroundColor" Runat="server" /></td>
        </tr>
        <tr>
          <td></td>
          <td align="right">
            <asp:Button ID="btnGetImage" Runat="server" Text="Get Image" /></td>
        </tr>
      </table>
      <br>
      <asp:Image ID="img" ImageAlign=AbsMiddle  Runat="server" AlternateText="Enter details and click Get Image"></asp:Image>
    </form>
  </body>
</HTML>
