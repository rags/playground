<%@ Page language="c#" Codebehind="frmMutipleTable.aspx.cs" AutoEventWireup="false" Inherits="RND.frmMutipleTable" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
	<HEAD>
		<title>frmMutipleTable</title>
		<meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
		<meta name="CODE_LANGUAGE" Content="C#">
		<meta name="vs_defaultClientScript" content="JavaScript">
		<meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
	</HEAD>
	<body MS_POSITIONING="GridLayout">
		<form id="frmMutipleTable" method="post" runat="server">
		Dataset
		<hr>
			Employee:
			<br>
			<asp:DataGrid id="dgEmployee" runat="server" />
			Department:
			<br>			
			<asp:DataGrid id="dgDepartment" runat="server" />
			<br>
			DataReader
			<hr>
			Employee:
			<br>
			<asp:DataGrid id="dgEmployee1" runat="server" />
			Department:
			<br>
			<br>
			<asp:DataGrid id="dgDepartment1" runat="server" />
		</form>
	</body>
</HTML>
