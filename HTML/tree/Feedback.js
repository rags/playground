// JScript source code
//AMSPS
/*
Author: Raghunandan R.
Module: Feedback.js
For setting user answers
*/
function setApplets()
{
  with(document.applets)
  {	
    for(i=0;i<length;i++)
    {
      try
      {
        var name = item(i).id;        
        var index = name.indexOf('_');
        if(name.substring(0,index)!="APPLET") continue;        
        var setVal = document.forms[0].item(name.substring(index+1)).value;        
        if((setVal!=null) && (setVal!=""))   item(i).setParams(setVal);
       }catch(ex){} 
    }
  }
}
function endtest()
{     
 switch(hdnMode.value)
	{
		case "pAfterFeedback":  window.close();
		default:
						window.location.href="frmInstructions.aspx?P1="+hdnScheduleDetailID.value +"&P2="+
															hdnAssessmentID.value +"&msg=a&mode=" + hdnMode.value + 
															"&AF=" + hdnAllowToSendAssessmentFeedback.value+"&QF="+
															hdnAllowToSendQuestionFeedback.value ;
	}				
}

function doSummary(ele)
{
	var summaryStyle = summaryHolder.style;				
	if(summaryStyle.display=="none")
	{
		summaryStyle.display = "block";
		ele.innerHTML= "&lt;&lt; Hide <u>s</u>ummary";				 
		ele.title = "Hide summary"
		return;
	}
	summaryStyle.display = "none";
	ele.innerHTML = "Show <u>s</u>ummary >>";				
	ele.title = "Show summary of assessment results"
}