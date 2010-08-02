/*
    Author: Raghunandan R
    Module: dynatree.js
    Purpose: to display dynamic tree    
    Note: Works with both SQL XML and Web Service.
 */
    var curNode;
    var treeHolder;    
    var treePath;////="/AMS/AMSWS/CWSStylesheet.asmx/getContent";// '/Participantlist/amstemplate/DynaTree.xml?'; 
    var notRootNode;
    var boolChkBoxRequired;
    var menuHandler;
    var contextNode;    
    function initialize(treeHldr,xmlpath,topicID,notARootNode,chkBoxReqd,menuHandlerFn)
    {
      treeHolder=treeHldr;
      document.body.insertAdjacentHTML("beforeEnd","<xml id='__DYNA__XMLISLAND__' ></xml>")                
      notRootNode = notARootNode;            
      boolChkBoxRequired=chkBoxReqd==true;            
      treePath=xmlpath||treePath; 
      menuHandler = menuHandlerFn; 
      displayNode(topicID); 
    }
    function replaceImages(entity)
    {      
      //var entity = document.getElementById(topicID);      
      if(entity.opened=="true") return;
      var img="/ams/images/plusstart.gif",imgOpen="/ams/images/minusstart.gif";
      entity.image=img;
      entity.imageOpen=imgOpen;
      entity.all["image"].src=img;
    }
  function clickOnEntity(entity)
    {       
      curNode=entity;      
      if(entity.open == "false")    displayChildren(entity);
      else  collapse(entity);
      window.event.cancelBubble = true;
    }
    
    function getCurrentNode()
    {
      return curNode;
    }
    //var path;
    function getPath(entity)
    {      
        if(entity.parentNode!=treeHolder)
            return traverseParent(entity.parentNode) +  entity.id;     
        return entity.id;
     }
    
    function traverseParent(node)
    {
      if(node.tagName=="DIV")
      {
        if(node.parentNode!=treeHolder)
              return traverseParent(node.parentNode) + node.id + "/";
        return  node.id+"/";
      }
    }
    
    //////////////Functions for expanding tree for a given path////////////////////////////
    var pathArr;
    var level;
    function setPath(path)
    {    
     pathArr = path.split("/");             
     level = 0;     
     displayPath();               
    }    
    
    function displayPath()
    { 
      if(level == pathArr.length) 
        {      
          document.getElementById("td" + pathArr[level-1]).click();          
          return;      
        }    
      if(document.getElementById(pathArr[level])) displayChildren(document.getElementById(pathArr[level++]));              
      setTimeout("displayPath()",100);      
    }
    ////////////////////////////////////////////////////////////////////////////////////
    
    function displayNode(topicID)
    {
         curNode =  treeHolder;
         __DYNA__XMLISLAND__.ondatasetcomplete = firstTimeDataAvalilible;
         //boolTreeLoaded = false;
         __DYNA__XMLISLAND__.src = treePath + "?curNodeID=" + topicID + "&parentID=0&chkBox=" + boolChkBoxRequired ;                                        
    }
    function displayChildren(entity)
    {      
      if(entity.opened=="false")
      {     
        var parentID = entity.id;    
        curNode =  entity;
        __DYNA__XMLISLAND__.ondatasetcomplete = dataAvalilible;        
        __DYNA__XMLISLAND__.src = treePath + "?parentID=" + parentID + "&curNodeID=0&chkBox=" + boolChkBoxRequired;                
         return;
      }
      expand(entity);
    }
    function firstTimeDataAvalilible()
    {      
      dataAvalilible();
      if(!notRootNode)  replaceImages(curNode.getElementsByTagName("DIV")[0]);      
    }
    function dataAvalilible()
    {	      
      var strHTML =__DYNA__XMLISLAND__.documentElement.xml;      
      var startIndex = strHTML.indexOf(">") + 1;
      var endIndex = strHTML.lastIndexOf("<");            
      strHTML = strHTML.substring(startIndex,endIndex);            
      curNode.innerHTML += strHTML       
      render(curNode);           
      expand(curNode);      
      //__DYNA__XMLISLAND__.innerHTML = "";
    }
    
    function render(entity)//to put transline.gif/line.gif
    {
            
      for(i=0; i < entity.childNodes.length; i++) 
      {
        if(entity.childNodes(i).tagName == "DIV") 
		    {
		      var curChild = entity.childNodes(i);		      
		      if(menuHandler) 
		      {
		       curChild.oncontextmenu = menuHandler;		       
		      }
		      imageTD = curChild.all("image" + curChild.id);
		      insertLines(imageTD,curChild.parentNode)
		    }
	    }
    }
    
    function insertLines(imageTD,parent)
    {
      if(parent==null || parent==treeHolder) return;
      insertLines(imageTD,parent.parentNode);
      if(parent.tagName!="DIV") return;
      var imgURL = (parent.nextSibling) ? "/AMS/images/line.gif" : "/AMS/images/transline.gif";
      var image = document.createElement("<img src='"  +  imgURL  +  "' border='0'  height='100%' width='16'>" );
       imageTD.appendChild(image);
    }
    
    function expand(entity)
     {      
        if(entity != treeHolder)  entity.childNodes(0).all["image"].src = entity.imageOpen;        
        for(i=0; i < entity.childNodes.length; i++) 
                  if(entity.childNodes(i).tagName == "DIV")       entity.childNodes(i).style.display = "block";      
	      entity.open = "true";
        entity.opened="true";          
      }
  
  function collapse(entity)
   {        
        entity.childNodes(0).all["image"].src = entity.image;
     // collapse and hide children
      /*  for(i=1; i < entity.childNodes.length; i++) 
        {  
            var curChild = entity.childNodes(i);
            if(curChild.tagName != "DIV")  continue;
            collapse(curChild);
            curChild.style.display = "none";
            
        } */
        var children = entity.childNodes;
        //children = entity.getElementsByTagName ("DIV");
        for(i=0; i < children.length; i++) 
        { 
              var curChild=children[i];
              if(curChild.tagName != "DIV")  continue;
              curChild.style.display = "none";
              curChild.open="false";
              //curChild.childNodes(0).all["image"].src = curChild.image;
         }                    
        entity.open = "false";
  }
  
  
 var prevMouseOverTD;//store object
 var prevMouseClickTDID;//store id to get obj dynamically
 var mouseOverColor = "#d2eeff";       //"#ffcc99";
 var mouseClickColor  = "#d1e6fb";    //"#ffffcc";
 function changeColor(td,val)
 {
   switch(val)
    {
      case 1:  
                     td.style.background = mouseOverColor;
                     try
                     {
                            if(prevMouseOverTD.id==prevMouseClickTDID) prevMouseOverTD.style.background=mouseClickColor;
                            if(td!=prevMouseOverTD && prevMouseOverTD.style.background!=mouseClickColor) 
                            prevMouseOverTD.style.background = "none";
                     }catch(e){}
                    prevMouseOverTD=td;
                    break;
      case 2: 
                    td.style.background=mouseClickColor;
                    try
                    {
                      if(prevMouseClickTDID!=td.id) 
                      document.getElementById(prevMouseClickTDID).style.background="none";
                    }catch(e){}
                     prevMouseClickTDID=td.id;
                    break;
    }
}      