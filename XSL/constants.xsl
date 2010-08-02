<?xml version="1.0" encoding="UTF-8" ?>
<!--Author: Raghunandan R.
       Module: DisplayFeedback.xsl
       Purpose: common variables ans templates used in Presentation.
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="no" omit-xml-declaration="yes"/>	
  
  <xsl:param name="showCorrectAnswer" select="2" />
  <xsl:param name="mode" select="'feedback'" /> <!-- values 1)test 2)feedback 3)clientFeedback -->
  <!-- for client feedback only -->
  <xsl:param name="questionsPerPage" select="1" />
  <xsl:param name="showNavLinks" select="0" />    
  <xsl:param name="scoreFlag" select="'true'" />
  <xsl:param name="bookMarkFlag" select="'true'" />
  <xsl:param name="hintsFlag" select="'true'" />
  <xsl:param name="allowSkip" select="'false'" />  
  <xsl:param name="timeAlreadyTaken" select="'0:0'" />
  <xsl:param name="enforceTime" select="3" />
  <!--Types of questions-->
  <xsl:variable name="matching" select="'Matching'"/>
  <xsl:variable name="pullDownList" select="'Pull Down List'"/>
  <xsl:variable name="ranking" select="'Ranking'"/>
  <xsl:variable name="entryList" select="'Entry List Static'"/>
  <xsl:variable name="entryListDyna" select="'Entry List Dynamic'"/>
  <xsl:variable name="essay" select="'Essay'"/>
  <xsl:variable name="textMatch" select="'Text Match'"/>
  <xsl:variable name="matrix" select="'Matrix'"/>
  <xsl:variable name="fillInBlanks" select="'Fill In Blanks Static'"/>
  <xsl:variable name="fillInBlanksDyna" select="'Fill In Blanks Dynamic'"/>
  <xsl:variable name="selectABlank" select="'Select a blank'"/>
  <xsl:variable name="numeric" select="'Numeric'"/>
  <xsl:variable name="likertScale" select="'Likert Scale'"/>
  <xsl:variable name="multipleChoiceStatic" select="'Multiple Choice Static'"/>
  <xsl:variable name="multipleChoiceDyna" select="'Multiple Choice Dynamic'"/>
  <xsl:variable name="multipleResponseStatic" select="'Multiple Response Static'"/>
  <xsl:variable name="multipleResponseDyna" select="'Multiple Response Dynamic'"/>
  <xsl:variable name="trueFalse" select="'True / False'"/>
  <!--VARS FOR APPLETS AND MOVIES-->
  <xsl:variable name="connectPoints" select="'Connect the Points'"/>
  <xsl:variable name="slider" select="'Slider'"/>
  <xsl:variable name="multipleResponseHotSpot" select="'HotSpot - Multiple Response'"/>
  <xsl:variable name="multipleChoiceHotSpot" select="'HotSpot - Multiple Choice'"/>
  <xsl:variable name="dragAndDrop" select="'Drag and Drop'"/>
  <xsl:variable name="MacromediaFlash" select="'Macromedia Flash'"/>
  <xsl:variable name="JavaApplet" select="'Java Applet'"/>
  <!--keys -->
  <!--xsl:key name="images" match="/*/template/images/*" use="name(.)"/>				
  <xsl:key name="font" match="/*/template/font/*/@*" use="concat(name(..),name(.))"/>				
  <xsl:key name="content" match="/*/template/content/@*" use="name(.)"/-->					     
  
  <xsl:template match="node()">
    <xsl:value-of select="normalize-space(.)" disable-output-escaping="yes" />
  </xsl:template>
  
  <xsl:template match="material">
    <!--xsl:value-of select="*/text()"/-->
    <xsl:for-each select="*">
      <xsl:choose>
        <xsl:when test="name(.)='mattext'">
          <xsl:apply-templates/>
        </xsl:when>
        <xsl:when test="name(.)='matemtext'">
          <i>
            <xsl:apply-templates/>
          </i>
        </xsl:when>
        <xsl:when test="name(.)='matimage'">
          <xsl:call-template name="image"/>
        </xsl:when>
        <xsl:when test="name(.)='mataudio'"><xsl:call-template name="audio"/></xsl:when>
        <xsl:when test="name(.)='matvideo'"><xsl:call-template name="vidio"/></xsl:when>
        <xsl:when test="name(.)='matapplet'">
       <xsl:value-of disable-output-escaping="yes" select="."/>
        </xsl:when>
        <xsl:when test="name(.)='matapplication'"></xsl:when>
        <xsl:when test="name(.)='matref'"></xsl:when>
        <xsl:when test="name(.)='matbreak'"></xsl:when>
        <xsl:when test="name(.)='matextension'"></xsl:when>
        <xsl:otherwise />
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>
  
	<xsl:template name="image">
		<img src="{.}" />
	</xsl:template>
	
	<xsl:template name="audio">
		<a href="{.}" target="new">
			<img src="/AMS/images/sound1.bmp" />
		</a>
	</xsl:template>

	<xsl:template mode="GetHR" match="content">
	  <hr size="{@questionseperatorsize}" color="{@questionseperatorcolor}" />
	</xsl:template>

		<xsl:template name="vidio">
		<a href="{.}" target="new">
			<EMBED align="middle" src="{.}" type="video/x-msvideo" BORDER="0"></EMBED>
		</a>
	</xsl:template>
	<xsl:template name="getFont">
	  <xsl:param name="size"/>
	  <xsl:choose>
	    <xsl:when test="$size=1">xx-small</xsl:when>
	    <xsl:when test="$size=2">x-small</xsl:when>
	    <xsl:when test="$size=3">small</xsl:when>
	    <xsl:when test="$size=4">medium</xsl:when>
	    <xsl:when test="$size=5">large</xsl:when>
	    <xsl:when test="$size=6">x-large</xsl:when>
	    <xsl:when test="$size&gt;=7">xx-large</xsl:when>
	    <xsl:otherwise>x-small</xsl:otherwise>
	  </xsl:choose>
	</xsl:template>
	
	
	<xsl:template name="makeTable">
	  <xsl:param name="noOfCols" select="5"/>
	  <xsl:param name="noOfcells" select="21"/>	  
	  <table border="0" cellpadding="0" xsl:use-attribute-sets="LinkTableCellSpacing" align="bottom">
	    <xsl:call-template name="makeRows">
	        <xsl:with-param name="noOfCols" select="$noOfCols"/>
	       <xsl:with-param name="noOfcells" select="$noOfcells"/>
	       <xsl:with-param name="curCellNo" select="1"/>	       
	    </xsl:call-template>
	  </table>	  
	</xsl:template>
	
	<xsl:template name="makeRows">
	  <xsl:param name="noOfCols" select="1"/>
	  <xsl:param name="noOfcells" select="21"/>
	  <xsl:param name="curCellNo" select="1"/>	  
	  <xsl:if test="$noOfcells &gt;=  $curCellNo">
	    <tr>
	      <xsl:call-template name="makeCells">
	          <xsl:with-param name="noOfCols" select="$noOfCols"/>
	          <xsl:with-param name="noOfcells" select="$noOfcells"/>
	          <xsl:with-param name="curCellNo" select="$curCellNo"/>	          
	      </xsl:call-template>
	    </tr>
	    <xsl:call-template name="makeRows">
	        <xsl:with-param name="noOfCols" select="$noOfCols"/>
	        <xsl:with-param name="noOfcells" select="$noOfcells"/>
	        <xsl:with-param name="curCellNo" select="$curCellNo + $noOfCols"/>	        
	    </xsl:call-template>
	  </xsl:if>	  
	</xsl:template>
	
	<xsl:template name="makeCells">
	  <xsl:param name="noOfCols" select="1"/>
	  <xsl:param name="curCellNo" select="1"/>
	  <xsl:param name="noOfcells" select="21"/>	  
	  <xsl:if test="$noOfCols &gt; 0 and $noOfcells &gt;=  $curCellNo">
	      <td id="navImg{$curCellNo}" align="center" valign="middle" class="linkImgStyle"  
	              onmouseover="handleLinkEvents(this,eventMOver)" onmouseout="handleLinkEvents(this,eventMOut)"
                onclick="handleLinkEvents(this,eventMClick);" isFlagged="0" selected="0" 
        >              
              <xsl:attribute name="nowrap"/>
              <xsl:value-of select="$curCellNo"/>
        </td>
        <xsl:call-template name="makeCells">
          <xsl:with-param name="noOfCols" select="$noOfCols - 1"/>
	        <xsl:with-param name="curCellNo" select="$curCellNo + 1"/>
	         <xsl:with-param name="noOfcells" select="$noOfcells"/>	         
        </xsl:call-template>
    </xsl:if>
    
	</xsl:template>
	<!--GENERAL APPLET TEMPLATES USED FOR BOTH PRESENTATION AND FEEDBACK-->
	<xsl:template name="CPTApplet">
		<xsl:param name="id"/>
		<xsl:param name="blockNo"/>
		<xsl:variable name="x">
			<xsl:call-template name="xAxis" />
		</xsl:variable>
		<xsl:variable name="y">
			<xsl:call-template name="yAxis" />
		</xsl:variable>
		<object  code="ConnectPointsUser.class" codebase="/ams/applet" id="{$id}" width="{material/matimage/@width}" height="{material/matimage/@height}">
			<param name="imgback" value="{material/matimage/@uri}" />
			<param name="topPos" value="{normalize-space(substring-after($y,','))}" />
			<param name="leftPos" value="{normalize-space(substring-after($x,','))}" />
			<param name="blockNo" value="{$blockNo}" />
			<param name="PointColor" value="{substring-before(../../qticomment,':')}" />
			<param name="LineColor" value="{substring-after(../../qticomment,':')}" />
		</object>
	</xsl:template>
	<xsl:template name="SliderApplet">
		<xsl:param name="id"/>
		<object code="ExcelSlider.class" codebase="/ams/applet" id="{$id}" width="{@width}" height="{@height}">
			<param name="minValue" value="{@lowerbound}" />
			<param name="maxValue" value="{@upperbound}" />
			<param name="incrValue" value="{@step}" />
			<param name="initValue" value="{@startval}" />
			<param name="sliderPos" value="{@orientation}" />
			<param name="ForeColor" value="{substring-after(../../qticomment,':')}" />
		</object>
	</xsl:template>
	<xsl:template name="MRApplet">
		<xsl:param name="id"/>
		<object code="HotSpotUser.class" codebase="/ams/applet" id="{$id}" width="{material/matimage/@width}" height="{material/matimage/@height}">
			<param name="imgback" value="{material/matimage/@uri}" />
			<param name="BlockNo" value="{count(response_label)}" />
			<param name="ForeColor" value="{../../qticomment}" />
			<param name="TypeMarker" value="square" />
		</object>	
    </xsl:template>
    <xsl:template name="MCApplet">
		<xsl:param name="id"/>
		<xsl:variable name="x">
			<xsl:call-template name="xAxis" />
		</xsl:variable>
		<xsl:variable name="y">
			<xsl:call-template name="yAxis" />
		</xsl:variable>    
		<object code="HotSpotRadio.class" codebase="/ams/applet" id="{$id}" width="{material/matimage/@width}" height="{material/matimage/@height}">
			<param name="CorrectValueleft" value="{normalize-space(substring-after($x,','))}" />
			<param name="CorrectValuetop" value="{normalize-space(substring-after($y,','))}" />
			<param name="imgback" value="{material/matimage/@uri}" />
			<param name="ForeColor" value="ffffff" />
			<param name="Enabled" value="No" />			
		</object>
    </xsl:template>
    <xsl:template name="DDApplet">
		<xsl:param name="id"/>
		<xsl:variable name="dec">
			<xsl:call-template name="Display" />
		</xsl:variable>
		<object code="DragDrop.class" codebase="/ams/applet" id="{$id}" width="{material/matimage/@width}" height="{material/matimage/@height}">
			<param name="imgback1" value="blank.jpg" />
			<param name="imgback" value="{material/matimage/@uri}" />
			<param name="img" value="{substring-after($dec,',')}" />
			<param name="PosX" value="0" />
			<param name="PosY" value="0" />
			<param name="ForeColor" value="ffffff" />
			<param name="Enabled" value="No" />			
		</object>	
	</xsl:template>
	<xsl:template name="FlashObject">
		<xsl:param name="id"/>
		<object idref="{$id}" id="FLSH_{substring-before($id,'-')}" name="__AMS_FlashObj" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=4,0,2,0" width="457" height="362">
			<param name="movie" value="{material/matapplication/@uri}{material/matapplication}" />
			<param name="quality" value="high" />
			<param name="SCALE" value="exactfit" />
			<embed src="{material/matapplication/@uri}{material/matapplication}" quality="high" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"></embed>
		</object>
    	</xsl:template>
	<xsl:template name="xAxis">
	<xsl:for-each select="response_label">
		<xsl:value-of select="concat( ',' , substring-before(.,',') )" />
	</xsl:for-each>
	</xsl:template>
	<xsl:template name="yAxis">
	<xsl:for-each select="response_label">
		<xsl:value-of select="concat(',' , substring-before(substring-after(.,','),','))" />
	</xsl:for-each>
	</xsl:template>
	
	<xsl:template match="item" mode="GetParams">
		<xsl:for-each select="user_feedback/response_value">
			<xsl:if test=".!=''">
				<xsl:value-of select='concat( . , ";")' />
			</xsl:if>
		</xsl:for-each>
	</xsl:template>
	
		<xsl:template name="GetDragDropParams">
    <xsl:for-each select="../../../user_feedback/response_value">
			<xsl:if test=".!=''">
				<xsl:value-of select='concat(@ident, "," , . , ";")' />
			</xsl:if>
		</xsl:for-each>	  
	</xsl:template>
	
	<xsl:template name="Display">
	<xsl:for-each select="response_label">
		<xsl:value-of select="concat(',' , material/matimage/@uri)" />
	</xsl:for-each>
	</xsl:template>
	<!-- //////////////////////////////Presentation\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-->
	<!-- loop thru all sections -->
	<xsl:template match="section" mode="test">
		<xsl:apply-templates select="item" mode="test">
			<xsl:with-param name="noOfQuestions" select="count(item)" />
		</xsl:apply-templates>
	</xsl:template>
	<!-- loop thru all questions -->
	<xsl:template match="item" mode="test">
    <xsl:param name="totalquestions" />    
    <div type="Question" questionType="{itemmetadata/qmd_itemtype}" id="_{@ident}" style="display: none;">
      <!--OVERFLOW: auto; WIDTH: 100%" id="DIV_{@ident}" -->
      <p></p>      
      <table cellpadding="0" cellspacing="0" width="100%">
        <tr>
          <td class="questionNo">			
			<xsl:value-of select="concat(position(),' out of ',count(../../section/item))" />
          </td>
          <xsl:if test="$scoreFlag='true'">
            <td align="right">
              <span>
			<xsl:attribute name="style"><xsl:call-template name="getScoreStyle"/></xsl:attribute>
                <xsl:value-of select="concat('Maximum marks: ',  itemmetadata/qmd_maximumscore)" />
              </span>
            </td>
          </xsl:if>
        </tr>
      </table>      
      <!--hr size="{key('content', 'questionseperatorsize')}" color="{key('content', 'questionseperatorcolor')}" /-->
      <xsl:apply-templates mode="GetHR" select="/ClientSidePresentation/template/content"/>      
      <div class="questionHolderStyle" name="questionHolder" id="questionHolder">
      <xsl:apply-templates select="." mode="ChooseTestQuestion"/>            
      <input type="hidden" name="hdnTimeTaken_{@ident}" value="{@time_taken}" />
       <input type="hidden" name="isAnswered_{@ident}" value="0" />
        <!--input type="hidden" name="timeTaken_{@ident}" value="0" /-->
        <input type="hidden" name="attempts_{@ident}" value="0" />
        <input type="hidden" name="isPresented_{@ident}" value="N" />
        <input type="hidden" name="isFlagged_{@ident}" value="0" />
        <xsl:if test="$enforceTime=2">        
        <input type="hidden" name="hdnTotalTime_{@ident}" value="{duration}" />
      </xsl:if>
        <xsl:if test="$hintsFlag='true'">
          <xsl:call-template name="showHints"/>        
        </xsl:if>
      </div>  
    </div>
  </xsl:template>
  
  <xsl:template match="item" mode="ChooseTestQuestion">
  <xsl:variable name="questionType" select="itemmetadata/qmd_itemtype"/>
	<xsl:choose>
        <xsl:when test="$questionType=$matching 
                                                                   or 
                                      $questionType=$pullDownList
                                                                    or
                                      $questionType=$ranking">
          <xsl:apply-templates select="presentation/material" />
          <xsl:call-template name="MatchList" />
        </xsl:when>
        <xsl:when test="$questionType=$entryList or $questionType=$entryListDyna">
          <xsl:apply-templates select="presentation/material" />
          <xsl:call-template name="EntryList" />
        </xsl:when>
        <xsl:when test="$questionType=$essay or $questionType=$textMatch">
          <xsl:apply-templates select="presentation/material" />
          <br /><br />
          <xsl:apply-templates select="presentation/response_str/render_fib" mode="TestEssay" />
        </xsl:when>
        <xsl:when test="itemmetadata/qmd_itemtype=$matrix">
          <xsl:apply-templates select="presentation/material" />
          <xsl:call-template name="Matrix" />
        </xsl:when>
        <xsl:when test="$questionType=$fillInBlanks  or $questionType=$fillInBlanksDyna">
          <xsl:apply-templates select="presentation" mode="TestFillBlanks" />
        </xsl:when>
        <xsl:when test="$questionType=$selectABlank">
          <xsl:apply-templates select="presentation" mode="TestSelectABlank" />
        </xsl:when>
        <xsl:when test="$questionType=$numeric">
          <xsl:apply-templates select="presentation" mode="TestNumeric" />
        </xsl:when>
        <xsl:when test="$questionType=$likertScale or $questionType=$multipleChoiceStatic  or $questionType=$multipleChoiceDyna">
          <xsl:apply-templates select="presentation/material" />
          <xsl:apply-templates select="presentation/response_lid" mode="Choices">
            <xsl:with-param name="type" select="'radio'"/>
          </xsl:apply-templates>
        </xsl:when>
        <xsl:when test="$questionType=$multipleResponseStatic  or $questionType=$multipleResponseDyna">
          <xsl:apply-templates select="presentation/material" />
          <xsl:apply-templates select="presentation/response_lid" mode="Choices">
            <xsl:with-param name="type" select="'checkbox'"/>
          </xsl:apply-templates>
        </xsl:when>
        <xsl:when test="$questionType=$trueFalse">
          <xsl:apply-templates select="presentation/material" />
          <xsl:apply-templates select="presentation/response_lid" mode="TFRadio" />
        </xsl:when>
        <!--***************************CHOOSE APPLETS**************************************-->
        <xsl:when test="$questionType=$connectPoints">
          <xsl:apply-templates select="presentation/material" /><br /><br />
          <xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="TestConnectPoints">
            <xsl:with-param name="blockNo" select="count(resprocessing/respcondition)" />            
          </xsl:apply-templates>
        </xsl:when>
        <xsl:when test="$questionType=$slider">
          <xsl:apply-templates select="presentation/material" /><br /><br />
          <xsl:apply-templates select="presentation/response_lid/render_slider" mode="TestSlider"/>
        </xsl:when>
        <xsl:when test="$questionType=$multipleResponseHotSpot">
          <xsl:apply-templates select="presentation/material" /><br /><br />
          <xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="TestMultipleResponse" />
        </xsl:when>
        <xsl:when test="$questionType=$multipleChoiceHotSpot">
          <xsl:apply-templates select="presentation/material" /><br /><br />
          <xsl:apply-templates select="presentation/flow/response_lid/render_hotspot" mode="TestMultipleChoice" />
        </xsl:when>
        <xsl:when test="$questionType=$dragAndDrop">
          <xsl:apply-templates select="presentation/material" /><br /><br />
          <xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="TestDragDrop" />
        </xsl:when>
        <xsl:when test="$questionType=$MacromediaFlash">
          <xsl:apply-templates select="material" /><br /><br />
          <xsl:apply-templates select="presentation/response_lid/render_extension" mode="TestFlash" />
        </xsl:when>
        <xsl:when test="$questionType=$JavaApplet">
          <xsl:apply-templates select="presentation/material" />
          <div  name="__APPLET_HOLDER" id="__APPLET_HOLDER" idref="{@ident}" fn="{presentation/response_str/render_extension/material/mattext}">		
			<xsl:apply-templates select="presentation/response_str/material" />
          </div>               
          <input type="hidden" name="{@ident}" value="{user_feedback/response_value}" />
        </xsl:when>
      </xsl:choose>      
  </xsl:template>
