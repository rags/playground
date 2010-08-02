<%@ Page language="c#" Codebehind="ChartFXClientScript.aspx.cs" AutoEventWireup="false" Inherits="RND.ckm.ChartFXClientScript" %>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title></title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
    <script LANGUAGE="javascript">

			<!--
			/*
			function Chartfx1_DoubleClick(nButton,nClicks,nHitType,x,y,nSeries,nPoint,obj){ 
				alert("Hello, " + nPoint);
			}
			
			function Chartfx1_GetTip(HitType, Series, Point, Object, Text){
				Text = "This is the customized text for Series " + (Series + 1) + " Point " + (Point + 1);
				Chartfx1.ReturnValue = Text;
			}
			*/
			-->
		
    </script>
    <script LANGUAGE="VBScript">
		
			<!--
			
			Sub Chartfx1_DoubleClick(nButton,nClicks,nHitType,x,y,nSeries,nPoint,obj) 
				msgbox("Hello, " & nPoint)
			End Sub
			
			Sub Chartfx1_GetTip(HitType, Series, Point, Object, Text)
				Text = "This is the customized text for Series " & (Series + 1) & " Point " & (Point + 1)
				document.getElementById("Chartfx1").ReturnValue = Text
			End Sub
sub Chartfx1_InternalCommand(nID) 
			MsgBox nID
		end sub 					
			-->
		
    </script>
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="ChartFXClientScript" method="post" runat="server">
      <table>
        <tr>
          <td>
            <% = strChart %>
          </td>
        </tr>
        <tr>
          <td>&nbsp;</td>
        </tr>
        <tr>
          <td>
            <INPUT type="button" value="Access Data" onclick="">
          </td>
        </tr>
        <tr>
          <td>&nbsp;</td>
        </tr>
      </table>
    </form>
  </body>
</HTML>
