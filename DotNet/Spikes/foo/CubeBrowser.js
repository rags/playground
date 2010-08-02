//----------------------------------------------------------------------------------
// Disclaimer
//----------------------------------------------------------------------------------
//Microsoft provides this sample application "as is" for informational purposes only 
//and Microsoft makes no warranties, either express or implied, as to its accuracy 
//of operation or suitability for use. Technical support is not available for the 
//provided source code.
//----------------------------------------------------------------------------------

//
//	CubeBrowser.js
//		JavaScript code for manipulating cube browser in DHTML
//

// global variables
var drag = 0;
var move = 0;
var clickleft = 0;
var clicktop = 0;
var startleft = 0;
var starttop = 0;
var dimBrowser;
var afterDrop = 0;

//
// check position of the mouse
//
function insideResultTable() {
	result = false
	t = document.all.ResultTable

	// check height
	if ((window.event.y > t.offsetTop) && 
	     (window.event.y < t.offsetTop + t.offsetHeight)) {
		result = true	
	}

	// check width
	if (result) {
		if ((window.event.x > t.offsetLeft) && 
		     (window.event.x < t.offsetLeft + t.offsetWidth)) {
			result = true	
		}
		else {
			result = false
		}
	}

	return result
}

function insideXAxis() {
	t = document.all.ResultTable

	// calculate the top and the bottom of the first row
	xAxisTop = t.offsetTop
	xAxisBottom = t.offsetTop + t.rows[0].offsetHeight

	if (window.event.y > xAxisTop && window.event.y < xAxisBottom) {
		return true
	}

	return false
}

function insideYAxis() {
	t = document.all.ResultTable

	// calculate the top and the bottom of the first row
	yAxisLeft = t.offsetLeft
	yAxisRight = t.offsetLeft + t.rows[0].cells[0].offsetWidth

	if (window.event.x > yAxisLeft && window.event.x < yAxisRight) {
		return true
	}

	return false
}

//
// initialize the window event handlers
//
function init() {
	window.document.onmousemove = mouseMove
	window.document.onmousedown = mouseDown
	window.document.onmouseup = mouseUp
	window.document.onmouseover = mouseOver
	window.document.onmouseout = mouseOut
	window.document.ondragstart = mouseStop
	window.document.onclick = mouseClick
}

//
// on mouse down remember where we started to drag
//
function mouseDown() {
	if (drag) {
		clickleft = window.event.x - parseInt(dragObj.style.left)
		clicktop = window.event.y - parseInt(dragObj.style.top)
		startleft = dragObj.style.left
		starttop = dragObj.style.top

		dragObj.style.zIndex += 1
		move = 1 
	}
}

function mouseStop() {
	window.event.returnValue = false
}

//
// if we are moving an object then update its position
// as the mouse moves
//
function mouseMove() {
	if (move) {
		dragObj.style.left = window.event.x - clickleft
		dragObj.style.top = window.event.y - clicktop
	}
	window.event.returnValue = false
}

//
// on mouseUp event execute the drag and drop
//
function mouseUp() {
	if (move) {
		move = 0

		// get the dimension name
		dimName = window.event.srcElement.id

		// check if the drop occured inside the table
		if (insideResultTable()) {
			if (insideXAxis()) {
				document.queryForm.elements("columns").value = "{[" + dimName + "].Levels(0).Members}"
				document.queryForm.elements("column dimension").value = dimName
				document.queryForm.submit()

				afterDrop = 1
				return false
			}
			else {
				if (insideYAxis()) {
					document.queryForm.elements("rows").value = "{[" + dimName + "].Levels(0).Members}"
					document.queryForm.elements("row dimension").value = dimName
					document.queryForm.submit()

					afterDrop = 1
					return false
				}				
				else {
					// return the dimension to the starting position
					dragObj.style.left = startleft
					dragObj.style.top = starttop
				}
			}
		}
		else {
			// return the dimension to the starting position
			dragObj.style.left = startleft
			dragObj.style.top = starttop
		}

		afterDrop = 0
	}
}

//
// if we are over a "draggable" object then set the drag flag
//
function mouseOver() {
	if (window.event.srcElement.className == "Dimension") {
		dragObj = window.event.srcElement
		drag = 1
	}
}

function mouseOut() {
	drag = 0
}


//
// if the user clicks on a dimension then display the dimension members in 
// the new window
//
function mouseClick() {
	if (afterDrop == 1) {
		return false
	}

	if (window.event.srcElement.className == "Dimension") {
		// get the dimension name
		dimName = window.event.srcElement.id

		// open the new window
		dimBrowser = window.open("", "DimensionBrowser", 
					 "resizable,scrollbars,height=400,width=300")
		dimBrowser.focus()

		// write to the new window
		newContent = "<HTML>"
		newContent = newContent + "<HEAD>"
		newContent = newContent + "<TITLE>Dimension Browser: " + dimName + "</TITLE>"
		newContent = newContent + "<LINK REL=STYLESHEET TYPE=\"text/css\" HREF=\"styles.css\">"
		newContent = newContent + "</HEAD>"
		newContent = newContent + "<BODY>"
		newContent = newContent + "Retrieving dimension information..."
		newContent = newContent + "<form CLASS=invisibleForm name=\"queryForm\" action=\"DimBrowser.asp\" method=\"get\">"
		newContent = newContent + "<input type=\"TEXT\" name=\"server\" value=\"" + document.queryForm.elements("server").value + "\" size=20>"
		newContent = newContent + "<input type=\"TEXT\" name=\"database\" value=\"" + document.queryForm.elements("database").value + "\" size=20>"
		newContent = newContent + "<input type=\"TEXT\" name=\"cube\" value=\"" + document.queryForm.elements("cube").value + "\" size=20>"
		newContent = newContent + "<input type=\"TEXT\" name=\"dimension\" value=\"" + dimName + "\" size=20>"
		newContent = newContent + "<input type=\"TEXT\" name=\"level\" value=\"1\" size=20>"
		newContent = newContent + "<input type=submit value=\"Send\">"
		newContent = newContent + "</form>"
		newContent = newContent + "</BODY>"
		newContent = newContent + "</HTML>"
		dimBrowser.document.write(newContent)
		dimBrowser.document.close()
		dimBrowser.document.queryForm.submit()
	}	
}

//
// this function is called when the user clicks on a cell in the table
//
function drill(evt) {
	var sMemberName
	if (window.event.srcElement.className == "axisXCell") {
		sMemberName = window.event.srcElement.id
		document.queryForm.elements("columns").value = "ToggleDrillState(" + document.queryForm.elements("columns").value + ",{" + sMemberName + "})"
		document.queryForm.submit()
	}
	else if (window.event.srcElement.className == "axisYCell") {
		sMemberName = window.event.srcElement.id
		document.queryForm.elements("rows").value = "ToggleDrillState(" + document.queryForm.elements("rows").value + ",{" + sMemberName + "})"
		document.queryForm.submit()
	}

	return false
}
