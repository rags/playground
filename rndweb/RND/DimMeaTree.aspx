<%@ Page language="c#" Codebehind="DimMeaTree.aspx.cs" AutoEventWireup="false" Inherits="RND.DimMeaTree" EnableViewState="False"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<HTML>
  <HEAD>
    <title>DimMeaTree</title>
    <meta name="GENERATOR" Content="Microsoft Visual Studio 7.0">
    <meta name="CODE_LANGUAGE" Content="C#">
    <meta name="vs_defaultClientScript" content="JavaScript">
    <meta name="vs_targetSchema" content="http://schemas.microsoft.com/intellisense/ie5">
    <script>
      function handleDivClickEvent(senderNode)
      {      
        if(senderNode.open=="true") collapse(senderNode);
        else  expand(senderNode);        
        event.cancelBubble=true;
      }
      function expand(entity)
      {      
        entity.childNodes(0).all["image"].src = entity.imageOpen;        
        for(i=0; i < entity.childNodes.length; i++) 
                  if(entity.childNodes(i).tagName == "DIV")       entity.childNodes(i).style.display = "block";      
	      entity.open = "true";
        entity.opened="true";       
      }
      function collapse(entity)
      {      
        entity.childNodes(0).all["image"].src = entity.image;        
        for(i=0; i < entity.childNodes.length; i++) 
                  if(entity.childNodes(i).tagName == "DIV")       entity.childNodes(i).style.display = "none";      
	      entity.open = "false";        
      }
       function handleTDMouseOverEvent(senderTD)
      {
        //changeColor(senderTD,1);
       }
       
       function handleTDClickEvent(senderTD)
       {
        //changeColor(senderTD,2);
       }
       
       function handleCheckEvent(senderChk)
       {
        alert(senderChk.id);
       }
    </script>
  </HEAD>
  <body MS_POSITIONING="GridLayout">
    <form id="DimMeaTree" method="post" runat="server">
      <div onclick="javascript:handleDivClickEvent(this)" id="treeHolder" style="PADDING-LEFT: 0px;CURSOR: hand" opened="fasle" open="false" image="./images/tree/plusstart.gif" imageOpen="./images/tree/minusstart.gif">
        <table border="0" cellspacing="0" cellpadding="0">
          <TBODY>
            <tr nowrap>
              <td valign="center">
                <table border="0" cellspacing="0" cellpadding="0" height="100%">
                  <tr nowrap>
                    <td id="imagetreeHolder" valign="center" align="right"></td>
                    <td valign="center" align="right">
                      <img border="0" id="image" width="19" height="21" style="DISPLAY: block" SRC="./images/tree/plusstart.gif">
                    </td>
                  </tr>
                </table>
              </td>
              <td align="left" id="tdtreeHolder" valign="center" nowrap height="19" onMouseOver="handleTDMouseOverEvent(this);" onClick="handleTDClickEvent(this);" STYLE="PADDING-LEFT: 1px;FONT-SIZE: 12px;FONT-FAMILY: arial">
                <b><font color="black">
                    <table border="0" cellpadding="0" cellspacing="0">
                      <tr nowrap>
                        <td>
                          <!--   <input type="checkbox" id="chk_treeHolder" onclick="handleCheckEvent(this);">-->
                        </td>
                        <td style="PADDING-LEFT: 1px;FONT-SIZE: 12px;FONT-FAMILY: arial">Dimensions and 
                          Measures</td>
                      </tr>
                    </table>
                  </font></b>
              </td>
            </tr>
          </TBODY>
        </table>
        <%=outputHTML%>
      </div>
    </form>
  </body>
</HTML>
