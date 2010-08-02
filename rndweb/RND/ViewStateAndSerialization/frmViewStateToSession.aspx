<%@ Page language="c#" Codebehind="frmViewStateToSession.aspx.cs" AutoEventWireup="false" Inherits="RND.ViewStateAndSerialization.frmViewStateToSession" enablesessionstate="readonly" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
    <HEAD>
        <title>frmViewStateToSession</title>
        <meta name="GENERATOR" Content="Microsoft Visual Studio .NET 7.1">
        <meta name="CODE_LANGUAGE" Content="C#">
        <meta name="vs_defaultClientScript" content="JavaScript">
        <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
    </HEAD>
    <body MS_POSITIONING="GridLayout">
        <form id="Form1" method="post" runat="server">
            <select id="cboTest" runat="server">
            </select>
            <asp:Button ID="btnPostBack" Runat="server" />
            <asp:Label ID="lbl" Runat="server">ok ok</asp:Label>
        </form>
    </body>
</HTML>
