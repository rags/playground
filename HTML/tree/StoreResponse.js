/*
Author: Raghunandan R.
Module: Navigation.js
For storing answers for assessment questions on the client side
*/
function storePageResponse(pageNO)  
{
  if(pageNO<1 || pageNO>noOfPages) return;
  for(var i = (pageNO - 1) * questionsPerPage ; i < pageNO*questionsPerPage   && i<questionArr.length;i++)   storeResponse(questionArr[i]);  
}

function storeResponse(questionEle)
{
  var id = questionEle.id.substring(1);  
  var ansFlagHolder = frmQuestion("isAnswered_" + id);    
  switch(questionEle.questionType)
  {
    case 'Connect the Points':
    case 'Slider':
    case 'HotSpot - Multiple Response':
    case 'HotSpot - Multiple Choice':
    case 'Drag and Drop':
             frmQuestion(id).value = frmQuestion("APPLET_" + id).getParams();              
   case 'Essay':
   case 'Text Match':
   case  'Numeric':
   case 'Macromedia Flash':
            ansFlagHolder.value = (frmQuestion(id).value!='')? 1:0;
            return;             
    case 'Multiple Choice Dynamic': 
    case 'Multiple Choice Static':
    case 'Likert Scale':
    case 'True / False':             
    case 'Multiple Response Static':
    case 'Multiple Response Dynamic':
    case 'Matrix':             
             var inputsArr = questionEle.getElementsByTagName('INPUT');                                       
             var i;
             for(i=0; i<inputsArr.length;i++)  if(inputsArr[i].checked && inputsArr[i].question)break;
             ansFlagHolder.value =( i<inputsArr.length)? 1:0;
             return;
    case 'Java Applet': 
              var JAHolder = questionEle.all["__APPLET_HOLDER"]
              try
              {
                frmQuestion(id).value = eval("JAHolder.firstChild." + JAHolder.fn);	   	                   
                ansFlagHolder.value = (frmQuestion(id).value!='')? 1:0;
               }
               catch(ex)
               {
                doPopUpMessage("A Java Applet question doesnt exist. It will be marked as unattempted");
                ansFlagHolder.value = 1;
               }              
             return;
   case 'Matching':
   case 'Pull Down List':
   case 'Ranking':
   case 'Select a blank' :
            var combos = questionEle.getElementsByTagName("SELECT"); 
            ansFlagHolder.value = checkChoiceValues(combos);
            return;
   case 'Entry List Static':
   case 'Entry List Dynamic':
   case  'Fill In Blanks Static':
   case  'Fill In Blanks Dynamic':   
             var varInputs = questionEle.getElementsByTagName("INPUT");             
             ansFlagHolder.value = checkChoiceValues(varInputs);
             return;   
  }
}

function checkChoiceValues(ChoiceArr)
{
  var i;
  for(i=0; i<ChoiceArr.length;i++) if(ChoiceArr[i].value!='' && ChoiceArr[i].question) break;
  return ( i<ChoiceArr.length)? 1:0;            
}


////////////////////////////////Flash related stuff//////////////////////////////////////
function QM_setInfo(choiceID, command, args) //to retrive values
{
	command = String(command);
	switch (command)
	{
		case "MM_cmiSendInteractionInfo":
		args = String(args);
		var F_intData = args.split(";");
		var result = F_intData[7]; 
		frmQuestion.elements(choiceID).value=result;
		frmQuestion.elements("isAnswered_" + choiceID).value="1";
	 }
}
function checkFlashFiles() //scripts  for all flash type questions
{
var objects = document.getElementsByName("__AMS_FlashObj");     
for(var i=0;i<objects.length;i++)
	document.write(	
								"\<SCRIPT LANGUAGE=\"VBScript\"\>\non error resume next\n" +
								"Sub " + objects[i].id + "_FSCommand(ByVal command, ByVal args)\n" +
								"call QM_setInfo(\"" +objects[i].idref + "\",command, args)\nend sub\n" +
								"\</SCRIPT\>"
							);
}
//////////////////////////////////////////End of flash related stuff//////////////////////////////////////

function isAnswered(id)
{
  return (frmQuestion("isAnswered_" + id).value=="1");
}