<!--***************************************************Prsentaion of questions***************************************************-->  
<!--present drop down kind of questions-->
  <xsl:template name="MatchList">
    <table border="0">
      <xsl:for-each select="presentation/response_lid">
        <tr>
          <td>
            <xsl:apply-templates select="material" />
          </td>
          <td>            
            <xsl:variable name="qid" select="../../@ident" /> <!-- question ident -->
            <xsl:variable name="cid" select="@ident" /> <!-- choice ident -->
            <xsl:variable name="selectedID" select="../../user_feedback/response_value[@ident=$cid]" />            
            <select name="{$qid}" question="true">
              <option value="" />
              <xsl:for-each select="render_choice/response_label">
                <option value="{$cid}:{@ident}"> <!--  @ident is optionident  -->
                  <xsl:if test="@ident=$selectedID">
								    <xsl:attribute name="selected" />
							    </xsl:if>
                  <xsl:apply-templates select="material" />
                </option>
              </xsl:for-each>
            </select>
          </td>
        </tr>
      </xsl:for-each>
      <!--xsl:apply-templates select="presentation/response_lid" mode="MatchList"/-->
    </table>
  </xsl:template>
  <!--presentaiton of Entry list type questions-->
   <xsl:template name="EntryList">
    <table border="0">
      <xsl:variable name="qid" select="@ident" />
       <xsl:variable name="quot">"</xsl:variable> 
      <xsl:for-each select="presentation/response_str/render_fib/response_label">
        <xsl:variable name="ident" select="@ident" />	
	      <xsl:variable name="value" select="../../../../user_feedback/response_value[@ident=$ident]" /> 	
        <tr>
          <td>
            <xsl:apply-templates select="flow_mat/material" />
          </td>
          <td>     
            <xsl:value-of select="concat('&lt;input type=text name=',$quot,$qid,'$',@ident,$quot,' value=', $quot, $value, $quot, ' question=true &gt;')" disable-output-escaping="yes"/>			                   
          </td>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:template>
  <!-- present essay and text match questions-->
  <xsl:template match="render_fib" mode="TestEssay">
    <textarea name="{../../../@ident}" rows="{@rows}" cols="{@columns}" >
      <xsl:value-of disable-output-escaping="yes" select="../../../user_feedback/response_value" />		
    </textarea>
  </xsl:template>
  <!-- present matrix questions-->
  <xsl:template name="Matrix">
    <xsl:variable name="qid" select="@ident" />
    <table border="0">
      <xsl:for-each select="presentation/response_lid">
        <xsl:variable name="cid" select="@ident" />
        <xsl:variable name="checkedID" select="../../user_feedback/response_value[@ident=$cid]" />
        <tr>
          <td>
            <xsl:apply-templates select="material" />
          </td>
          <xsl:for-each select="render_choice/response_label">
            <td>
              <input type="radio" name="{$qid}${$cid}" value="{@ident}" question="true" >
                <xsl:if test="@ident=$checkedID">
						      <xsl:attribute name="checked" />
					      </xsl:if>
              </input>              
            </td>
            <td>
              <xsl:apply-templates select="material" />
            </td>
          </xsl:for-each>
        </tr>
      </xsl:for-each>
    </table>
  </xsl:template>
  <!-- fill in the blanks presentation-->
  <xsl:template match="presentation" mode="TestFillBlanks">
    <xsl:variable name="qid" select="../@ident" />
    <xsl:for-each select="*">
      <xsl:choose>
        <xsl:when test="name(.)='material'">
          <xsl:choose>
            <xsl:when test="position()=1">
              <xsl:value-of disable-output-escaping="yes" select="concat( . , '  ')" />
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of disable-output-escaping="yes" select="concat('  ' , . , '  ')" />
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:when test="name(.)='response_str'">
          <xsl:variable name="cid" select="@ident" />
          <!--input type="text" name="{$qid}${@ident}" size="{render_fib/@maxchars}" question="true" onkeypress="return checkType('{render_fib/@fibtype}',this);"></input-->          
				<xsl:variable name="value"  select="../../user_feedback/response_value[@ident=$cid]"/>
				<xsl:variable name="quot">"</xsl:variable>
				<xsl:variable name="apos" >'</xsl:variable>
				<xsl:value-of disable-output-escaping="yes" 
				   select="concat('&lt;input onkeypress=', $quot, 'return checkType(', $apos, render_fib/@fibtype, $apos, ',this);', $quot, ' name=',$quot,$qid,'$',$cid,$quot,' question=true type=text size=',render_fib/@maxchars,' value=',$quot,$value,$quot,' &gt;')"
				 />												 
        </xsl:when>
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>
  <!-- Select a blank presentation -->
  <xsl:template match="presentation" mode="TestSelectABlank">
    <xsl:for-each select="*">
      <xsl:choose>
        <xsl:when test="name(.)='material'">
          <xsl:choose>
            <xsl:when test="position()=1">
              <xsl:value-of disable-output-escaping="yes" select="concat( . , '  ')" />
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of disable-output-escaping="yes" select="concat('  ' , . , '  ')" />
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:when test="name(.)='response_str'">
          <xsl:variable name="qid" select="../../@ident" />
          <xsl:variable name="cid" select="@ident" />
          <xsl:variable name="selectedValue" select="../../user_feedback/response_value[@ident=$cid]" />
          <select name="{$qid}" question="true">
            <option value="" />
            <xsl:for-each select="render_choice/response_label">
              <option value="{$cid}:{@ident}">
                <xsl:if test="@ident=$selectedValue">
									<xsl:attribute name="selected" />
								</xsl:if>
                <xsl:apply-templates select="material" />
              </option>
            </xsl:for-each>
          </select>
        </xsl:when>
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>
  <!-- present Numeric question-->
  <xsl:template match="presentation" mode="TestNumeric">
    <xsl:for-each select="material|response_num ">
      <xsl:choose>
        <xsl:when test="name(.)='material'">
          <xsl:apply-templates select="." />
        </xsl:when>
        <xsl:when test="name(.)='response_num'">
          <input type="text" value="{../../user_feedback/response_value}" title=" Enter a number. " name="{../../@ident}" onkeypress="return checkType('{render_fib/@fibtype}',this)"/>
        </xsl:when>
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>
  <!-- multiple choice,likert scale,multiple response questions are presented here-->
  <xsl:template match="response_lid" mode="Choices">
    <xsl:param name="type"/>
    <table border="0">
	<xsl:choose>
		<xsl:when test="render_choice/response_label/flow_mat/@class='Block'">
			<tr>
				<xsl:for-each select="render_choice/response_label">
					<td>
					<xsl:variable name="id" select="../../../../@ident" />
					  <input type="{$type}" name="{$id}" value="{@ident}" question="true">
							  <xsl:if test="../../../../user_feedback/response_value=@ident">
								  <xsl:attribute name="checked" />
							  </xsl:if>								
					  </input>
					</td>
					<td>
					  <xsl:attribute name="NOWRAP"/>
					  <xsl:apply-templates select="flow_mat/material" />
					</td>
				</xsl:for-each>				
			</tr>
		</xsl:when>
		<xsl:otherwise>
			<xsl:for-each select="render_choice/response_label">
			<tr>
				<td>
				<xsl:variable name="id" select="../../../../@ident" />
				<input type="{$type}" name="{$id}" value="{@ident}" question="true">
						<xsl:if test="../../../../user_feedback/response_value=@ident">
							<xsl:attribute name="checked" />
						</xsl:if>								
				</input>
				</td>
				<td>
				  <xsl:apply-templates select="flow_mat/material" />
				</td>
			</tr>
			</xsl:for-each>
		</xsl:otherwise>
	</xsl:choose>
      
    </table>
  </xsl:template>
  
  <!-- true false questions-->
  <xsl:template match="response_lid" mode="TFRadio">
    <table border="0">
	<xsl:choose>
		<xsl:when test="render_choice/flow_label/response_label/flow_mat/@class='Box'">
			<tr>
				<xsl:for-each select="render_choice/flow_label/response_label">
					<td>
					<xsl:variable name="id" select="../../../../../@ident" />
					<input type="radio" name="{$id}" value="{@ident}" question="true" >
					  <xsl:if test="../../../../../user_feedback/response_value=@ident">
						  <xsl:attribute name="checked" />
					  </xsl:if>
					</input>					
					</td>
					<td>
					<xsl:attribute name="NOWRAP"/>
					<xsl:apply-templates select="flow_mat/material" />
					</td>
				</xsl:for-each>
			</tr>
		</xsl:when>
		<xsl:otherwise>
			<xsl:for-each select="render_choice/flow_label/response_label">
				<tr>
					<td>
					<xsl:variable name="id" select="../../../../../@ident" />
						<input type="radio" name="{$id}" value="{@ident}" question="true" >
					    <xsl:if test="../../../../../user_feedback/response_value=$id">
						    <xsl:attribute name="checked" />
					    </xsl:if>
					  </input>					
					</td>
					<td>					
					  <xsl:apply-templates select="flow_mat/material" />
					</td>
				</tr>
			</xsl:for-each>
		</xsl:otherwise>	
	</xsl:choose>	      
    </table>
  </xsl:template>
  <!--******************************************PRESENT APPLETS AND FLASH*************************************-->
