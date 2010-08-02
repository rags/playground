<%@ Page language="c#" Codebehind="frmGridHeader.aspx.cs" AutoEventWireup="true" Inherits="RND.Grid.frmGridHeader" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
    <HEAD>
        <title>frmGridHeader</title>
        <meta name="GENERATOR" Content="Microsoft Visual Studio .NET 7.1">
        <meta name="CODE_LANGUAGE" Content="C#">
        <meta name="vs_defaultClientScript" content="JavaScript">
        <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
    </HEAD>
    <!--
Pearls of swine bereft of me<BR>Long and weary my road has been<BR>I was lost in the cities<BR>Alone in the 
hills<BR>No sorrow or pity for the leaving I feel<BR><BR>(chorus)<BR>I am not 
your rolling wheels<BR>I am the highway<BR>I am not your carpet ride<BR>I am the 
sky<BR><BR>Friends and liars don't wait for me<BR>I'll get on all by myself<BR>I 
put millions of miles<BR>Under my heels<BR>And still too close to you<BR>I 
feel<BR><BR>(chorus)<BR>I am not your rolling wheels<BR>I am the highway<BR>I am 
not your carpet ride<BR>I am the sky<BR>I am not your blowing wind<BR>I am the 
lightening<BR>I am not your autumn moon<BR>I am the night
    -->
    <body MS_POSITIONING="GridLayout">
        <form id="Form1" method="post" runat="server">
            <asp:DataGrid ID="grid" Runat="server" OnItemCreated="created" OnItemDataBound="bound"  ShowFooter="True" AllowPaging=true>            
            </asp:DataGrid>
        </form>
    </body>
</HTML>