function checkType(type,element)
{  
  var code = event.keyCode;
  var val =element.value;
  switch(type)
  {
      case "String":               return true;
      case "Decimal":           if((code==43 || code==45) && val=="") return true;
                                              if(val.indexOf(".") < 0 && code==46) return true;
                                              if((code <58 && code >47)) return true;		       
                                              return false;
  }
}

function doSubmit()
{
	//storeAppletResponse();   
	storePageResponse(curPage);
	if(hdnTimeUp.value=="1")
	{  
	  submitForm();
	  return;
	 }	    
	if(!isTestComplete())
	{
		if(/*!boolAllowSkip || */hdnAnswerAll.value=="true")
		{			
			doPopUpMessage("All the questions should be answered to submit test / assessment");		
			return;
		}
		confirmSubmit("All questions are not answered.<br>Do you want to submit the test for evaluation?");
		return;
		//if(!confirm("All questions are not answered.\nDo you want to submit the test for evaluation?")) return false; //remove
	}  	
	confirmSubmit("<br>Are you sure you want to submit the assessment for evaluation?"); 
}

function submitForm()
{  
  setFormValues();  
  clearTimeout(timerID);
  //document.getElementById("Proceed").disabled = true;
  document.getElementById("Proceed").style.visibility = "hidden";
  boolSubmitClick = true;
  frmQuestion.submit();  
  doPopUpMessage("Assessment is being evaluated.This may take sometime.<br>Please wait...");
}

function setFormValues()
{  
  frmQuestion.appendChild(hdnScheduleDetailID);
  frmQuestion.appendChild(hdnAssessmentID);
  frmQuestion.appendChild(hdnSendMailAfterTest);
  frmQuestion.appendChild(hdnShowCorrectAnswer);
  frmQuestion.appendChild(hdnShowNavLinks);
  frmQuestion.appendChild(hdnQuestionsPerPage);
  frmQuestion.appendChild(hdnMode);
  frmQuestion.appendChild(hdnAllowToSendAssessmentFeedback);
  frmQuestion.appendChild(hdnAllowToSendQuestionFeedback);
  frmQuestion.appendChild(xslContent);
  frmQuestion.appendChild(hdnAllowFeedback);
  frmQuestion.appendChild(hdnParticipantID);
  frmQuestion.appendChild(hdnRestartFromLastStep);  
  frmQuestion.appendChild(hdnViewState);       
}

var confirmDialog;
function confirmSubmit(msg)
{
	var btnStyle = "color: "+popUpBackColor+";background-color: "+popUpFontColor+";border: none;cursor: hand";
	var inputParts = new Array("<input type="," id="," value="," onclick="," style="," />");
	var html= inputParts[0] + "hidden" + inputParts[1] +"response" + inputParts[5];				 
	html += inputParts[0] + "button" + inputParts[1] +"btnTrue" + inputParts[2] + "Yes"+ inputParts[3] + "'parent.submitForm()'"+inputParts[4]  + "'" + btnStyle + "'" + inputParts[5] + "&nbsp;&nbsp;" ;
	html += inputParts[0] + "button" + inputParts[4]  + "'" + btnStyle+ "'" +  inputParts[1] +"btnFalse" + inputParts[2] +"' No '"+ inputParts[3] + "'parent.confirmDialog.hide()'" +inputParts[5];				 	 				
	var msg = "<div align=center vlaign=middle height=100>" + msg + "<br><br>"+html+"</div>";    								
	confirmDialog  = doPopUp(msg,380,100,popUpFontColor,popUpBackColor)
}

