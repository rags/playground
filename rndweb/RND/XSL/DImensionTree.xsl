<?xml version="1.0" encoding="UTF-8" ?> 
<!--Author: Raghunandan R.
      Reference: contentree by Raghvendra Ural
      purpose: to build tree from xml got from database
   -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes" />
<!--<xsl:param name="checkBoxRequired" select="'1'"></xsl:param>-->
<xsl:param name="imgPath" select="'../images/tree'"></xsl:param>
<xsl:template match="/">
    <!--<div>
    
    </div>-->
    <xsl:apply-templates select="ContentMenu"/>    
</xsl:template>
<xsl:template match="ContentMenu">
    <xsl:apply-templates select="MenuItem"/>
</xsl:template>
<xsl:template match="MenuItem">
<div onclick="javascript:handleDivClickEvent(this)" onMouseOver="window.event.cancelBubble = true;contextNode=this;" onMouseOut="//contextNode=null;"
              onselectstart="return true" ondragstart="return true" open="false" 
               style="padding-left: 0px;cursor: hand;display: none;">               
         <xsl:copy-of select="@id"/>             
         <xsl:copy-of select="@type"/>      
         <xsl:copy-of select="@dimension"/>
         <xsl:copy-of select="@name"/>
          <xsl:variable name="hasChild" select="@type!='member' or @hasChild='true'"/>     
          <xsl:variable name="image">
                    <xsl:choose>
							                  <xsl:when test="position()!=last()">
								                          <xsl:choose>
									                          <xsl:when test="@type='dimension'"><xsl:value-of select="concat($imgPath,'/leaf.gif')"/></xsl:when>
									                          <xsl:otherwise><xsl:value-of select="concat($imgPath,'/plusstart.gif')"/></xsl:otherwise>
								                          </xsl:choose>
							                  </xsl:when>
							                  <xsl:otherwise>															
								                            <xsl:choose>
																<xsl:when test="@type='dimension'"><xsl:value-of select="concat($imgPath,'/leaf_last1.gif')"/></xsl:when>
									                            <xsl:otherwise><xsl:value-of select="concat($imgPath,'/plusstart.gif')"/></xsl:otherwise>
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
                        <td id="image{@id}" valign="middle" align="right"><xsl:call-template name="InsertLines"/></td>
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
              <xsl:attribute name="STYLE">padding-left: 1px;font-family: arial;font-size: 12px;font-weight:bold</xsl:attribute>                
                    <xsl:choose>                    
                    <xsl:when test="@type='dimension'">
                    <table border="0" cellpadding="0" cellspacing="0">
                        <tr nowrap="true">
                        <td>
                        <input type="checkbox" id="chk_{@id}" onclick="handleCheckEvent(this);" disabled="">
                        </input>
                        </td>
                        <td style="padding-left: 1px;font-family: arial;font-size: 12px;"><xsl:value-of select="@name" /></td>
                        </tr>
                      </table>
                    </xsl:when>
                    <xsl:otherwise>
                      <xsl:value-of select="@name" />
                    </xsl:otherwise>                    
                    </xsl:choose>                
              </td>
          </tr>
        </TBODY>
      </table>      
      <xsl:apply-templates />
    </div>
  </xsl:template>
  
  <xsl:template name="InsertLines">  
	<xsl:for-each select="ancestor::*[name()!='ContentMenu']">
		<xsl:choose>
			<xsl:when test="count(following-sibling::*) &gt; 0">
				<img src="{concat($imgPath,'/line.gif')}" border="0"  height='100%' width='16' />	
			</xsl:when>
			<xsl:otherwise>
				<img src="{concat($imgPath,'/transline.gif')}" border='0'  height='100%' width='16' />	
			</xsl:otherwise>
		</xsl:choose>
	</xsl:for-each>

  </xsl:template>
  
 </xsl:stylesheet>

  