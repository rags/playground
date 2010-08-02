<DIV class="yToolbar" id="FormatToolbar" style="WIDTH: 300px">
											<DIV class="TBHandle">
											</DIV>
											<DIV language="javascript" class="Btn" title="Bold" onclick="format('bold');">
												<IMG class="Ico" src="/AMS/images/bold.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Italic" onclick="format('italic')">
												<IMG class="Ico" src="/AMS/images/italic.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Underline" onclick="format('underline')">
												<IMG class="Ico" src="/AMS/images/under.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Foreground Color" onclick="foreColor()">
												<IMG class="Ico" src="/AMS/images/tpaint.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Background Color" onclick="backColor()">
												<IMG class="Ico" src="/AMS/images/parea.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Align Left" onclick="format('justifyleft')" NAME="Justify">
												<IMG class="Ico" src="/AMS/images/aleft.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Center" onclick="format('justifycenter')" NAME="Justify">
												<IMG class="Ico" src="/AMS/images/center.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Align Right" onclick="format('justifyright')" NAME="Justify">
												<IMG class="Ico" src="/AMS/images/aright.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Numbered List" onclick="format('insertorderedlist')">
												<IMG class="Ico" src="/AMS/images/nlist.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Bulletted List" onclick="format('insertunorderedlist')">
												<IMG class="Ico" src="/AMS/images/blist.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Decrease Indent" onclick="format('outdent')">
												<IMG class="Ico" src="/AMS/images/ileft.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Increase Indent" onclick="format('indent')">
												<IMG class="Ico" src="/AMS/images/iright.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Insert Table" onclick="InsertTable()">
												<IMG class="Ico" src="/AMS/images/table.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Create Hyperlink" onclick="createLink()">
												<IMG class="Ico" src="/AMS/images/wlink.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
											<DIV class="TBGen" id="EditMode" title="Editing Mode" style="VISIBILITY: visible">
												<INPUT language="javascript" onclick="setMode(switchMode.checked)" type="checkbox" name="switchMode">View 
												HTML source
											</DIV>
										</DIV>
										<DIV class="yToolbar" id="ParaToolbar" style="WIDTH: 300px">
											<DIV class="TBHandle">
											</DIV>
											<SELECT language="javascript" class="TBGen" id="ParagraphStyle" title="Paragraph Format" onchange="format('formatBlock',this[this.selectedIndex].value);this.selectedIndex=0">
												<OPTION class="heading" selected>
												Paragraph<OPTION value="Normal">Normal<OPTION value="Heading 1">Heading 1 
												&lt;H1&gt;<OPTION value="Heading 2">Heading 2 &lt;H2&gt;<OPTION value="Heading 3">Heading 
												3 &lt;H3&gt;<OPTION value="Heading 4">Heading 4 &lt;H4&gt;<OPTION value="Heading 5">Heading 
												5 &lt;H5&gt;<OPTION value="Heading 6">Heading 6 &lt;H6&gt;<OPTION value="Address">Address 
												&lt;ADDR&gt;<OPTION value="Formatted">Formatted &lt;PRE&gt;<OPTION style="COLOR: darkred" value="removeFormat">Remove 
													Formatting</OPTION></SELECT><SELECT language="javascript" class="TBGen" id="FontName" title="Font Name" onchange="format('fontname',this[this.selectedIndex].value);this.selectedIndex=0">
												<OPTION class="heading" selected>
												Font<OPTION value="Arial">Arial<OPTION value="Arial Black">Arial Black<OPTION value="Arial Narrow">Arial 
												Narrow<OPTION value="Comic Sans MS">Comic Sans MS<OPTION value="Courier New">Courier 
												New<OPTION value="System">System<OPTION value="Times New Roman">Times New Roman<OPTION value="Verdana">Verdana<OPTION value="Wingdings">Wingdings</OPTION></SELECT><SELECT language="javascript" class="TBGen" id="FontSize" title="Font Size" onchange="format('fontsize',this[this.selectedIndex].value);this.selectedIndex=0">
												<OPTION class="heading" selected>
												Size<OPTION value="1">1<OPTION value="2">2<OPTION value="3">3<OPTION value="4">4<OPTION value="5">5<OPTION value="6">6<OPTION value="7">7</OPTION></SELECT>
											<DIV class="TBSep">
											</DIV>
											<DIV language="javascript" class="Btn" title="Cut" onclick="format('cut')">
												<IMG class="Ico" src="/AMS/images/cut.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Copy" onclick="format('copy')">
												<IMG class="Ico" src="/AMS/images/copy.gif">
											</DIV>
											<DIV language="javascript" class="Btn" title="Paste" onclick="format('paste')">
												<IMG class="Ico" src="/AMS/images/paste.gif">
											</DIV>
											<DIV class="TBSep">
											</DIV>
										</DIV>
										<IFRAME class="Composition" id="Composition" style="zorder: 10001" width="650" height="100">
										</IFRAME><INPUT type="hidden" name="hidvar"><input type="hidden" id="hdnreturnObject" name="hdnReturnObject">
										<SCRIPT>
		<!--
			Composition.document.open();
alert(bodyTag);
			Composition.document.write(bodyTag);
			Composition.document.close();
			Composition.document.designMode="On";
		// -->
		</SCRIPT>
		<SCRIPT language="Javascript" src="compose.js"></SCRIPT>
		