function updatePageResponse(pageNO)
{  
   var userResponseXML = "<UserResponses " +
                                                 ( (boolQuestionLevelTimer)?"":("time_taken='" + frmQuestion("hdnTimeTaken").value+"'")  )+
                                                   ">";
   for(var i = (pageNO - 1) * questionsPerPage ; i < pageNO*questionsPerPage   && i<questionArr.length;i++)
    {
      var qid  = questionArr[i].id.substring(1);            
      userResponseXML += "<UserResponse qid=\"" + qid + "\"  " + 
                                                ((boolQuestionLevelTimer)?("time_taken='" + frmQuestion("hdnTimeTaken_" + qid).value+"'") : ''  )+
                                                 ">";
      switch(questionArr[i].questionType)
      {
        case  'True / False': //7
        case  'Likert Scale':
        case  'Multiple Choice Static':
        case  'Multiple Choice Dynamic':
        case  'Multiple Response Static':
        case  'Multiple Response Dynamic':
        case  'Matrix':                              
                 var choiceArr = questionArr[i].getElementsByTagName('INPUT');                                                         
                 for(var j=0;j<choiceArr.length;j++) 
                       if(choiceArr[j].checked && choiceArr[j].question)
                       {
                         //response = choiceArr[j].value;
                         //response = response.substring(response.lastIndexOf(":") + 1);
                         cid = choiceArr[j].name;
                         userResponseXML += "<Response cid=\"" + cid.substring(cid.lastIndexOf("$") + 1)  +  "\"><![CDATA["+  choiceArr[j].value +"]]></Response>";
                       }
                 break;
        case 'Connect the Points':        //2
        case 'HotSpot - Multiple Response':
                 var choiceArr = frmQuestion(qid).value.split(";"); 
                 for(var j=0;j<choiceArr.length-1;j++) userResponseXML += "<Response cid=''><![CDATA["+  choiceArr[j] +"]]></Response>";
                 break;
        case 'Drag and Drop':                      //1                                                
                 var choiceArr = frmQuestion(qid).value.split(";"); 
                 for(var j=0;j<choiceArr.length-1;j++) 
                 {
                  var ind = choiceArr[j].indexOf(",");
                  userResponseXML += "<Response cid=\"" + choiceArr[j].substring(0,ind)+  "\"><![CDATA["+  choiceArr[j].substr(ind+1) +"]]></Response>";
                 }
                 break;        
        case 'HotSpot - Multiple Choice': //7
        case 'Essay':
        case 'Text Match':
        case 'Numeric':
        case 'Macromedia Flash':
        case 'Java Applet': 
        case 'Slider':
                 var response = frmQuestion(qid).value;                 
                 if(response != "") userResponseXML += "<Response cid=''><![CDATA[" + htmlEncode(response)  + "]]></Response>";
                 break;      
        case 'Matching': //4
        case 'Pull Down List':
        case 'Ranking':
        case 'Select a blank' :
                  var combos = questionArr[i].getElementsByTagName("SELECT"); 
                   for(var j=0; j<combos.length;j++)  
                   {
                       var response = combos[j].value;
                       if(response=="" || !(combos[j].question)) continue;
                       var index = response.indexOf(":");
                       var cid = response.substring(0,index);
                       response = response.substring(index + 1);                       
                       userResponseXML += "<Response cid=\"" + cid +  "\"><![CDATA[" +  response + "]]></Response>";          
                   }                           
                  break;
        case 'Entry List Static': //4
        case 'Entry List Dynamic':
        case  'Fill In Blanks Static':
        case  'Fill In Blanks Dynamic':    
                  var varInputs = questionArr[i].getElementsByTagName("INPUT");             
                   for(var j=0; j<varInputs.length;j++)  
                   {
                       var response = varInputs[j].value;
                       if(response=="" || !(varInputs[j].question)) continue;                       
                       var cid = varInputs[j].name;
                       cid = cid.substr(cid.indexOf("$") + 1);
                       userResponseXML += "<Response cid=\"" +  cid +  "\"><![CDATA["+  htmlEncode(response) +"]]></Response>";          
                   }                       
                  break;                                   
      }      
      userResponseXML += "</UserResponse>"; 
    }        
  userResponseXML += "</UserResponses>";  
  //if(userResponseXML.indexOf("</Response>")==-1) return; s  
  var tempXMLDoc  = new ActiveXObject("msxml2.domdocument");
  tempXMLDoc.load("/AMSWS/CWSParticipant.asmx/storeState?userResponse="+userResponseXML +"&intScheduleDetailID=" + hdnScheduleDetailID.value);  
}

function htmlEncode(str) //is there a builtin fn for this????????
{ 
  str =  str.replace(/&/g,"&amp;");
  str =  str.replace(/"/g,"&quot;");
  str =  str.replace(new RegExp("<","g"),"&lt;");
  str =  str.replace(new RegExp(">","g"),"&gt;");
  return escape(str);
}