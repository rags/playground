<%@ Page language="c#" Codebehind="frmFlatenning.aspx.cs" AutoEventWireup="false" Inherits="RND.frmFlatenning" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmFlatenning</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="frmFlatenning" method="post" runat="server">
      <table>
        <tr>
          <td>Server:&nbsp;
            <asp:TextBox id="txtServer" runat="server"></asp:TextBox>&nbsp;&nbsp;&nbsp; 
            Catalog:&nbsp;
            <asp:TextBox id="txtCatalog" runat="server"></asp:TextBox></td>
        </tr>
        <tr>
          <td><asp:TextBox id="txtQuery" runat="server" Height="109px" Width="816px" TextMode="MultiLine"></asp:TextBox>&nbsp;&nbsp;<asp:Button id="btnShow" runat="server" Text="View"></asp:Button></td>
        </tr>
        <tr>
          <td>
            <%=strView.ToString()%>
          </td>
        </tr>
      </table>
    </form>
  </body>
</HTML>
