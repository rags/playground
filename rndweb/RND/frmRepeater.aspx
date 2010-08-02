<%@ Page language="c#" Codebehind="frmRepeater.aspx.cs" AutoEventWireup="false" Inherits="RND.frmRepeater" EnableViewState="False" EnableViewStatemac="FAlse" Trace="true"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
    <HEAD>
        <title>frmRepeater</title>
        <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
        <meta name="CODE_LANGUAGE" Content="C#">
        <meta name="vs_defaultClientScript" content="JavaScript">
        <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
    </HEAD>
    <body MS_POSITIONING="GridLayout">
        <form id="frmRepeater" method="post" runat="server">
            <asp:Label ID="blb" Runat="server"></asp:Label>
            <asp:Repeater id="repeater" Runat="server" OnDataBinding="x" OnItemDataBound="y">
                <ItemTemplate>
                    <div><%#((Container.ItemIndex +1)%2==0)?"o":"n"%>
                        ok<%#Container.ItemIndex +1%></div>
                </ItemTemplate>
            </asp:Repeater>
            <asp:DataGrid ID="grid" Runat="server" EnableViewState="False" />
            <asp:DropDownList ID="cbo" Runat="server" AutoPostBack=True />
            <asp:Button ID="btn" Runat="server"></asp:Button>
        </form>
    </body>
</HTML>