<!-- Connect the points question-->
<xsl:template match="render_hotspot" mode="TestConnectPoints">
    <xsl:param name="blockNo" />    
    <br />
    <xsl:variable name="id" select="../../../@ident" />    
    <xsl:call-template name="CPTApplet">
		<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
		<xsl:with-param name="blockNo" select="$blockNo"/>
    </xsl:call-template>
    <input type="hidden" name="{$id}" >
      <xsl:attribute name="value"><xsl:apply-templates select="../../.." mode="GetParams" /></xsl:attribute>        
    </input>
  </xsl:template>
<!-- Slider type question-->  
  <xsl:template match="render_slider" mode="TestSlider">
    <xsl:variable name="id" select="../../../@ident" />    
    <xsl:call-template name="SliderApplet">
		<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
    </xsl:call-template>
    <input type="hidden" name="{$id}" value="{../../../user_feedback/response_value}" />
  </xsl:template>
  <!-- Multiple response applet-->
  <xsl:template match="render_hotspot" mode="TestMultipleResponse">
    <xsl:variable name="id" select="../../../@ident" />    
    <xsl:call-template name="MRApplet">
		<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
    </xsl:call-template>
    <input type="hidden" name="{$id}">
      <xsl:attribute name="value"><xsl:apply-templates select="../../.." mode="GetParams" /></xsl:attribute>   
    </input>
  </xsl:template>
  <!--Multiple choice applet-->
  <xsl:template match="render_hotspot" mode="TestMultipleChoice">    
    <xsl:variable name="id" select="../../../../@ident" />    
    <xsl:call-template name="MCApplet">
		<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
    </xsl:call-template>
    <input type="hidden" name="{$id}" value="{../../../../user_feedback/response_value}" />
  </xsl:template>
  <!-- Drag and drop applet-->
  <xsl:template match="render_hotspot" mode="TestDragDrop">    
    <xsl:variable name="id" select="../../../@ident" />    
    <xsl:call-template name="DDApplet">
		<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
    </xsl:call-template>
    <input type="hidden" name="{$id}" >
      <xsl:attribute name="value"><xsl:call-template name="GetDragDropParams"/></xsl:attribute>
    </input>
  </xsl:template>
  <!-- MACROMEDIA FLASH Questions-->
  <xsl:template match="render_extension" mode="TestFlash">
  <xsl:variable name="id" select="../../../@ident"/>
  <input type="hidden" name="{$id}" value="{../../../user_feedback/response_value}" />    
    <xsl:call-template name="FlashObject">
		<xsl:with-param name="id" select="$id"/>
    </xsl:call-template>
   </xsl:template> 
   <!-- Template to show hints-->
   <xsl:template mode="GetHints" match="hint">
    <xsl:for-each select="hintmaterial">
      <xsl:variable name="hint" select="normalize-space(flow_mat/material)" />
      <xsl:if test="$hint!=''">
        <div style="visibility: hidden;OVERFLOW: auto;background-color:{$genLightColor}">
          <xsl:value-of select="$hint" />
        </div>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>
  <xsl:template name="GetTimer">
	<div id="timerHolder" class="timerStyle">
		<xsl:choose>	
			<xsl:when test="$enforceTime=1">		
					Time left: <input type="text" class="timeStyle timerStyle" id="txtTimer" value="00:00:00" HIDEFOCUS="true">
					<xsl:attribute name="readonly"/>
					</input>		
				<input type="hidden" name="hdnTimeTaken" value="{/ClientSidePresentation/questestinterop/@time_taken}" />
			</xsl:when>
			<xsl:when test="$enforceTime=2">		
					Time left for question: <input type="text" class="timeStyle timerStyle" id="txtTimer" value="00:00:00" HIDEFOCUS="true">
					<xsl:attribute name="readonly"/>
					</input>		
			</xsl:when>	
			<xsl:otherwise><xsl:text disable-output-escaping="yes">&amp;nbsp;</xsl:text></xsl:otherwise>
		</xsl:choose>
	</div>
  </xsl:template>
