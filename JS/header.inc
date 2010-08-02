


<!---- Script for Menu --->
<script language="JavaScript">
<!--
function MM_reloadPage(init) {  //reloads the window if Nav4 resized
  if (init==true) with (navigator) {if ((appName=="Netscape")&&(parseInt(appVersion)==4)) {
    document.MM_pgW=innerWidth; document.MM_pgH=innerHeight; onresize=MM_reloadPage; }}
  else if (innerWidth!=document.MM_pgW || innerHeight!=document.MM_pgH) location.reload();
}
MM_reloadPage(true);
// -->

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.0
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && document.getElementById) x=document.getElementById(n); return x;
}

function MM_swapImage() { //v3.0

  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

function MM_showHideLayers() { //v3.0
  var i,p,v,obj,args=MM_showHideLayers.arguments;
  for (i=0; i<(args.length-2); i+=3) if ((obj=MM_findObj(args[i]))!=null) { v=args[i+2];
    if (obj.style) { obj=obj.style; v=(v=='show')?'visible':(v='hide')?'hidden':v; }
    obj.visibility=v; }
}

function MM_jumpMenu(targ,selObj,restore){ //v3.0
  eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
  if (restore) selObj.selectedIndex=0;
}
//-->
</script>

<!---  Div tag for Menu Applet starts here---->
<div id="Layer1" style="position:absolute; left:0px; top:60px; width:222px; height:358px; z-index:1; visibility:hidden"> 
  <table width="222" border="0" cellspacing="0" cellpadding="0" height="293">
    <tr> 
      <td width="220" bgcolor="#E6E6E6">TreeMenu...</td>
      <td bgcolor="#000000" width="2"><img src="../../images/spacer.gif" width="2" height="4"></td>
    </tr>
    <tr align="right" valign="bottom" bgcolor="#000000"> 
      <td colspan="2" height="6"><a href="javascript:;" onClick="MM_showHideLayers('Layer1','','hide')"><img src="../../images/close.gif" width="14" height="14" vspace="2" hspace="2" border="0" alt="Close Menu"></a></td>
    </tr>
  </table>
</div>

<!---  Div tag for Menu Applet ends here---->


<table width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr> 
	  <!-- <td width="120"><img src="../../images/freedomnew.gif" width="120" height="42"></td> -->
      <td  background="../../images/back.gif" width="100%"><img src="../../images/top_sub.jpg"></td>
      <td background="../../images/back.gif"><!--<img src="../../images/excellogo.gif">--></td>
    </tr>
  </table>

 <script>
/*****************************************************************************
Default browsercheck - Leave this one
******************************************************************************/
 //Making browsercheck object

var mDebugging=2 

oCMenu1=new makeCoolMenu("oCMenu1") 
oCMenu1.useframes=0 
oCMenu1.frame="frmMain" 

oCMenu1.useclick=0 
oCMenu1.useNS4links=1  
oCMenu1.NS4padding=2 
oCMenu1.checkselect=0
oCMenu1.offlineUrl="file:///C|/Inetpub/wwwroot/AMS/" 
oCMenu1.onlineUrl="http://www.dhtmlcentral.com/coolmenus/examples/withoutframes/" 

oCMenu1.pagecheck=1 
oCMenu1.checkscroll=0
oCMenu1.resizecheck=1 
oCMenu1.wait=100 

//Background bar properties
oCMenu1.usebar=1 
oCMenu1.barcolor="#6699CC" 
oCMenu1.barwidth="75%" 
oCMenu1.barheight="menu" 
oCMenu1.barx=0 
oCMenu1.bary="28" 
oCMenu1.barinheritborder=0 

//Placement properties
oCMenu1.rows=1 
oCMenu1.fromleft="10" 
oCMenu1.fromtop="28" 
oCMenu1.pxbetween=3


//oCMenu1.menuplacement=new Array('2%','20%','36%','57%','70%','80%') 
oCMenu1.menuplacement=0



//TOP LEVEL PROPERTIES - ALL OF THESE MUST BE SPESIFIED FOR LEVEL[0]
oCMenu1.level[0]=new Array() 
oCMenu1.level[0].width=100 
oCMenu1.level[0].height=18
oCMenu1.level[0].bgcoloroff="#6699CC" 
oCMenu1.level[0].bgcoloron="" 
oCMenu1.level[0].textcolor="white" 
oCMenu1.level[0].hovercolor="#0F5A97" 
oCMenu1.level[0].style="padding:2px; font-family:verdana,helvetica; font-size:11px; font-weight:normal" 
oCMenu1.level[0].border=0 
oCMenu1.level[0].bordercolor="red" 
oCMenu1.level[0].offsetX=0 
oCMenu1.level[0].offsetY=-1 
oCMenu1.level[0].NS4font="tahoma,arial,helvetica"
oCMenu1.level[0].NS4fontSize="2"

/*New: Added animation features that can be controlled on each level.*/
oCMenu1.level[0].clip=0 
oCMenu1.level[0].clippx=0 
oCMenu1.level[0].cliptim=0 
//Filters - This can be used to get some very nice effect like fade, slide, stars and so on. EXPLORER5.5+ ONLY - If you set this to a value it will override the clip on the supported browsers
oCMenu1.level[0].filter=0 

//Alignment properties
oCMenu1.level[0].align="bottom" //Value: "top" || "bottom" || "left" || "right" 

//EXAMPLE SUB LEVEL[1] PROPERTIES - You have to spesify the properties you want different from LEVEL[0] - If you want all items to look the same just remove this
oCMenu1.level[1]=new Array() 
oCMenu1.level[1].width=oCMenu1.level[0].width-2
oCMenu1.level[1].height=22
oCMenu1.level[1].style="padding:2px; font-family:verdana,helvetica; font-size:11px; font-weight:normal"
oCMenu1.level[1].align="right" 
oCMenu1.level[1].offsetX=-(oCMenu1.level[0].width-2)/2+20
oCMenu1.level[1].offsetY=0
oCMenu1.level[1].border=1 
oCMenu1.level[1].bordercolor="black"

//EXAMPLE SUB LEVEL[2] PROPERTIES - You have to spesify the properties you want different from LEVEL[1] OR LEVEL[0] - If you want all items to look the same just remove this
oCMenu1.level[2]=new Array() 
oCMenu1.level[2].width=150
oCMenu1.level[2].height=20
oCMenu1.level[2].bgcoloroff="black"
oCMenu1.level[2].bgcoloron="#0099cc"
oCMenu1.level[2].style="padding:2px; font-family:tahoma,arial,helvetica; font-size:10px; font-weight:bold"
oCMenu1.level[2].align="bottom" 
oCMenu1.level[2].offsetX=-(oCMenu1.level[1].width-2)/2+100
oCMenu1.level[2].offsetY=0
oCMenu1.level[2].border=1 
oCMenu1.level[2].bordercolor="#6386DE"
oCMenu1.level[2].NS4font="tahoma,arial,helvetica"
oCMenu1.level[2].NS4fontSize="1"

/*Variables for each menu item: (** means that they have to be spesified!)
oCMenu1.makeMenu(
				'name',
				'parent',
				'text',
				'link',
				'target',
				'width',
				'height',
				'img1',
				'img2',
				'bgcoloroff',
				'bgcoloron',
				'textcolor',
				'hovercolor',
				'onclick',
				'onmouseover',
				'onmouseout')
*/


oCMenu1.makeMenu('top0','','Content','','',55)
	oCMenu1.makeMenu('sub00','top0','Content structure','../ContentStructureManagement/frmContentStructureManagement.aspx?show=cs','',120)
	oCMenu1.makeMenu('sub01','top0','Keywords','../ContentStructureManagement/frmContentStructureManagement.aspx?show=kw','',120)
	oCMenu1.makeMenu('sub02','top0','Content mapping','../ContentStructureManagement/frmContentStructureManagement.aspx?show=cm','',120)


	
oCMenu1.makeMenu('top1','','Question','','',60)
	oCMenu1.makeMenu('sub11','top1','Question Bank','../QuestionBank/frmQuestionBank.aspx','',150)
	oCMenu1.makeMenu('sub12','top1','Question mapping','../../QuestionMapping/frmQuestionMapping.aspx','',150)
	oCMenu1.makeMenu('sub13','top1','Learning objects Library','frmObjectsLibrary.aspx','',150)
	oCMenu1.makeMenu('sub14','top1','Metattagging','../Metatagging/frmmetataggingtree.aspx','',150)

oCMenu1.makeMenu('top2','','Assessment','','',80)
	oCMenu1.makeMenu('sub21','top2','Assessment','../AssessmentManagement/frmAssessmentManagement.aspx?show=ass','',80)
	oCMenu1.makeMenu('sub22','top2','Schedule','../AssessmentManagement/frmAssessmentManagement.aspx?show=sch','',80)
	
	
oCMenu1.makeMenu('top3','','Results','','',50)	
	oCMenu1.makeMenu('sub31','top3','Essay evaluation','../Authoring/ResultsManagement/frmEssayEvaluation.aspx','',110)	
	oCMenu1.makeMenu('sub32','top3','Score editor','../Authoring/ResultsManagement/frmScoreEditor.aspx','',110)	
	
oCMenu1.makeMenu('top4','','Reports','','',50)
	oCMenu1.makeMenu('sub41','top4','Reports','','',100)
	oCMenu1.makeMenu('sub42','top4','Report builder','','',100)

oCMenu1.makeMenu('top5','','Administration','','',95)
	oCMenu1.makeMenu('sub51','top5','Group','../SecurityandSystemAdministration/frmSecuritynSystemAdministration.aspx?show=g','',95)
	oCMenu1.makeMenu('sub52','top5','Role','../SecurityandSystemAdministration/frmSecuritynSystemAdministration.aspx?show=r','',95)
	oCMenu1.makeMenu('sub53','top5','User','../SecurityandSystemAdministration/frmSecuritynSystemAdministration.aspx?show=u','',95)
	oCMenu1.makeMenu('sub54','top5','Participant','../SecurityandSystemAdministration/frmSecuritynSystemAdministration.aspx?show=p','',95)

oCMenu1.makeMenu('top6','','Stylesheet','','',70)
	oCMenu1.makeMenu('sub61','top6','Import stylesheet','','',120)
	oCMenu1.makeMenu('sub62','top6','Delete stylesheet','','',120)
	oCMenu1.makeMenu('sub63','top6','View stylesheet','','',120)

oCMenu1.makeMenu('top7','','Communication','','',100)	
	oCMenu1.makeMenu('sub71','top7','Email','','',100)	

oCMenu1.makeMenu('top8','','Search','','',50)
	oCMenu1.makeMenu('sub81','top8','Search','','',50)
	
oCMenu1.makeMenu('top9','','Help','','',50)
	oCMenu1.makeMenu('sub91','top9','Contents','')
	oCMenu1.makeMenu('sub92','top9','Index','')
	oCMenu1.makeMenu('sub93','top9','Search','')


		
		
//Leave these two lines! Making the styles and then constructing the menu
oCMenu1.makeStyle(); oCMenu1.construct()			
</script>

