<%@ Page language="c#" Codebehind="frmExcel.aspx.cs" AutoEventWireup="false" Inherits="RND.ckm.frmExcel" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmExcel</title>
    <META content="Microsoft Visual Studio 7.0" name="GENERATOR">
    <META content="C#" name="CODE_LANGUAGE">
    <META content="JavaScript" name="vs_defaultClientScript">
    <META content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
    <script>
    function getData()
    {
      alert(frmExcel.excel.cells);
      alert(frmExcel.excel.HTMLData);
    }
    </script>
  </HEAD>
  <BODY MS_POSITIONING="GridLayout">
    <FORM id="frmExcel" method="post" runat="server">
      <OBJECT id="simpleControl2" style="WIDTH: 332px; HEIGHT: 306px" height="306" width="332" data="data:application/x-oleobject;base64,IGkzJfkDzxGP0ACqAGhvEzwhRE9DVFlQRSBIVE1MIFBVQkxJQyAiLS8vVzNDLy9EVEQgSFRNTCA0LjAgVHJhbnNpdGlvbmFsLy9FTiI+DQo8SFRNTD48SEVBRD4NCjxNRVRBIGh0dHAtZXF1aXY9Q29udGVudC1UeXBlIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD13aW5kb3dzLTEyNTIiPg0KPE1FVEEgY29udGVudD0iTVNIVE1MIDYuMDAuMjYwMC4wIiBuYW1lPUdFTkVSQVRPUj48L0hFQUQ+DQo8Qk9EWT4NCjxQPiZuYnNwOzwvUD48L0JPRFk+PC9IVE1MPg0K" classid="./ExcelControl#RND.ckm.ExcelControl" VIEWASTEXT>
      </OBJECT>
      <OBJECT style="Z-INDEX: 101; LEFT: 76px; POSITION: absolute; TOP: 348px" classid="clsid:0002E510-0000-0000-C000-000000000046" VIEWASTEXT  id="excel">
        <PARAM NAME="HTMLURL" VALUE="">
        <PARAM NAME="HTMLData" VALUE="<%=excelHtml%>">	
        <PARAM NAME="DataType" VALUE="HTMLDATA">
        <PARAM NAME="AutoFit" VALUE="0">
        <PARAM NAME="DisplayColHeaders" VALUE="-1">
        <PARAM NAME="DisplayGridlines" VALUE="-1">
        <PARAM NAME="DisplayHorizontalScrollBar" VALUE="-1">
        <PARAM NAME="DisplayRowHeaders" VALUE="-1">
        <PARAM NAME="DisplayTitleBar" VALUE="0">
        <PARAM NAME="DisplayToolbar" VALUE="0">
        <PARAM NAME="DisplayVerticalScrollBar" VALUE="-1">
        <PARAM NAME="EnableAutoCalculate" VALUE="-1">
        <PARAM NAME="EnableEvents" VALUE="-1">
        <PARAM NAME="MoveAfterReturn" VALUE="-1">
        <PARAM NAME="MoveAfterReturnDirection" VALUE="0">
        <PARAM NAME="RightToLeft" VALUE="0">
        <PARAM NAME="ViewableRange" VALUE="1:65536">
      </OBJECT>
      <button onclick="getData()">ok ok</button>
    </FORM>
  </BODY>
</HTML>
