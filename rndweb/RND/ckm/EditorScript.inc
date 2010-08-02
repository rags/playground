<style>SELECT {
	BACKGROUND: #ffffff; FONT: 8pt verdana,arial,sans-serif
}
.Gen {
	POSITION: relative
}
TABLE {
	POSITION: relative
}
.heading {
	BACKGROUND: #ffffff; COLOR: navy
}
/*.Composition {
	POSITION: relative; BACKGROUND-COLOR: #ffffff
}*/
.yToolbar {
	BORDER-RIGHT: 1px solid; BORDER-TOP: 1px solid; LEFT: 0px; BORDER-LEFT: 1px solid; WIDTH: 500px; BORDER-BOTTOM: #d1e6fa 1px solid; POSITION: relative; TOP: 0px; HEIGHT: 27px; BACKGROUND-COLOR: #d1e6fa
}
.Btn {
	BORDER-RIGHT: #d1e6fa 1px solid; BORDER-TOP: #d1e6fa 1px solid; BORDER-LEFT: #d1e6fa 1px solid; WIDTH: 23px; POSITION: absolute; TOP: 1px; HEIGHT: 23px; BACKGROUND-COLOR: #d1e6fa
}
.Ico {
	LEFT: -1px; WIDTH: 22px; POSITION: absolute; TOP: -1px; HEIGHT: 22px
}
.TBSep {
	BORDER-RIGHT: buttonhighlight 1px solid; FONT-SIZE: 0px; BORDER-LEFT: buttonshadow 1px solid; WIDTH: 1px; POSITION: absolute; TOP: 1px; HEIGHT: 22px
}
.TBGen {
	FONT: 8pt verdana,arial,sans-serif; POSITION: absolute; TOP: 2px; HEIGHT: 22px
}
.TBHandle {
	BORDER-RIGHT: buttonshadow 1px solid; BORDER-TOP: buttonhighlight 1px solid; FONT-SIZE: 1px; BORDER-LEFT: buttonhighlight 1px solid; WIDTH: 3px; POSITION: absolute; TOP: 1px; HEIGHT: 22px; BACKGROUND-COLOR: #d1e6fa
}
.BtnMouseOverUp {
	BORDER-RIGHT: buttonshadow 1px solid; BORDER-TOP: buttonhighlight 1px solid; BORDER-LEFT: buttonhighlight 1px solid; WIDTH: 24px; BORDER-BOTTOM: buttonshadow 1px solid; POSITION: absolute; TOP: 1px; HEIGHT: 23px; BACKGROUND-COLOR: #d1e6fa
}
.BtnMouseOverDown {
	BORDER-RIGHT: buttonhighlight 1px solid; BORDER-TOP: buttonshadow 1px solid; BORDER-LEFT: buttonshadow 1px solid; WIDTH: 24px; BORDER-BOTTOM: buttonhighlight 1px solid; POSITION: absolute; TOP: 1px; HEIGHT: 23px; BACKGROUND-COLOR: #d1e6fa
}
.BtnDown {
	BORDER-RIGHT: buttonhighlight 1px solid; BORDER-TOP: buttonshadow 1px solid; BORDER-LEFT: buttonshadow 1px solid; WIDTH: 24px; BORDER-BOTTOM: buttonhighlight 1px solid; POSITION: absolute; TOP: 1px; HEIGHT: 23px; BACKGROUND-COLOR: gainsboro
}
.IcoDown {
	LEFT: 0px; WIDTH: 24px; POSITION: absolute; TOP: 0px; HEIGHT: 23px
}
.IcoDownPressed {
	LEFT: 1px; POSITION: absolute; TOP: 1px
}
BODY {
	BORDER-RIGHT: 0px; BORDER-TOP: 0px; MARGIN: 5px; BORDER-LEFT: 0px; BORDER-BOTTOM: 0px
}
		</style>
		<SCRIPT>
<!--
var bLoad=false
var pureText=true
var bodyTag="<BODY>" //MONOSPACE STYLE=\"font:10pt arial,sans-serif\"
var bTextMode=false
public_description=new Editor

function Editor() {
  this.put_html=SetHtml;
  this.get_html=GetHtml;
  this.put_text=SetText;
  this.get_text=GetText;
  this.CompFocus=GetCompFocus;
}

function GetCompFocus() {
  Composition.focus();
}

function GetText() 
{
  return Composition.document.body.innerText;
}

function SetText(text) {
  text = text.replace(/\n/g, "<br>")
  Composition.document.body.innerHTML=text;
}

function GetHtml() {
  if (bTextMode) 
    return Composition.document.body.innerText;
  else {
    cleanHtml();
    cleanHtml();
    return Composition.document.body.innerHTML;
  }
}

function SetHtml(sVal) {
  if (bTextMode) Composition.document.body.innerText=sVal;
  else Composition.document.body.innerHTML=sVal;
  
}
// -->
		</SCRIPT>