<xsl:template name="getNoOfCells">
	<xsl:variable name="noOfQuestions" select="count(section/item)"/>   
	<xsl:choose>
	<xsl:when test="$noOfQuestions  mod $questionsPerPage &gt; 0">
		<xsl:value-of select="substring-before($noOfQuestions div $questionsPerPage,'.') + 1"/>
	</xsl:when>
	<xsl:otherwise>
		<xsl:value-of select="$noOfQuestions div $questionsPerPage"/>
	</xsl:otherwise>
	</xsl:choose>
</xsl:template> 
  <!-- /////////////////////////////////Feedback\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-->
	<!-- loop thru all sections -->
	<xsl:template match="section" mode="feedback">	 
		<xsl:apply-templates select="item" mode="feedback">
			<xsl:with-param name="totalquestions" select="count(item)" />
		</xsl:apply-templates>
	</xsl:template>
	
	<!-- loop thru all questions and choose questions types and take appropriate actions-->
	<xsl:template match="item" mode="feedback">
		<xsl:param name="totalquestions" />		
		<div id="_{@ident}"  type="Question" questionType="{itemmetadata/qmd_itemtype}" style="display: none;">			
			<span class="questionNo"><xsl:value-of select="position()"/> out of <xsl:value-of select="$totalquestions"/></span>			
			<xsl:apply-templates mode="GetHR" select="/ClientSidePresentation/template/content"/>      
			<div name="questionHolder" id="questionHolder" class="questionHolderStyle">				
					<xsl:apply-templates mode="ChooseFeedbackQuestions" select="."/>
			</div>								
      </div>		
	</xsl:template>
	
	<xsl:template  match="item" mode="ChooseFeedbackQuestions">
	<xsl:variable name="questionType" select="itemmetadata/qmd_itemtype"/>
		<div>
			<xsl:variable name="feedbackStyle">
				<xsl:call-template name="getFeedbackStyle"/>
			</xsl:variable>				
			<xsl:choose>
				<xsl:when test="$questionType=$fillInBlanks or $questionType=$fillInBlanksDyna">
					<xsl:apply-templates select="presentation" mode="FillBlanks" />
				</xsl:when>
				<xsl:when test="$questionType=$matching 
													                          or 
							                          $questionType=$pullDownList
													                          or
							                          $questionType=$ranking">
					<xsl:apply-templates select="presentation/material" />
					<table border="0">
						<xsl:apply-templates select="presentation/response_lid" mode="Matching" />
					</table>
				</xsl:when>
				<xsl:when test="$questionType=$numeric">
					<xsl:apply-templates select="presentation" mode="Numeric" />
				</xsl:when>				
				<xsl:when test="$questionType=$likertScale or $questionType=$multipleChoiceStatic or $questionType=$multipleChoiceDyna">
					<xsl:apply-templates select="presentation/material" />
					<xsl:apply-templates select="presentation/response_lid" mode="RadioCheck">
						<xsl:with-param name="inputType" select="'radio'" />
					</xsl:apply-templates>
				</xsl:when>
				<xsl:when test="$questionType=$multipleResponseStatic or $questionType=$multipleResponseDyna">
					<xsl:apply-templates select="presentation/material" />
					<xsl:apply-templates select="presentation/response_lid" mode="RadioCheck">
						<xsl:with-param name="inputType" select="'checkbox'" />
					</xsl:apply-templates>
				</xsl:when>
				<xsl:when test="$questionType=$matrix">
					<xsl:apply-templates select="presentation/material" />
					<table border="0">
						<xsl:apply-templates select="presentation/response_lid" mode="Matrix" />
					</table>
				</xsl:when>
				<xsl:when test="$questionType=$trueFalse">
					<xsl:apply-templates select="presentation/material" />
					<xsl:apply-templates select="presentation/response_lid" mode="TrueFalse" />
				</xsl:when>
				<xsl:when test="$questionType=$entryList or $questionType=$entryListDyna">
					<xsl:apply-templates select="presentation/material" />
					<table border="0">
						<xsl:apply-templates select="presentation/response_str/render_fib/response_label" mode="EntryList" />
					</table>
				</xsl:when>
				<xsl:when test="$questionType=$essay or $questionType=$textMatch">
					<xsl:apply-templates select="presentation/material" />
					<br /><br />
					<xsl:apply-templates select="presentation/response_str/render_fib" mode="Essay" />
					<br /><br />
					<!--hr size="3" color="green" /-->
					<xsl:if test="$questionType=$essay">
						<span style="{$feedbackStyle}">Essay will be evaluated by the tutor later.</span>
					</xsl:if>
				</xsl:when>
				<xsl:when test="$questionType=$selectABlank">
					<xsl:apply-templates select="presentation" mode="SelectABlank" />
				</xsl:when>
				<!-- choose applets questions-->
				<xsl:when test="$questionType=$slider">
					<xsl:apply-templates select="presentation/material" /><br /><br />
					<xsl:apply-templates select="presentation/response_lid/render_slider" mode="Slider" />
				</xsl:when>
				<xsl:when test="$questionType=$connectPoints">
					<xsl:apply-templates select="presentation/material" /><br /><br />
					<xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="ConnectPoints">
						<xsl:with-param name="blockNo" select="count(resprocessing/respcondition)" />
						<xsl:with-param name="RMT" select="3" />
					</xsl:apply-templates>
				</xsl:when>
				<xsl:when test="$questionType=$dragAndDrop">
					<xsl:apply-templates select="material" /><br /><br />
					<xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="DragDrop" />
				</xsl:when>
				<xsl:when test="$questionType=$MacromediaFlash">
					<xsl:apply-templates select="material" /><br /><br />
					<xsl:apply-templates select="presentation/response_lid/render_extension" mode="Flash" />
				</xsl:when>
				<xsl:when test="$questionType=$multipleResponseHotSpot">
					<xsl:apply-templates select="presentation/material" /><br /><br />
					<xsl:apply-templates select="presentation/response_xy/render_hotspot" mode="MultipleResponse" />
				</xsl:when>
				<xsl:when test="$questionType=$multipleChoiceHotSpot">
					<xsl:apply-templates select="presentation/material" /><br /><br />
					<xsl:apply-templates select="presentation/flow/response_lid/render_hotspot" mode="MultipleChoice" />
				</xsl:when>
				<xsl:when test="$questionType=$JavaApplet">
					<xsl:apply-templates select="presentation/material" /><br />
					<xsl:apply-templates select="presentation/response_str/material" />
				</xsl:when>
			</xsl:choose>
			<!--give feedback-->
			<table border="0" cellpadding="0" cellspacing="3">
				<xsl:choose>
					<xsl:when test="user_feedback/presentation_value='NA'">
						<tr style="{$feedbackStyle}">
							<td align="left"><b>Question was not attempted</b></td>
						</tr>
						<xsl:call-template name="showScoreAndAnswer" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:call-template name="showScoreAndAnswer" />
						<tr style="{$feedbackStyle}">
							<xsl:apply-templates mode="FeedBack" select="user_feedback" />
						</tr>
					</xsl:otherwise>
				</xsl:choose>
			</table>				
			<p></p>
		</div>
	</xsl:template>
