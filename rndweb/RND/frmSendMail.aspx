<%@ Page language="c#" Codebehind="frmSendMail.aspx.cs" AutoEventWireup="false" Inherits="RND.frmSendMail" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmSendMail</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmSendMail" method="post" runat="server">
      <table>
        <tr>
          <td>To:</td>
          <td>
            <asp:TextBox id="txtTo" runat="server" Width="412px"></asp:TextBox>
          </td>
        </tr>
        <tr>
          <td>CC:</td>
          <td><asp:TextBox id="txtCC" runat="server" Width="412px"></asp:TextBox></td>
        </tr>
        <tr>
          <td>BCC:</td>
          <td><asp:TextBox id="txtBCC" runat="server" Width="412px"></asp:TextBox></td>
        </tr>
        <tr>
          <td>From</td>
          <td><asp:TextBox id="txtFrom" runat="server" Width="412px"></asp:TextBox></td>
        </tr>
        <tr>
          <td>Subject</td>
          <td><asp:TextBox id="txtSubject" runat="server" Width="412px"></asp:TextBox></td>
        </tr>
        <tr>
          <td>Attachments:</td>
          <td></td>
        </tr>
        <tr>
          <td colspan="2">
            <asp:TextBox id="txtBody" runat="server" TextMode="MultiLine" Columns="60" Rows="12"></asp:TextBox>
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <table>
              <tr>
                <td>
                </td>
                <td>
                  <asp:Button id="btnSend" runat="server" Text="Send"></asp:Button></td>
                <td><asp:CheckBox id="chkSendAs" runat="server" Text="Send as HTML"></asp:CheckBox></td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </form>
  </body>
</HTML>
