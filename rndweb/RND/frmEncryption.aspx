<%@ Page language="c#" Codebehind="CodeBehindForfrmEncryption.aspx.cs" AutoEventWireup="false" Inherits="RND.ckm.ClsFrmEncryption" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmEncryption</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmEncryption" method="post" runat="server">
      <table>
        <tr>
          <td>Text to encrypt/decrypt</td>
          <td><asp:TextBox id="txtIn" runat="server"></asp:TextBox></td>
          <td>Key</td>
          <td><asp:TextBox id="txtKey" runat="server"></asp:TextBox></td>
        </tr>
        <tr>
          <td>Result</td>
          <td><asp:TextBox id="txtOut" runat="server" Enabled="False" Rows="5" Columns="20" TextMode="MultiLine"></asp:TextBox></td>
          <td>
            <asp:Button id="btnEncrypt" runat="server" Text="Encrypt"></asp:Button></td>
          <td>
            <asp:Button id="btnDecrypt" runat="server" Text="Decrypt"></asp:Button></td>
        </tr>
      </table>
    </form>
  </body>
</HTML>