<!--***************************************************Presentaion of questions***************************************************-->  
<!--present drop down kind of questions-->	
	<xsl:template match="response_lid" mode="Matching">
		<!--input type="hidden" name="{@ident}" value=""></input-->
		<tr>
			<td>
				<xsl:apply-templates select="material" />
			</td>
			<td>
				<xsl:variable name="id" select="@ident" />
				<xsl:variable name="selectedID" select="../../user_feedback/response_value[@ident=$id]" />
				<select>
					<xsl:attribute name="disabled" />					
					<xsl:for-each select="render_choice/response_label">
					  <xsl:if test="@ident=$selectedID">								
						    <option value="{@ident}">							
							    <xsl:apply-templates select="material" />
						    </option>						
						</xsl:if>
					</xsl:for-each>
				</select>
			</td>
		</tr>
	</xsl:template>
<!--presentaiton of Entry list type questions-->
<xsl:template match="response_label" mode="EntryList">
	<xsl:variable name="ident" select="@ident" />	
	<xsl:variable name="value" select="../../../../user_feedback/response_value[@ident=$ident]" /> 	
	<xsl:variable name="quot">"</xsl:variable>
	<tr>
		<td>
			<xsl:apply-templates select="flow_mat/material" />
		</td>
		<td>
			<xsl:value-of select="concat('&lt;input type=text value=', $quot, $value, $quot, ' readonly&gt;')" disable-output-escaping="yes"/>			
		</td>
	</tr>
</xsl:template>
<!-- present essay and text match questions-->
<xsl:template match="render_fib" mode="Essay">
	<textarea rows="{@rows}" cols="{@columns}" > <!--rows="{@rows}" cols="{@columns}"-->
		<xsl:attribute name="readonly" />
		<xsl:value-of disable-output-escaping="yes" select="../../../user_feedback/response_value" />		
	</textarea>
</xsl:template>	
<!-- Unfortunately no one can be told what the matrix is u have to see it for urself-->
<xsl:template match="response_lid" mode="Matrix">
	<tr>
		<td>
			<xsl:apply-templates select="material" />
		</td>
		<xsl:variable name="id" select="@ident" />
		<xsl:variable name="checkedID" select="../../user_feedback/response_value[@ident=$id]" />
		<xsl:for-each select="render_choice/response_label">
			<td>
				<input type="radio">
					<xsl:if test="@ident=$checkedID">
						<xsl:attribute name="checked" />
					</xsl:if>
					<xsl:attribute name="disabled" />
				</input>
			</td>
			<td>
				<xsl:apply-templates select="material" />
			</td>
		</xsl:for-each>
	</tr>
