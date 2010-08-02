<%@ Language=VBScript %>
<% 
'----------------------------------------------------------------------------------
' Disclaimer
'----------------------------------------------------------------------------------
'Microsoft provides this sample application "as is" for informational purposes only 
'and Microsoft makes no warranties, either express or implied, as to its accuracy 
'of operation or suitability for use. Technical support is not available for the 
'provided source code.
'----------------------------------------------------------------------------------

'
' connect to OLAP server
'
Function ConnectToServer()
	' check if we already have a connection
    	if Not IsObject(Session("ADODBConnection")) then 
	  ' get the connection params
 	  szServer = Request.QueryString("server")
	  szDatabase = Request.QueryString("database")

	  ' create and open ADODB Connection
    	  set C = Server.CreateObject("ADODB.Connection")
    	  C.Provider = "msolap"
    	  C.Open "provider=msolap;data source=" & szServer & ";user id=;password=;Connect timeout=120;Initial catalog=" & szDatabase

	  ' set the session object
    	  Set Session("ADODBConnection") = C
    	end if
End Function

'
' get a cube definition object
'
Function GetCubeDefinition()
	' connect to the OLAP server
	ConnectToServer

	' create a catalog
	set cat = Server.CreateObject("ADOMD.Catalog")
	
	' set the catalog's connection
	set cat.ActiveConnection = Session("ADODBConnection")

	' get the cube definition
	cubeName = Request.QueryString("cube")
	set GetCubeDefinition = cat.CubeDefs(cubeName)
End Function

'
' generate HTML for the dimension members
'
Function DisplayDimensionMembers()
	' get the cube definition
	set cubeDef = GetCubeDefinition

	' get the dimension
	dimName = Request.QueryString("dimension")
	set dimension = cubeDef.Dimensions(dimName)
	
	' get the lowest level to be displayed
	lowestLevel = Request.QueryString("level")

	' display members in each level for each hierarchy
	if dimension.Hierarchies.Count = 1 then
		DisplayHierarchyMembers dimension.Hierarchies(0), lowestLevel
	else
		for hierIndex = 0 to dimension.Hierarchies.Count - 1
			Response.Write (dimension.Hierarchies(hierIndex).Name)
			DisplayHierarchyMembers dimension.Hierarchies(hierIndex), lowestLevel
		next
	end if
End Function

'
' generate HTML for the hierarchy members
'
Function DisplayHierarchyMembers(hierarchy, lowestLevel)
	set rootLevel = hierarchy.Levels(0)
	for memberIndex = 0 to rootLevel.Members.Count - 1
		DisplayMember rootLevel.Members(memberIndex), lowestLevel
	next
End Function

'
' generate HTML for the member
'
Function DisplayMember(member, lowestLevel)
	Response.Write ("<div ")
	Response.Write ("id=" & Chr(34) & member.UniqueName & Chr(34) & " ")
	Response.Write ("class=Member>")

	Response.Write ("<div id=Level style=""position:absolute;left=-100;visibility:hidden"">")
	Response.Write (member.LevelDepth)
	Response.Write ("</div>")

	for i = 0 to member.LevelDepth
		Response.Write ("&nbsp &nbsp ")
	next
	Response.Write (member.Name)
	Response.Write ("</div>")

	' display the children of this member
	if member.LevelDepth - lowestLevel < 0 then
		for memberIndex = 0 to member.Children.Count - 1
			DisplayMember member.Children(memberIndex), lowestLevel
		next	
	end if
End Function
%>


<HTML> 
<HEAD> 
<TITLE>
<%
= "Dimension Browser: " & Request.QueryString("dimension")
%>
</TITLE>
<LINK REL=STYLESHEET TYPE="text/css" HREF="styles.css"> 

<SCRIPT LANGUAGE="JavaScript">

var selectedMember;

function init() {
	window.document.onmousedown = mouseDown
	window.document.ondblclick = mouseDblClick
}

function mouseDown() {
	if (window.event.srcElement.className == "Member") {
		// deselect the currently selected member
		if (selectedMember) {
			selectedMember.style.color="blue"
		}

		// get the unique member name
		selectedMember = window.event.srcElement

		// highlight the selected member
		window.event.srcElement.style.color="red"
	}	
}

function mouseDblClick() {
	if (window.event.srcElement.className == "Member") {
		document.queryForm.elements("level").value = parseInt(window.event.srcElement.children.Level.innerText) + 1
		document.queryForm.submit()
	}	
}

function cmdOK() {
	// update the form on the opener window
	window.close()
	window.opener.document.queryForm.elements("where").value = selectedMember.id
	window.opener.document.queryForm.submit()	
}

</SCRIPT>

</HEAD> 
<BODY onLoad="init()">

<!--
	display the dimension name
-->
<b>
<% = Request.QueryString("dimension") %>
</b>
<br>

<!--
	display the dimension members
-->

<% 
	DisplayDimensionMembers
%>

<p>

<!--
	display the command buttons
-->
<center>
<input type="button" value="OK" onClick="cmdOK()">
<input type="button" value="Cancel" onClick="window.close()">
</center>

<!--
	hidden form
-->
<div CLASS=invisibleForm>
<form CLASS=invisibleForm name="queryForm" action="DimBrowser.asp" method="get">
<input type="TEXT" name="server" value="<% = Request.QueryString("server") %>" size=20>
<input type="TEXT" name="database" value="<% = Request.QueryString("database") %>" size=20>
<input type="TEXT" name="cube" value="<% = Request.QueryString("cube") %>" size=20>
<input type="TEXT" name="dimension" value="<% = Request.QueryString("dimension") %>" size=20>
<input type="TEXT" name="level" value="<% = Request.QueryString("level") %>" size=20>
<input type=submit value="Send">
</form>
</div>


</BODY>
</HTML>