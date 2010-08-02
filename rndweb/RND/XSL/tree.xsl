<?xml version="1.0" encoding="UTF-8" ?> 
<!--Author: Raghunandan R.
      Reference: contentree by Raghvendra Ural
      purpose: to build tree from xml got from database
   -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes" />
<xsl:param name="checkBoxRequired" select="'1'"></xsl:param>
<xsl:param name="imgPath" select="'./images/tree'"></xsl:param>
<xsl:template match="/">
    <!--script language="javascript">
      //put all the your  calls for event handlinghere; these may vary from application to application
     /*
      function handleDivClickEvent(senderDiv) 
      {
        
       // window.event.cancelBubble = true;
       //clickOnEntity(senderDiv);
       //GetQuestions(senderDiv);
      }
      
      function handleTDMouseOverEvent(senderTD)
      {
        //changeColor(senderTD,1);
       }
       
       function handleTDClickEvent(senderTD)
       {
        //changeColor(this,2);
       }
       */
    </script-->        
    <xsl:apply-templates select="ContentMenu"/>        
</xsl:template>
<xsl:template match="ContentMenu">
    <xsl:apply-templates select="MenuItem"/>
</xsl:template>
<xsl:template match="MenuItem">
     <div onclick="javascript:handleDivClickEvent(this)" onMouseOver="window.event.cancelBubble = true;contextNode=this;" onMouseOut="//contextNode=null;"
              onselectstart="return true" ondragstart="return true" open="false" id="{@id}" 
               style="padding-left: 0px;cursor: hand;display: none;">
         <xsl:variable name="hasChild" select="count(MenuItem)&gt;0"/>
          <xsl:variable name="image">
                    <xsl:choose>
							                  <xsl:when test="position()!=last()">
								                          <xsl:choose>
									                          <xsl:when test="$hasChild=true()"><xsl:value-of select="concat($imgPath,'/plus1.gif')"/></xsl:when>
									                          <xsl:otherwise><xsl:value-of select="concat($imgPath,'/leaf.gif')"/></xsl:otherwise>
								                          </xsl:choose>
							                  </xsl:when>
							                  <xsl:otherwise>
								                            <xsl:choose>
									                            <xsl:when test="$hasChild=true()">
										                            <xsl:value-of select="concat($imgPath,'/plus2.gif')"/>
								                            </xsl:when>
									                            <xsl:otherwise><xsl:value-of select="concat($imgPath,'/leaf_last1.gif')"/></xsl:otherwise>
								                            </xsl:choose>
							                  </xsl:otherwise>
						    </xsl:choose>
          </xsl:variable>    
          <xsl:attribute name="opened">
              <xsl:choose>
                <xsl:when test="$hasChild=true()"><xsl:value-of select="'false'"/></xsl:when>
                <xsl:otherwise><xsl:value-of select="'true'"/></xsl:otherwise>
              </xsl:choose>
          </xsl:attribute>
          <xsl:attribute name="image">
                <xsl:value-of select="$image"/>
		     </xsl:attribute>
		     <xsl:attribute name="imageOpen">
                  <xsl:choose>
							                    <xsl:when test="position()!=last()">
								                            <xsl:choose>
									                            <xsl:when test="$hasChild=true()"><xsl:value-of select="concat($imgPath,'/minus1.gif')"/></xsl:when>
									                            <xsl:otherwise><xsl:value-of select="concat($imgPath,'/leaf.gif')"/></xsl:otherwise>
								                            </xsl:choose>
							                    </xsl:when>
							                    <xsl:otherwise>
								                              <xsl:choose>
									                              <xsl:when test="$hasChild=true()">
										                              <xsl:value-of select="concat($imgPath,'/minus2.gif')"/>
								                              </xsl:when>
									                              <xsl:otherwise><xsl:value-of select="concat($imgPath,'/leaf_last1.gif')"/></xsl:otherwise>
								                              </xsl:choose>
							                    </xsl:otherwise>
						      </xsl:choose>
		     </xsl:attribute>
		     <table border="0" cellspacing="0" cellpadding="0">
        <TBODY>
          <tr nowrap="true">
            <td valign="middle">
              <table border="0" cellspacing="0" cellpadding="0" height="100%">
                  <tr nowrap="true">
                         <td id="image{@id}" valign="middle" align="right">
                         <xsl:call-template name="InsertLines"/>
                         </td>
                         <td valign="middle" align="right">
                           <img border="0" id="image"  width="19" height="21" style='display: block'>
                                <xsl:attribute name="SRC">
                                        <xsl:value-of select="$image" />
                                </xsl:attribute>
                            </img>
                          </td>
                  </tr>
              </table>
            </td>
            <td align="left" id="td{@id}" valign="middle" nowrap="true" height="19" onMouseOver="handleTDMouseOverEvent(this);" onClick="handleTDClickEvent(this);" >
              <xsl:attribute name="STYLE">padding-left: 1px;font-family: arial;font-size: 12px;</xsl:attribute>
                <b>
                  <font color="black">
                    <xsl:choose>
                    <xsl:when test="$checkBoxRequired='0'"><xsl:value-of select="@name" /></xsl:when>
                    <xsl:otherwise>
                      <table border="0" cellpadding="0" cellspacing="0">
                        <tr nowrap="true">
                        <td><input type="checkbox" id="chk_{@id}" onclick="handleCheckEvent(this);"></input></td>
                        <td style="padding-left: 1px;font-family: arial;font-size: 12px;"><xsl:value-of select="@name" /></td>
                        </tr>
                      </table>
                    </xsl:otherwise>
                    
                    </xsl:choose>
                  </font>
                </b>
              </td>
          </tr>
        </TBODY>
      </table>
      <xsl:apply-templates select="MenuItem"/>
    </div>
  </xsl:template>
  <xsl:template name="InsertLines">
      <xsl:for-each select="ancestor::*[name()!='ContentMenu']">
         <img  border='0'  height='100%' width='16'>
          <xsl:attribute name="SRC">
            <xsl:choose>
              <xsl:when test="following-sibling::*"><xsl:value-of select="concat($imgPath,'/line.gif')"/></xsl:when>
              <xsl:otherwise><xsl:value-of select="concat($imgPath,'/transline.gif')"/></xsl:otherwise>
            </xsl:choose>
          </xsl:attribute>
         </img>
      </xsl:for-each>
  </xsl:template>
 </xsl:stylesheet>