</xsl:template>
<!-- fill in the blanks presentation-->
<xsl:template match="presentation" mode="FillBlanks">
	<xsl:for-each select="*">
		<xsl:choose>
			<xsl:when test="name(.)='material'">
				<xsl:choose>
					<xsl:when test="position()=1">
						<xsl:value-of disable-output-escaping="yes" select="concat( . , '  ')" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of disable-output-escaping="yes" select="concat('  ' , . , '  ')" />
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="name(.)='response_str'">
				<xsl:variable select="@ident" name="id" />
				<xsl:variable name="value"  select="../../user_feedback/response_value[@ident=$id]"/>
				<xsl:variable name="quot">"</xsl:variable>
				<xsl:value-of disable-output-escaping="yes" select="concat('&lt;input type=text size=',render_fib/@maxchars,' value=',$quot,$value,$quot,' readonly&gt;')"/>				
			</xsl:when>
		</xsl:choose>
	</xsl:for-each>
</xsl:template>
<!-- Select a blank presentation -->
<xsl:template match="presentation" mode="SelectABlank">
		<xsl:for-each select="*">
			<xsl:choose>
				<xsl:when test="name(.)='material'">
					<xsl:choose>
						<xsl:when test="position()=1">
							<xsl:value-of disable-output-escaping="yes" select="concat( . , '  ')" />
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of disable-output-escaping="yes" select="concat('  ' , . , '  ')" />
						</xsl:otherwise>
					</xsl:choose>
				</xsl:when>
				<xsl:when test="name(.)='response_str'">
					<xsl:variable name="ident" select="@ident" />					
					<xsl:variable name="selectedValue" select="../../user_feedback/response_value[@ident=$ident]" />					
					<select>
						<xsl:attribute name="disabled" />
						<xsl:for-each select="render_choice/response_label">
						  	<xsl:if test="@ident=$selectedValue">
							      <option value="{@ident}">																      
								      <xsl:apply-templates select="material" />
							      </option>
								</xsl:if>							
						</xsl:for-each>
					</select>
				</xsl:when>
			</xsl:choose>
		</xsl:for-each>
	</xsl:template>
<!-- present Numeric question-->
<xsl:template match="presentation" mode="Numeric">
	<xsl:for-each select="*">
		<xsl:choose>
			<xsl:when test="name(.)='material'">
				<xsl:choose>
					<xsl:when test="position()=1">
						<xsl:value-of disable-output-escaping="yes" select="concat( . , '  ')" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of disable-output-escaping="yes" select="concat('  ' , . , '  ')" />
					</xsl:otherwise>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="name(.)='response_num'">
				<input type="text" value="{../../user_feedback/response_value}">
					<xsl:attribute name="readonly" />
				</input>
			</xsl:when>
		</xsl:choose>
	</xsl:for-each>
</xsl:template>
<!-- likert scale,Mutiple choice, multiple response-->
<xsl:template match="response_lid" mode="RadioCheck">
		<xsl:param name="inputType" />
		<!--input type="hidden" name="{../../@ident}" value=""></input-->		
		<table border="0">
			<xsl:choose>
				<xsl:when test="render_choice/response_label/flow_mat/@class='Block'">
					<tr>
						<xsl:for-each select="render_choice/response_label">
							<td>
								<xsl:variable name="id" select="@ident" />
								<input type="{$inputType}" name="{../../../../@ident}" value="{$id}">
									<xsl:if test="../../../../user_feedback/response_value=$id">
										<xsl:attribute name="checked" />
									</xsl:if>
									<xsl:attribute name="disabled" />
								</input>
							</td>
							<td><xsl:apply-templates select="flow_mat/material" /></td>
						</xsl:for-each>
					</tr>
				</xsl:when>
				<xsl:otherwise>
					<xsl:for-each select="render_choice/response_label">
						<tr>
							<td>
								<xsl:variable name="id" select="@ident" />
								<input type="{$inputType}" name="{../../../../@ident}" value="{$id}">
									<xsl:if test="../../../../user_feedback/response_value=$id">
										<xsl:attribute name="checked" />
									</xsl:if>
									<xsl:attribute name="disabled" />
								</input>
							</td>
							<td><xsl:apply-templates select="flow_mat/material" /></td>
						</tr>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>			
		</table>
	</xsl:template>
<!-- For true/false questions-->
	<xsl:template match="response_lid" mode="TrueFalse">
		<table border="0">
			<xsl:choose>
				<xsl:when test="render_choice/flow_label/response_label/flow_mat/@class='Box'">
					<tr>
						<xsl:for-each select="render_choice/flow_label/response_label">
							<td>
								<xsl:variable name="id" select="@ident" />
								<input type="radio" name="{../../../../../@ident}" value="{$id}">
									<xsl:if test="../../../../../user_feedback/response_value=$id">
										<xsl:attribute name="checked" />
									</xsl:if>
									<xsl:attribute name="disabled" />
								</input>
							</td>
							<td><xsl:apply-templates select="flow_mat/material" /></td>
						</xsl:for-each>
					</tr>
				</xsl:when>
				<xsl:otherwise>
					<xsl:for-each select="render_choice/flow_label/response_label">
						<tr>
							<td>
								<xsl:variable name="id" select="@ident" />
								<input type="radio" name="{../../../../../@ident}" value="{$id}">
									<xsl:if test="../../../../../user_feedback/response_value=$id">
										<xsl:attribute name="checked" />
									</xsl:if>
									<xsl:attribute name="disabled" />
								</input>
							</td>
							<td><xsl:apply-templates select="flow_mat/material" /></td>
						</tr>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
			
		</table>
	</xsl:template>
	<!--***************************************************present applets******************************************************************-->
	<!--general templates-->
	
	<xsl:template match="item" mode="GetCorrectAnswer">
		<xsl:for-each select="user_feedback/correct_answer/answer">
			<xsl:if test=".!=''">
				<xsl:value-of select='concat( . , ";")' />
			</xsl:if>
		</xsl:for-each>
	</xsl:template>

	<xsl:template name="DisplayLinks">
		<xsl:param name="ident" />
		<xsl:param name="correctAns" />
		<xsl:param name="userAns" />		
		<table border="0" cellpadding="0" cellspacing="10">
			<tr>
			 <xsl:if test="$showCorrectAnswer=2">
				  <td>
					  <span style="CURSOR: hand; COLOR: blue; TEXT-DECORATION: underline" onclick="document.applets.item('{$ident}').setParams('{$correctAns}');this.style.color='#800080';">
						  <b>Correct  answer</b>
					  </span>
				  </td>
				</xsl:if>
				<xsl:if test="$userAns!=''">
				  <td>
					  <span style="CURSOR: hand; COLOR: blue; TEXT-DECORATION: underline" onclick="document.applets.item('{$ident}').setParams('{$userAns}');this.style.color='#800080';">
						  <b>Your answer</b>
					  </span>
				  </td>
				</xsl:if>
			</tr>
		</table>
	</xsl:template>
<!--PRESENT APPLET TEMPLATES-->
<!-- Connect the points question-->
	<xsl:template match="render_hotspot" mode="ConnectPoints">
		<xsl:param name="blockNo" />		
		<br />
		<xsl:variable name="ident" select="concat('APPLET_',../../../@ident)" />		
		<xsl:call-template name="CPTApplet">
			<xsl:with-param name="id" select="$ident"/>
			<xsl:with-param name="blockNo" select="$blockNo"/>
		</xsl:call-template>		
		<xsl:variable name="param">
			<xsl:apply-templates select="../../.." mode="GetParams" />
		</xsl:variable>
		<xsl:variable name="correctAns">
			<xsl:apply-templates select="../../.." mode="GetCorrectAnswer" />
		</xsl:variable>
		<input type="hidden" name="{../../../@ident}" value="{$param}" />
		<!--xsl:if test="$showCorrectAnswer=2"-->
			<xsl:call-template name="DisplayLinks">
				<xsl:with-param name="ident" select="$ident" />
				<xsl:with-param name="userAns" select="$param" />
				<xsl:with-param name="correctAns" select="$correctAns" />				
			</xsl:call-template>
		<!--/xsl:if-->
	</xsl:template>
<!-- Slider type question-->
	<xsl:template match="render_slider" mode="Slider">
		<xsl:variable name="ident" select="concat('APPLET_',../../../@ident)" />				
		<xsl:call-template name="SliderApplet">
			<xsl:with-param name="id" select="$ident"/>
		</xsl:call-template>
		<xsl:variable name="correctAns">
			<xsl:value-of select="../../../user_feedback/correct_answer/answer" />
		</xsl:variable>
		<xsl:variable name="userAns" select="../../../user_feedback/response_value" />
		<!--xsl:if test="$showCorrectAnswer=2"-->
			<xsl:call-template name="DisplayLinks">
				<xsl:with-param name="ident" select="$ident" />
				<xsl:with-param name="userAns" select="$userAns" />
				<xsl:with-param name="correctAns" select="../../../user_feedback/correct_answer/answer" />
			</xsl:call-template>
		<!--/xsl:if-->
		<input type="hidden" name="{../../../@ident}" value="{$userAns}" />
	</xsl:template>
