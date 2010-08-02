<%@ Register TagPrefix="chartfx" Namespace="SoftwareFX.ChartFX.Internet.Server" Assembly="ChartFX.Internet" %>
<%@ Page language="c#" Codebehind="frmChart1.aspx.cs" AutoEventWireup="false" Inherits="RND.frmChart1" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmChart</title>
    <META content="Microsoft Visual Studio 7.0" name="GENERATOR">
    <META content="C#" name="CODE_LANGUAGE">
    <META content="JavaScript" name="vs_defaultClientScript">
    <META content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">

    <SCRIPT language="VBScript"> 
		Sub Chart1_DoubleClick(nButton,nClicks,nHitType,x,y,nSeries,nPoint,obj) 
				msgbox("Hello, " & nPoint)
			End Sub
			
			Sub Chart1_GetTip(HitType, Series, Point, Object, Text)
				Text = "This is the customized text for Series " & (Series + 1) & " Point " & (Point + 1)
				document.getElementById("Chartfx1").ReturnValue = Text
			End Sub
sub Chart1_InternalCommand(nID) 
			MsgBox nID
		end sub 		    	
    </SCRIPT>
  </HEAD>
  <BODY MS_POSITIONING="GridLayout"> <!--onload="//setInterval('alert(frmChart.innerHTML)',30000)"-->
    <FORM id="frmChart" method="post" runat="server">
      <TABLE>
        <TR>
          <TD>
            <asp:textbox id="txtQuery" runat="server" TextMode="MultiLine" Width="816px" Height="109px"></asp:textbox>&nbsp;&nbsp;
            <asp:button id="btnShow" runat="server" Text="View"></asp:button></TD>
        </TR>
        <TR>
          <TD><%=outstr%></TD>
        </TR>
      </TABLE>
    </FORM>
  </BODY>
</HTML>
