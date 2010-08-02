<%@ Page language="c#" Codebehind="frmDrawingBoard.aspx.cs" AutoEventWireup="false" Inherits="RND.WindowsControl.frmDrawingBoard" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<html>
  <head>
    <title>frmClipBoard</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
  </head>
  <body MS_POSITIONING="GridLayout">
    <form id="frmClipBoard" method="post" runat="server">
    <OBJECT id="simpleControl2" style="WIDTH: 700px; HEIGHT: 500px"classid="DrawingBoard.dll#RND.WindowsControl.DrawingBoard" VIEWASTEXT>
    <param name="Text" value="Good bye blue sky" >
    </OBJECT>
    <br>    
    <%="[" + System.Threading.Thread.CurrentPrincipal.Identity.Name +"]"%>    
    <%="[" + System.Web.HttpContext.Current.User.Identity.Name +"]"%>
    </form>
  </body>
</html>
