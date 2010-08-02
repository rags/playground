<%@ Page language="c#" Codebehind="frmArrayBoundCombo.aspx.cs" AutoEventWireup="false" Inherits="RND.frmArrayBoundCombo" enableviewstate="false"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
    <HEAD>
        <title>frmExcel</title>
        <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
        <meta name="CODE_LANGUAGE" Content="C#">
        <meta name="vs_defaultClientScript" content="JavaScript">
        <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
        <!-- INCLUDE FILE="EditorScript.inc" -->
    </HEAD>
    <body MS_POSITIONING="GridLayout">
        <form id="frmExcel" method="post" runat="server">            
            <asp:DropDownList id="DropDownList1" style="Z-INDEX: 102; LEFT: 325px; POSITION: absolute; TOP: 497px" EnableViewState="True"
                runat="server"></asp:DropDownList>
            <asp:ListBox id="ListBox1" style="Z-INDEX: 103; LEFT: 441px; POSITION: absolute; TOP: 514px"
                runat="server"></asp:ListBox>
                <select id="Dropdownlist2" style="Z-INDEX: 102; LEFT: 325px; POSITION: absolute; TOP: 100px" EnableViewState="True"
                runat="server"></select>
                <asp:TextBox ID="txt" Runat="server" ></asp:TextBox>
            <asp:Button ID="btn" Runat="server"></asp:Button>
        </form>
    </body>
</HTML>
