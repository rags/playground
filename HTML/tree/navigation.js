/*
Author: Raghunandan R.
Module: Navigation.js
For navigating through assessment questions and feedback on the client side
*/
      var noOfPages,questionsPerPage,curPage=0;
      var questionArr,mode;
      var imgWidth,imgHeight;
      var eventMOver =1,eventMOut=2,eventMClick=3;//,eventFlagged=4;
      var imgMOver,imgMOut,imgMClick ,imgFlag,imgMClickFlag,linkColorMOver,linkColorMClick,linkColorMOut,linkColorFlag;
      var flagTxtHolder;              
      var boolNavLinks,boolAllowSkip,boolQuestionLevelTimer,boolShowHints,boolSaveState;
      var boolSubmitClick;
       function initialize()
      {
       boolQuestionLevelTimer = false;            
       setMode(hdnMode.value);		       
       switch(mode)
       {
         case "test":                          boolAllowSkip  = allowSkip.value=="true";              
											                                 boolShowHints = hintsFlag.value=='true'; 											                                 
											                                 checkFlashFiles();	
											                                 switch(enforceTime.value)
                                                        {
                                                          case "3": break;
                                                          case "1": initializeTimer();
                                                                          startTimer(frmQuestion.hdnTimeTaken);
                                                                          break;
                                                          case "2": initializeTimer();                 
                                                                          boolQuestionLevelTimer = true;
                                                                          break;
                                                        }
                                                        boolSubmitClick = false;
                                                        if(boolSaveState=hdnRestartFromLastStep.value=="True") setApplets();
                                                        break;
         case "clientFeedback":      setApplets();
                                                        boolSubmitClick = true;
                                                        break;	   
       }          
	     loadTestQuestions();              	  	 	     
      }
      
      function loadTestQuestions()
      {       
       questionsPerPage = hdnQuestionsPerPage.value;                
        var divArr = frmQuestion.getElementsByTagName("DIV");        
        questionArr = new Array();
        var j=0;        
        for(var i=0;i<divArr.length;i++)  
            if(divArr[i].getAttribute("type")=="Question") questionArr[j++] = divArr[i];                 
        var noOfQuestions = questionArr.length;                
        noOfPages = getNOOfPages(noOfQuestions,questionsPerPage);                        
        boolNavLinks = hdnShowNavLinks.value=="1";
        if(boolNavLinks)
        {		
		        imgMOver  =  links.imgMOver;
		        imgMOut    =  links.imgMOut;    
		        imgMClick  =  links.imgMClick;  
		        imgFlag        =  links.imgFlag;
		        imgMClickFlag = links.imgMClickFlag || imgFlag;
		        linkColorMOver = links.linkColorMOver;
		        linkColorMOut = links.linkColorMOut;
		        linkColorMClick = links.linkColorMClick; 		
		        linkColorFlag = links.linkColorFlag;
        }    
        //if(canLoadPage(1)) 
        showPage(1);
        checkPage();
      }      
      function showHint(id,hintsLink)
      {
          showHints(
                                  document.getElementById("hints_" + id),
                                  document.getElementById("hintCount" + id),
                                  hintsLink                      
                               );
      }
      function showHints(hintsHolder,hdnNoOfHintsDisplayed,hintsLink)
      {
         var noOfHintsDisplayed;
         try{
                    noOfHintsDisplayed= parseInt(hdnNoOfHintsDisplayed.value);
               }
         catch(exception)
              {
                  noOfHintsDisplayed = 0;
              }    
         hintsHolder.childNodes[noOfHintsDisplayed].style.visibility = "visible";
         setValue(hdnNoOfHintsDisplayed, ++noOfHintsDisplayed);
         hintsHolder.doScroll("scrollbarPageDown");
         //hintsLink.innerHTML = hintsLink.hintText + "  " + (noOfHintsDisplayed + 1);
         if(noOfHintsDisplayed>=hintsHolder.childNodes.length)
            with(hintsLink)
            {
                onclick="";
               // innerHTML = "No more hints";
                with(style)
                {
                  //textDecoration="none";
                  cursor="default";
                }
            }
      }
       
       function showHintLink(pageNO)
       {
          if(pageNO<1 || pageNO>noOfPages) return;
          for(var i = (pageNO - 1) * questionsPerPage ; i < pageNO*questionsPerPage   && i<questionArr.length;i++)//for every question in page
                  with(questionArr[i].all.item("hintLink"))
                    {
                      var hintsHolder = parentNode.nextSibling.firstChild;//take its div in sibling td
                      if(hintsHolder.hasChildNodes())
                        {    //try reading hidden var noofhintsdisplayed.... it'll be easier
                            var noOfChildren = hintsHolder.childNodes.length;
                            for(var k=0;k<noOfChildren;k++)
                                if(hintsHolder.childNodes[k].style.visibility=="hidden") break;                                
                            innerHTML = (k==noOfChildren)? "No more hints" :  hintText +" "+  (k+1);
                      } 
                      else
                        hintsHolder.style.display="none"; 
                    } 
           
       }
       
       function getNOOfPages(noOfQuestions,questionsPerPage)
       {
         return Math.floor( noOfQuestions / questionsPerPage ) + ( (noOfQuestions % questionsPerPage==0)? 0 : 1);
       }
       
       function showNextLoadablePage()
       {
	       var msg = "Time's up for question: <b>#" + curPage + "</b>";
	       doPopUpMessage(msg);
         for(var i=(curPage% noOfPages) + 1;i!=curPage;i=(i% noOfPages) + 1)
         {
           if(canLoadPage(i))
           {            
            if(boolNavLinks) resetNavLinkProperty(imgMOut,linkColorMOut);            
            showPage(i);
            checkPage();
            doPopUpMessage(msg);
            return true;
            }           
         }
         return false;
       }
       
       function showNext()
       {        
        if(!canLoadPage(curPage + 1)) return;        
        if(boolNavLinks) resetNavLinkProperty(imgMOut,linkColorMOut);
        showPage(curPage + 1);
        checkPage();        
       }
       
       function showPrev()
       {
        if(!canLoadPage(curPage - 1)) return;
        if(boolNavLinks) resetNavLinkProperty(imgMOut,linkColorMOut);
        showPage(curPage - 1);
        checkPage();
       }
       
      function showPage(pageNo)
      {
       /* if(mode=="test")
        {
          if(boolShowHints) 
          showHintLink(pageNo);                     
        } */         
        setDisplay(curPage,"none");                  
        setDisplay(pageNo,"block");          
        curPage = pageNo;               
        if(mode=="test")
        {            
            if(boolQuestionLevelTimer)  startTimer(frmQuestion("hdnTimeTaken_" + getCurQuestionID()));                
            if(boolNavLinks)
            {           
              var btnFlag = frmQuestion.btnFlag;              
              resetNavLinkProperty(imgMClick,linkColorMClick);          
              setFlagText();
            }           
          return; 
        }                  
        if(boolNavLinks) resetNavLinkProperty(imgMClick,linkColorMClick);           
      }
      
    function setDisplay(pageNO,attr)
    {
        if(pageNO<1 || pageNO>noOfPages) return;
        for(var i = (pageNO - 1) * questionsPerPage ; i < pageNO*questionsPerPage   && i<questionArr.length;i++)
        {
            questionArr[i].style.display=attr;
            if(mode=="test") setPresented(getQuestionID(i));          
        }
    }
    
    function checkPage()
    { 
      var prev = document.getElementById("prev");
      var next = document.getElementById("next");
      if(curPage==1)  prev.disabled = true;
      else                        prev.disabled = false;
      
      if(curPage==noOfPages)    next.disabled = true;
      else                                           next.disabled = false;
    }
    function changeFontColor(element,color)
    {
     if(element) element.style.color = color;
    }
    function changeBackColor(element,color)
    {
     if(element) element.style.backgroundColor  = color;
    }
    function  setBackImg(element,url)
    {
	    if(element) element.style.backgroundImage = "url(" + url + ")";
     }
     function changeImgSrc(element,url)
     {      
      if(element) element.src = url;      
     }
     function setValue(element, value)
	  {
	    if(element) element.value = value;	
	  }
	  function setInnerHTML(element, value)
	  {
	    if(element) element.innerHTML= value;	
	  }
             
    function handleLinkEvents(element, mouseEvent)
    {    
      switch(mouseEvent)
      {
        case eventMOver:     setBackImg(element,imgMOver);
                                               changeFontColor(element,linkColorMOver);
                                               break;
        case eventMOut:      
									 var pageNo = parseInt(element.innerText)
									 if(element.isFlagged=="1")
									 {
									 	changeFontColor(element,linkColorFlag);
									 	setBackImg(element,imgFlag);
									  }
                                              else if(pageNo==curPage)                                               
                                               {
                                                 changeFontColor(element,linkColorMClick);				
                                                 setBackImg(element,imgMClick);
                                                } 
                                              else  										
                                              //if(pageNo!=curPage && element.isFlagged!="1")//curPage != parseInt(element.innerText))
                                              {
                                                 setBackImg(element,imgMOut);                                                                   
                                                 changeFontColor(element,linkColorMOut);						                                              
                                               }   
                                              
                                               break;
                                               
        case eventMClick:   
                                              var nextPageNo = parseInt(element.innerText); 
                                              if(nextPageNo==curPage) return;
                                              changeFontColor(element,linkColorMClick);
                                              if(!canLoadPage(nextPageNo)) return;
                                              resetNavLinkProperty(imgMOut,linkColorMOut);                                         
                                              showPage(nextPageNo);
                                              checkPage();
                                              resetNavLinkProperty(imgMClick,linkColorMClick);       
                                                
        }
      }
      
 function canLoadPage(pageNO)
 {
  switch(mode)
  {
    case "test" :   
                                              storePageResponse(curPage);                                              
                                              if(!boolAllowSkip)
                                                for(var i=curPage;i< pageNO ;i++)
                                                    if(!isPageAnswered(i))
                                                    {
                                                      doPopUpMessage("Please answer all the questions in previous pages to goto this page");
                                                      return false ;
                                                    }                                              
                                                    
                                              if(boolQuestionLevelTimer && isTimeUp(pageNO))
                                              {
										                            doPopUpMessage("Time's up for question: <b>#" + pageNO + "</b>");
                                                return false;
                                              }                  
                                              //alert(boolSaveState);
                                              if(boolSaveState || boolQuestionLevelTimer) storeTimeTaken();//store time taken till noz
                                              if(boolSaveState) updatePageResponse(curPage)  
                                              return true;
                            
    case "clientFeedback": return true;
  }
 }
 
 function FlagUnFlag(btnFlag)
 {
    
    switch(getCurPageBackImg().isFlagged) 
    {
      case "0":             flagPage();
                                  setInnerHTML(flagTxtHolder,"Un<u>f</u>lag");                                  
                                  break;
      case "1":             UnflagPage();  
                                  setInnerHTML(flagTxtHolder,"<u>F</u>lag");
                                  break;
    }  
 }
 
 function setFlagText()
 {
   try
   {
   switch(getCurPageBackImg().isFlagged) 
    {
      case "1":             setInnerHTML(flagTxtHolder,"Un<u>f</u>lag");
                                  break;
      case "0":             setInnerHTML(flagTxtHolder,"<u>F</u>lag");
                                  break;
    }
    }catch(ex){}
 }
 
 function flagPage()
 {
   var element = getCurPageBackImg();
   element.isFlagged = "1";
   setBackImg(element, imgFlag);   
   changeFontColor(element,linkColorFlag);
 }
 
 function UnflagPage()
 {
   var element = getCurPageBackImg();
   element.isFlagged = "0";
   setBackImg(element, imgMClick);   
   changeFontColor(element,linkColorMClick);
 }
 
   function doFocus(element)
   {
      try{
              element.focus();
             }
      catch(ex){}       
   }
 
  function returnFalse(){return false;}
        
  function resetNavLinkProperty(img,color)
  {
      var element = getCurPageBackImg();
      if(element.isFlagged=="1")  return;  
      changeFontColor(element,color);
      setBackImg(element,img);                
  }
 
  function getCurPageBackImg()
  {
    return document.getElementById("navImg" + curPage);
  }
  
  function isPageAnswered(pageNO)
  { 
   if(pageNO<1 || pageNO>noOfPages) return;
   //storeAppletResponse();
   return checkIsAnswered(pageNO);
  }
  function getCurQuestionID()
  {
    return getQuestionID(curPage - 1);
  }
  function getQuestionID(index)
  {
    return questionArr[index].id.substring(1);
  }
  function checkIsAnswered(pageNO)
  {
    for(var i = (pageNO - 1) * questionsPerPage ; i < pageNO*questionsPerPage   && i<questionArr.length;i++)
      if(!isAnswered(getQuestionID(i))) return false; 
   return true;
  }	

  function isTestComplete()
  {
	for(var i=1;i<=noOfPages;i++)
		if(!checkIsAnswered(i))   return false;		
	return true;
  }  

  function setPresented(qid)
  {    
    setValue(frmQuestion("isPresented_"+qid),"Y");    
  }   
  /////////////////////////////////////Buzzer Scipt///////////////////////////////////////////////
    var  buzzerTime, minsRemaining, hrsRemaining, secsRemaining;
    var totalTimeMins, totalTimeSecs;
    var txtTimerField,hdnTimerField;
    var timerID;    
    function initializeTimer()
    {
      txtTimerField = frmQuestion.txtTimer;            
      buzzerTime = enableBuzzerBeforeTime.value;
    }
    
    function startTimer(hdnTimeTaken)
    {
      clearTimeout(timerID);      
      if(boolQuestionLevelTimer)  getTimeForQuestion(getCurQuestionID());      
      else 
      {
        totalTimeMins  = assessmentDuration.value;
        hrsRemaining = Math.floor(totalTimeMins/60);
	      minsRemaining = Math.floor(totalTimeMins%60);
	      totalTimeSecs = secsRemaining = 0;	    
	    }
	    hdnTimerField = 	hdnTimeTaken;
      var minsAlreadyTaken=0,secsAlreadyTaken=0,hrsAlreadyTaken=0;
      var  timeTaken = hdnTimerField.value;
      if(timeTaken!="")
      {
        var timeAlreadyTaken = timeTaken.split(":");      
        //timeAlreadyTaken[0] == >secsAlreadyTaken;  timeAlreadyTaken[1] ==> minsAlreadyTaken
        minsAlreadyTaken = parseInt(timeAlreadyTaken[0]), 
        secsAlreadyTaken= parseInt(timeAlreadyTaken[1]);      
        hrsAlreadyTaken = Math.floor(minsAlreadyTaken/60);
        minsAlreadyTaken %= 60;
      }
      deduct(hrsAlreadyTaken,minsAlreadyTaken,secsAlreadyTaken) 
      setValue(txtTimerField, formatTime(hrsRemaining, minsRemaining,secsRemaining));	   
      if(hrsRemaining==0 && minsRemaining==0 && secsRemaining==0) 
      { 
        doTimeUp();
        return;
      }
      timerID = setTimeout("doBuzzer()",1000);      
    }
    
    function deduct(hr,min,sec)
    {
     
      secsRemaining -= sec;
      if(secsRemaining<0)
      { 
        secsRemaining += 60;
        minsRemaining--;
      }
      minsRemaining -= min;
      if(minsRemaining<0)
      { 
        minsRemaining += 60;
        hrsRemaining--;
      }
      hrsRemaining -= hr;
      if(hrsRemaining<0)   alert("Fatal error: Contact Raghunandan R.");
    }
    function doBuzzer()
    {
      secsRemaining--;
      if(resetTimeRemaining())
      {
          setValue(txtTimerField, formatTime(hrsRemaining, minsRemaining,secsRemaining));	                             
          timerID = setTimeout("doBuzzer()",1000);
          if((minsRemaining + hrsRemaining*60)==buzzerTime && secsRemaining==0 && buzzerTime!=0)   
            showAlarm(20,"Time remaining: <b>" + formatTime(hrsRemaining, minsRemaining,0) + "</b>");                      
       }   
    }        
    
    function showAlarm(cnt,msg)
    {
     if(cnt<1)
     {      
       moveTo(0,0);
       doPopUpMessage(msg);
       return;
     }
     setTimeout("showAlarm("+ --cnt+ ",'" +msg+"')",50);
     doPopUpMessage(msg);
     if(cnt%2==0)      moveTo(1,1);
	   else                        moveTo(-1,-1);	
    }
    
    function resetTimeRemaining()
    {
      
      if(secsRemaining<0)
      {
        secsRemaining = 59;
        minsRemaining -= 1;
      }
      if(minsRemaining<0)
      {
        minsRemaining=59;
        hrsRemaining -=1;
      }
      if(hrsRemaining<0)
      {
       secsRemaining=minsRemaining=hrsRemaining=0 ;
       doTimeUp();            
       return false;
      }
      return true;
    }
    
    function doTimeUp()
    {
        storeTimeTaken();
        if(boolQuestionLevelTimer)
           if(showNextLoadablePage()) return;           
           else doPopUpMessage("<b>OOPS!:</b> time's up for all questions",3)
        else doPopUpMessage("<b>OOPS!:</b> time's up",3)
        setValue(hdnTimeUp, "1");
        doSubmit();
        return;
    }
    
    function formatTime(hr,min,sec)
    {
      return  ((hr>9)? hr : ("0" + hr) )+ ":" +
	                  ((min>9)? min: ("0" + min) )+ ":" + 
	                  ((sec>9)? sec: ("0" + sec) ) ;	                             
    }
    
    function doPopUpMessage(msg,msgTimeout)
    {
     var fontColor,backColor;
	    try
	    {
		      fontColor  = popUpFontColor;
          backColor = popUpBackColor;
      }
      catch(ex)
      {
         fontColor  = "black";
         backColor = "lightyellow";
      }
     if(msgTimeout)
     {
     var warnContent ="about:<head><title>Assessment Management System</title></head><body oncontextmenu='return false;' bgcolor="+backColor+"><font face=ariel size=2 color="+fontColor+">"+ msg+"</font></body>\<SCRIPT\>setTimeout('self.close();'," + (msgTimeout * 1000||2000) + ");\</SCRIPT\>"
     var features = "dialogWidth:" + 300 + "px; dialogHeight:" + 100 + "px; dialogTop: px; dialogLeft: px; center:yes; help:no; status:no; resizable:no;";
      window.showModalDialog(warnContent, 0, features);
      return;
      }
     doPopUp(msg,380,50,fontColor,backColor);     
    }
    
    function doPopUp(msg,width,height,fontColor,backColor)
    {
	   var oPopup = window.createPopup();
     var oPopBody = oPopup.document.body;    
     oPopup.document.oncontextmenu=returnFalse;
     oPopBody.style.backgroundColor = backColor;
     oPopBody.style.color =  fontColor;
     oPopBody.style.font="bold 14px Arial";     
     oPopBody.style.border = "solid black 1px";     
     oPopup.show(screen.availHeight/2 - height/2, screen.availWidth/2 - width/2, width, height, document.body);
     oPopBody.innerHTML = "<div align=center vlaign=middle height="+height+">" +msg+"</div>";    	     
     return oPopup;
    }
    
    function isTimeUp(pageNO)
    {     
      var totMins,totSecs;
      var hdnTotTime = frmQuestion("hdnTotalTime_" + getQuestionID(pageNO-1));
      var isoTime = hdnTotTime.value;      
      try
      {
        totSecs  =  parseInt(isoTime.substring(isoTime.lastIndexOf("M")+1,isoTime.lastIndexOf("S"))); 
        totMins = parseInt(isoTime.substring(isoTime.lastIndexOf("H")+1,isoTime.lastIndexOf("M")));
      }
      catch(ex)
      {
        totSecs  = 0;
        totMins = 1;
        hdnTotTime.value = "T0H1M0S";
      }
      var timeTakenAlready = frmQuestion("hdnTimeTaken_" + getQuestionID(pageNO - 1)).value.split(":");
      if(parseInt(timeTakenAlready[0])>=totMins && parseInt(timeTakenAlready[1])>=totSecs) return true;          
      return false;
    }
    
    function storeTimeTaken()
    {
      var totalMinsRemaining = minsRemaining + hrsRemaining * 60; 
      var timeTakenMins = (totalTimeMins - totalMinsRemaining)||0;      
      //var timeTakenSecs = 60 - (secsRemaining||0);
      //if(timeTakenSecs<60) timeTakenMins--;      
      var timeTakenSecs = totalTimeSecs - (secsRemaining||0);      
      if(timeTakenSecs < 0)
      {
        timeTakenMins--;
        timeTakenSecs +=60;
      }
      //else timeTakenSecs = 0;
      if(boolQuestionLevelTimer)
      {
        setValue(frmQuestion("hdnTimeTaken_" + getCurQuestionID()), timeTakenMins + ":" + timeTakenSecs);             
        return;
      }
      setValue(frmQuestion("hdnTimeTaken"), timeTakenMins + ":" + timeTakenSecs);     
    }
    
    function getTimeForQuestion(id)
    {
      var hdnTotalTime = frmQuestion("hdnTotalTime_" + id);
      var isoTime = hdnTotalTime.value;
      if(isoTime.lastIndexOf("T")==-1) correctQuestionLevelTimingError(hdnTotalTime);
      else
        try      
        {
          totalTimeSecs  = secsRemaining   = parseInt(isoTime.substring(isoTime.lastIndexOf("M")+1,isoTime.lastIndexOf("S")));
          totalTimeMins = minsRemaining = parseInt(isoTime.substring(isoTime.lastIndexOf("H")+1,isoTime.lastIndexOf("M")));          
          hrsRemaining   = 0; //parseInt(isoTime.substring(isoTime.lastIndexOf("T")+1,isoTime.lastIndexOf("H")));              
        }
        catch(ex) 
        {        
          correctQuestionLevelTimingError(hdnTotalTime)
        }      
    }
    function correctQuestionLevelTimingError(hdnTotalTime)
    {
      hrsRemaining    = 0;
      totalTimeMins = minsRemaining = 1;
      totalTimeSecs  =  secsRemaining  = 0;
      hdnTotalTime.value = "T0H1M0S";    
    }
 ////////////////////////////////////////End of Timer//////////////////////////////////////////////
       
    function setMode(testmode)
    {
      switch(testmode)
		{
		case "test":		
		case	"tryOutFeedback":	
		case "participantFeedback":		
		case "prePostFeedback":			
							mode = "test";																	
							return;		
		case "clientFeedback": 
		case "pAfterFeedback":
		case "prePostAfterFeedback":	
		case "tryOutAfterFeedback":			
		case "Preview":
							mode="clientFeedback";																																							
							return;			
		}
    }	
    
   	//Security related functions
	function handleIllegalAccess()
	{
		document.writeln("<span style='font-weight: bold; color: red'>Either you aren't authorized to view this page or a wrong method has been used to access the page</span>");
		window.location.assign("about:blank");			  
		self.close();
	}
	
	var boolEnableCopyPaste=true;
	function doEnforceSecurity()
	{			
		document.body.onbeforeunload=function ()
		{
			//if(!boolSubmitClick) return "You are trying to abort the test. It will be submitted for evaluation if u continue. Click on cancel to resume.";	
		};		
		
		document.body.onunload=function ()
		{
			if(!boolSubmitClick && !boolSaveState) 
			{
				doPopUpMessage("Assessment was aborted. It is being evaluated.<br>Please wait...");
				//storeAppletResponse();     
				storePageResponse(curPage);
				setFormValues();    
				var newwin = window.open("","","fullscreen=yes");
				var securityScript = "\<script\>document.oncontextmenu=document.onkeydown=function (){return false;}; \</script\>"
				/*This script is nessecary becoz new window is vulnearable till feedback is displayed. 
					it may take few secs to several minutes. crtl+n and view src from menu, view src from right click can give away xml
				*/
				var newDoc = newwin.document;
				newDoc.open();
				newDoc.write(securityScript);
				newDoc.write("<div style='display: none'>" + frmQuestion.outerHTML + "</div>"); //dont show the form. To hide details of how it is done								
				newDoc.close();
				newwin.frmQuestion.submit();
			}	
		};
		
		//disable selection of all elemats except in textboxes
    var eles = new Array("IMG","TABLE","TR","SPAN","TD","DIV");		
		disableSelection(eles);
	  SecureJavaAppletQuestions();
		document.oncontextmenu= function ()
		{return ((event.srcElement.type=="textarea" || event.srcElement.type=="text") &&boolEnableCopyPaste);}; 						
		
		document.onhelp= returnFalse;		
		
		document.onkeydown=function ()
		{			
      if(event.altKey||event.altLeft) 
      {          
          handleShourtcuts();
          return false;
      }  
			if(/* F1...F12*/111<event.keyCode && 124>event.keyCode)
			{		
				event.keyCode=0;
				return false;
			}
			var boolSrcIsText = event.srcElement.type=="textarea" || event.srcElement.type=="text";
			if(!boolSrcIsText && event.keyCode==8)	return false;		
			var boolCpPst =  boolSrcIsText && boolEnableCopyPaste;				
			if(event.ctrlKey||event.ctrlLeft)
						return ((event.keyCode== 88 || event.keyCode==67 ||event.keyCode==86) && boolCpPst); //ENABLE CRTL+X CRTL+V CRTL+Z																			
		};											
	}
	
	function disableSelection(eleArr)
	{
	  for(var i=0;i<eleArr.length;i++) 
	  {  
	      var allEle = document.getElementsByTagName(eleArr[i]);	 
	      for(var j=0;j<allEle.length;j++) allEle[j].unselectable="on";
	   }   	   
	}
	
	function handleShourtcuts()
	{
	  var ele=null;
    switch(event.keyCode)
    {            
      case 80:        ele = frmQuestion.prev;
                            break;
      case 78:        ele = frmQuestion.next;
                            break;
      case 82:       ele = document.getElementById("Proceed");
                            break;                      
      case 83:        ele = document.getElementById("summaryTextHolder");
                            break;
      case 70:       ele = document.getElementById("btnFlag");
                            break;            
      default:        return false;                      
    }
    if(ele) ele.click();
	}
	
	function SecureJavaAppletQuestions()
	{
	  var objects = document.getElementsByTagName("OBJECT");
	  for(var i in objects)  objects[i].onfocus=function (){setTimeout('document.body.focus()',200);};	    
	}  