<%@ Register TagPrefix="chartfx" Namespace="SoftwareFX.ChartFX.Internet.Server" Assembly="ChartFX.Internet" %>
<%@ Page language="c#" Codebehind="WebForm1.aspx.cs" AutoEventWireup="false" Inherits="InternalCommand_Client.WebForm1" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
	<HEAD>
		<title>WebForm1</title>
		<meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
		<meta name="CODE_LANGUAGE" Content="C#">
		<meta name="vs_defaultClientScript" content="JavaScript">
		<meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
		<script language="VBScript"> 
		<!-- 
	
		sub Chart1_InternalCommand(nID)
		msgbox(nID)
		end sub

		--> 
		</script>
	</HEAD>
	<body MS_POSITIONING="GridLayout">
		<form id="Form1" method="post" runat="server">
			<ChartFX:Chart id="Chart1" style="Z-INDEX: 101; LEFT: 10px; POSITION: absolute; TOP: 17px" runat="server" Width="475px" Height="426px"></ChartFX:Chart>
		</form>
	</body>
</HTML>