<!-- Multiple response applet-->
	<xsl:template match="render_hotspot" mode="MultipleResponse">
		<xsl:variable name="ident" select="concat('APPLET_',../../../@ident)" />		
		<xsl:call-template name="MRApplet">
			<xsl:with-param name="id" select="$ident"/>
		</xsl:call-template>
		<xsl:variable name="param">
			<xsl:apply-templates select="../../.." mode="GetParams" />
		</xsl:variable>
		<xsl:variable name="correctAns">
			<xsl:apply-templates select="../../.." mode="GetCorrectAnswer" />
		</xsl:variable>
		<!--xsl:if test="$showCorrectAnswer=2"-->
			<xsl:call-template name="DisplayLinks">
				<xsl:with-param name="ident" select="$ident" />
				<xsl:with-param name="userAns" select="$param" />
				<xsl:with-param name="correctAns" select="$correctAns" />
			</xsl:call-template>
		<!--/xsl:if-->
		<input type="hidden" name="{../../../@ident}" value="{$param}" />
	</xsl:template>
	<!-- Multiple choice applet-->
	<xsl:template match="render_hotspot" mode="MultipleChoice">		
		<xsl:variable name="ident" select="concat('APPLET_',../../../../@ident)" />		
		<xsl:call-template name="MCApplet">
			<xsl:with-param name="id" select="$ident"/>
		</xsl:call-template>
		<xsl:variable name="param" select="../../../../user_feedback/response_value" />
		<!--xsl:if test="$showCorrectAnswer=2"-->
			<xsl:call-template name="DisplayLinks">
				<xsl:with-param name="ident" select="$ident" />
				<xsl:with-param name="userAns" select="$param" />
				<xsl:with-param name="correctAns" select="../../../../user_feedback/correct_answer/answer" />
			</xsl:call-template>
		<!--/xsl:if-->
		<input type="hidden" name="{../../../../@ident}" value="{$param}" />
	</xsl:template>
<!-- Drag and drop applet-->
	<xsl:template match="render_hotspot" mode="DragDrop">		
		<xsl:variable name="id" select="../../../@ident" />
		<xsl:variable name="param">
      <xsl:call-template name="GetDragDropParams"/>			
		</xsl:variable>
		<xsl:variable name="correctAns">
			<xsl:for-each select="../../../user_feedback/correct_answer/answer">
				<xsl:if test=".!=''">
					<xsl:value-of select='concat(@ident, "," , . , ";")' />
				</xsl:if>
			</xsl:for-each>
		</xsl:variable>		
		<xsl:call-template name="DDApplet">
			<xsl:with-param name="id" select="concat('APPLET_',$id)"/>
		</xsl:call-template>
		<!--xsl:if test="$showCorrectAnswer=2"-->
			<xsl:call-template name="DisplayLinks">
				<xsl:with-param name="ident" select="concat('APPLET_',$id)" />
				<xsl:with-param name="userAns" select="$param" />
				<xsl:with-param name="correctAns" select="$correctAns" />
			</xsl:call-template>
		<!--/xsl:if-->
		<input type="hidden" name="{../../../@ident}" value="{$param}" />
	</xsl:template>	
<!-- MACROMEDIA FLASH Questions-->
<xsl:template match="render_extension" mode="Flash">	
	<xsl:call-template name="FlashObject">
		<xsl:with-param name="id" select="../../../@ident"/>
    </xsl:call-template>
