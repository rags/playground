<%@ Page language="c#" Codebehind="frmHttpReq.aspx.cs" AutoEventWireup="false" Inherits="RND.frmHttpReq" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmHttpReq</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmHttpReq" method="post" runat="server">
      <asp:TextBox id="txtServer" runat="server"></asp:TextBox>
      <asp:TextBox id="txtURL" runat="server"></asp:TextBox>
      <asp:Button id="Button1" runat="server" Text="Button"></asp:Button>
      <br>
      <div runat="server" id="container"></div>
    </form>
  </body>
</HTML>
