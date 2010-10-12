<%@ Page language="c#" Codebehind="frmChart.aspx.cs" AutoEventWireup="false" Inherits="RND.frmChart" %>
<%@ Register TagPrefix="chartfx" Namespace="SoftwareFX.ChartFX.Internet.Server" Assembly="ChartFX.Internet" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>frmChart</title>
    <meta content="Microsoft Visual Studio 7.0" name="GENERATOR">
    <meta content="C#" name="CODE_LANGUAGE">
    <meta content="JavaScript" name="vs_defaultClientScript">
    <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema">
    <script>
function x()
{
  alert(document.getElementById("Chart1").outerHTML); 
}
    </script>
    <script language="VBScript"> 
    <!--
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
			
			-->
		
    </script>
  </HEAD>
  <body MS_POSITIONING="GridLayout"> <!--onload="//setInterval('alert(frmChart.innerHTML)',30000)"-->
    <form id="frmChart" method="post" runat="server">
      <table>
        <tr>
          <td><asp:textbox id="txtQuery" runat="server" Height="109px" Width="816px" TextMode="MultiLine"></asp:textbox>&nbsp;&nbsp;<asp:button id="btnShow" runat="server" Text="View"></asp:button></td>
        </tr>
        <tr>
          <td><CHARTFX:CHART id="Chart1" runat="server" Height="487px" Width="869px" PersonalizedName="xxx"></CHARTFX:CHART></td>
        </tr>
      </table>
    </form>
  </body>
</HTML>