</xsl:template>
<!-- FEEDBACK SUMMARY-->

	<xsl:template mode="showAssessmentResults" match="ParticipantAssessmentResult">
		<xsl:param select="'SumofScores'" name="algorithm" />
		<xsl:variable name="dblSpace" select="'  '"/>
		<table border="0" cellpadding="0" cellspacing="0" align="center">
			<xsl:attribute name="style">
				<xsl:call-template name="getFeedbackStyle"/>
			</xsl:attribute>
			<tr>
				<th colspan="2">Assessment result</th>
			</tr>
			<tr>
				<td>No. of questions in assessment: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntTotalQuestions)" />
				</td>
			</tr>
			<tr>
				<td>No. of correct answers: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntCorrect)" />
				</td>
			</tr>
			<tr>
				<td>No. of wrong answers: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntNotCorrect)" />
				</td>
			</tr>
			<tr>
				<td>No. of questions attempted: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntAttempted)" />
				</td>
			</tr>
			<tr>
				<td>No. of questions not attempted:  </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntNotAttempted)" />
				</td>
			</tr>
			<tr>
				<td>No. of questions presented: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@IntPresented)" />
				</td>
			</tr>
			<!--tr><td><xsl:value-of select="$algorithm"/></td></tr-->
			<xsl:choose>
				<xsl:when test="$algorithm='NumberCorrect' or 
                                          $ algorithm='WeightedNumberCorrect' or 
                                          $algorithm='ParameterWeightedNumberCorrect'">
					<tr>
						<td>Count normalised: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngCountNormalised,'%')" />
						</td>
					</tr>
				</xsl:when>
				<xsl:when test="$algorithm='NumberCorrectAttempted' or
                                         $algorithm='WeightedNumberCorrectAttempted' or
                                         $algorithm='ParameterWeightedNumberCorrectAttempted'">
					<tr>
						<td>Count normalised: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngCountNormalised,'%')" />
						</td>
					</tr>
					<tr>
						<td>Count normalised for questions attempted: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngCountNormalisedAttempted,'%')" />
						</td>
					</tr>
				</xsl:when>
				<xsl:when test="$algorithm='SumofScores' or
                                         $algorithm='ParameterWeightedSumofScores' or
                                         $algorithm='WeightedSumofScores'">
					<tr>
						<td>Minimum score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngMinScore)" />
						</td>
					</tr>
					<tr>
						<td>Maximum score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngTotalScore)" />
						</td>
					</tr>
					<tr>
						<td>Actual score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngActualScore)" />
						</td>
					</tr>
					<tr>
						<td>Percentage: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngSumNormalisedTotal,'%')" />
						</td>
					</tr>
					<tr>
						<td>Threshold percentage to pass: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@ThresholdScoreToPass,'%')" />
						</td>
					</tr>
				</xsl:when>
				<xsl:when test="$algorithm='SumofScoresAttempted'  or
                                         $algorithm='ParameterWeightedSumofScoresAttempted' or
                                         $algorithm='WeightedSumofScoresAttempted'">
					<tr>
						<td>Minimum score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngMinScore)" />
						</td>
					</tr>
					<tr>
						<td>Maximum score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngTotalScore)" />
						</td>
					</tr>
					<tr>
						<td>Actual score: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngActualScore)" />
						</td>
					</tr>
					<tr>
						<td>Score attempted: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngScoreAttempted)" />
						</td>
					</tr>
					<tr>
						<td>Percentage: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngSumNormalisedTotal,'%')" />
						</td>
					</tr>
					<tr>
						<td>Percentage score for questions attempted:  </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@SngSumNormalisedAttempted,'%')" />
						</td>
					</tr>
					<tr>
						<td>Threshold percentage to pass: </td>
						<td align="right">
							<xsl:value-of select="concat($dblSpace,@ThresholdScoreToPass,'%')" />
						</td>
					</tr>
				</xsl:when>
				<xsl:when test="$algorithm='BestKfromN'" />
				<xsl:when test="$algorithm='GuessingPenalty'" />
			</xsl:choose>
			<tr>
				<td>Assessment outcome: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@StrAssessmentResult)" />
				</td>
			</tr>
			<tr>
				<td>Grade: </td>
				<td align="right">
					<xsl:value-of select="concat($dblSpace,@StrGrade)" />
				</td>
			</tr>
			<xsl:if test="@EssayCount!=0">
			  <tr>			   
			    <td colspan="2">
			      You have attempted <xsl:value-of select="@EssayCount"/> Essay(s). <br />
			      The result summary displayed is excluding these questions, which will be evaluated by
			      the tutor later and the result will change accordingly.				    
			    </td>
		    </tr>
			</xsl:if>		
		</table>
	</xsl:template>
	<!-- general templates for feedback -->
	<xsl:template name="showScoreAndAnswer">
		<xsl:variable name="scoreStyle">
			<xsl:call-template name="getScoreStyle"/>
		</xsl:variable>
		<tr style="{$scoreStyle}">
			<xsl:apply-templates mode="Score" select="user_feedback" />			
		</tr>
		<xsl:if test="itemmetadata/qmd_itemtype!=$essay and $showCorrectAnswer=2">
			<tr style="{$scoreStyle}">
				<xsl:apply-templates select="user_feedback" mode="CorrectAnswer" />
			</tr>
		</xsl:if>
	</xsl:template>
	
	<xsl:template name="GetStyle">
	    <xsl:variable name="fontSize">
			  <xsl:call-template name="getFont">
				  <!--xsl:with-param name="size" select="key('font', 'scoresize')" /-->
				  <xsl:with-param name="size" select="@size" />
			  </xsl:call-template>
		  </xsl:variable>
		  <xsl:value-of select="concat('font: ', @face, ';font-size: ', $fontSize, ';color: ',@color)" />
	</xsl:template>
	
	<xsl:template name="getScoreStyle">
	  <xsl:for-each select="/ClientSidePresentation/template/font/score">
	      <xsl:call-template name="GetStyle"/>
		</xsl:for-each>
	</xsl:template>
	
	<xsl:template name="getHintStyle">
	  <xsl:for-each select="/ClientSidePresentation/template/font/hints">
		  <xsl:call-template name="GetStyle"/>
		</xsl:for-each>
	</xsl:template>
	
	<xsl:template name="getFeedbackStyle">
	  <xsl:for-each select="/ClientSidePresentation/template/font/feedback">
		<xsl:call-template name="GetStyle"/>
		</xsl:for-each>
	</xsl:template>	
	
	<xsl:template mode="CorrectAnswer" match="user_feedback">
    <xsl:variable name="isCorrectAnswerAvalible">
			<xsl:apply-templates select="../itemmetadata/qmd_itemtype" mode="IsCorrectAnswerAvalible" />
	</xsl:variable>        	
    <xsl:if test="$isCorrectAnswerAvalible='false'">
			<td style="font-weight:  bold" valign="top">Answer(s):   </td>
			<td>
				<xsl:for-each select="correct_answer/answer[.!='']">
					<xsl:value-of disable-output-escaping="yes" select="." />
					<xsl:choose>
						<xsl:when test="position()=last() - 1">
							<xsl:value-of select="'   and   '" />
						</xsl:when>
						<xsl:when test="position()!=last()">
							<xsl:value-of select="',  '" />
						</xsl:when>
					</xsl:choose>
				</xsl:for-each>
			</td>
		</xsl:if>
  </xsl:template>
	<xsl:template mode="IsCorrectAnswerAvalible" match="qmd_itemtype">
		<xsl:value-of select=".=$slider or .=$multipleChoiceHotSpot or .=$multipleResponseHotSpot 
                                           or .=$dragAndDrop or .=$connectPoints or .=$essay" />		
	</xsl:template>
	<xsl:template mode="Score" match="user_feedback">
		<td style="font-weight:  bold" valign="top">Score:  </td>
		<td>
			<xsl:value-of select="concat(score/@scoredmarks,' out of ',score/@maxmarks)" />
		</td>
	</xsl:template>
	<xsl:template mode="FeedBack" match="user_feedback">
		<xsl:variable name="finalFeedback">
			<xsl:for-each select="display_feedback">
				<!--xsl:value-of select=""/-->
				<xsl:variable select="@linkrefid" name="linkRefID" />
				<xsl:call-template name="display">
					<xsl:with-param name="displayBuf" select="../../itemfeedback[@ident=$linkRefID]/flow_mat/material" />
				</xsl:call-template>
			</xsl:for-each>
		</xsl:variable>
		<td style="font-weight:  bold" valign="top">Feedback:  </td>
		<xsl:choose>
			<xsl:when test="$finalFeedback=''">
				<td>No feedback</td>
			</xsl:when>
			<xsl:otherwise>
				<td>
					<xsl:value-of disable-output-escaping="yes" select="$finalFeedback" />
				</td>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<xsl:template name="display">
		<xsl:param name="displayBuf" />
		<xsl:if test="$displayBuf!=''">
			<xsl:choose>
				<xsl:when test="position()=last()-1">
					<xsl:value-of select="concat($displayBuf,'   and   ')" />
				</xsl:when>
				<xsl:when test="position()=last()">
					<xsl:value-of select="$displayBuf" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="concat($displayBuf,',  ')" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>	
	<!--/////////////////////////////////////To get outer template/////////////////////////////////////-->
	<xsl:template name="OuterLayout">
	<xsl:for-each select="/*/template/images">
	<table width="100%" border="0" cellpadding="0" cellspacing="0" > <!--begginning of outer table-->	
			<tr>
				<td colspan="3" bgcolor="{top/@bkcolor}">
				<xsl:variable name="src" select="top/@src"/>				
				<xsl:choose>
					<xsl:when test="$src!=''">
						<img src="{$src}"/>
					</xsl:when>	
					<xsl:otherwise><xsl:value-of disable-output-escaping="yes" select="'&amp;nbsp;&amp;nbsp;'"/></xsl:otherwise>
				</xsl:choose>
				</td>
			</tr>
			<tr>
				<td width="34" bgcolor="{left/@bkcolor}">
					<xsl:variable name="src1" select="left/@src"/>
					<xsl:choose>
						<xsl:when test="$src1!=''">
							<img src="{$src1}"/>
						</xsl:when>	
						<xsl:otherwise><xsl:value-of disable-output-escaping="yes" select="'&amp;nbsp;&amp;nbsp;'"/></xsl:otherwise>
					</xsl:choose>
				</td>
				<td width="100%" align="center">
					<br /> <!--begginning of outer td-->
						<xsl:apply-templates select="/*/questestinterop" mode="this"/>
					</td> <!--end of ouer td-->
				<td width="34" bgcolor="{right/@bkcolor}">
						<xsl:variable name="src2" select="right/@src"/>
						<xsl:choose>
							<xsl:when test="$src2!=''">
								<img src="{$src2}"/>
							</xsl:when>	
							<xsl:otherwise><xsl:value-of disable-output-escaping="yes" select="'&amp;nbsp;&amp;nbsp;'"/></xsl:otherwise>
						</xsl:choose>		
				</td>
			</tr>
			<tr>
			<td colspan="3" bgcolor="{bottom/@bkcolor}">
				<xsl:variable name="src3" select="bottom/@src"/>				
				<xsl:choose>
					<xsl:when test="$src3!=''">
						<img src="{$src3}"/>
					</xsl:when>	
					<xsl:otherwise><xsl:value-of disable-output-escaping="yes" select="'&amp;nbsp;&amp;nbsp;'"/></xsl:otherwise>
				</xsl:choose>	
			</td>
			</tr>
		</table> <!-- end of outer table-->					
	</xsl:for-each>	
	</xsl:template>
	<xsl:template name="GetBodyStyle">
				<xsl:for-each select="/*/template/images">
			bod.bgColor = "<xsl:value-of select="background/@bkcolor"/>";				
			bod.background = "<xsl:value-of select="background/@src"/>";		
			</xsl:for-each>
  </xsl:template>	
  <xsl:template name="showSummary">
    <div align="center" >
		  <span id="summaryTextHolder" class="timerStyle" title="Show summary of assessment results (ALT + S)" style="cursor:hand" onmouseover="changeFontColor(this,'{$genOverColor}')" onmouseout="changeFontColor(this,'{$genColor}')" onclick="doSummary(this)">Show <u>s</u>ummary >></span>
		</div>
		<div style="display: none;background-color: {$genLightColor}" id="summaryHolder">
		  <xsl:apply-templates mode="showAssessmentResults" select="ParticipantAssessmentResult">
			  <xsl:with-param select="section/outcomes_processing/@scoremodel" name="algorithm" />
		  </xsl:apply-templates>
		</div>
  </xsl:template>
  <xsl:template name="showHints">
  <xsl:variable name="hintContent">
    <xsl:apply-templates mode="GetHints" select="itemfeedback[@ident='Hints']/hint" />
  </xsl:variable>  
  <xsl:if test="$hintContent!=''">
      <p>
	      <input type="hidden" name="hintCount{@ident}" value="0" />      		  
        <table border="0" cellpadding="0" cellspacing="0">
            <tr>
              <td align="left"  valign="top" style="padding-right: 20px">
                <!--span id="hintLink" hintText="Hint" style="cursor:hand;color: blue; text-decoration: underline" onclick="javascript:showHint('{@ident}',this)" /-->                
                <div  id="hintLink" onclick="javascript:showHint('{@ident}',this)" class="buttonText" style="text-align: center">
                <img src="{$skinPath}/hints.gif"/>
                <br /><u>H</u>ints
                </div>
              </td>
              <td align="left">              
                <!--div id="hints_{@ident}" style="OVERFLOW: auto;height:70;color: {key('font', 'hintscolor')};FONT-SIZE: {$size}; FONT-FAMILY: {key('font', 'hintsface')}"-->
                <div id="hints_{@ident}" >
                  <xsl:attribute name="style">OVERFLOW: auto;height:70<xsl:call-template name="getHintStyle"/></xsl:attribute>         
                  <xsl:copy-of select="$hintContent"  />
                </div>
              </td>
            </tr>
          </table>
      </p>
   </xsl:if>
  </xsl:template>
</xsl:stylesheet>  