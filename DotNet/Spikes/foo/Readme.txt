-----------------------------------------
Microsoft SQL Server OLAP Services SAMPLE
-----------------------------------------
Title:  WebBrowser  (beta)
Release Date:  05/03/1999
Files:	WebBrowser.exe (self-extracting zip)

-----------------------------------------
1.  DISCLAIMER
-----------------------------------------
Microsoft provides this sample application "as is" for informational purposes only. Microsoft makes no warranties, either express or implied, as to its accuracy of operation or suitability for use. Technical support is not available for the provided source code.

-----------------------------------------
2.  WHAT THIS SAMPLE APPLICATION DOES
-----------------------------------------
This application uses Active Server Pages (ASP) to allow users to browse a cube using Microsoft Internet Explorer.  The client computer does not need to have OLAP Services client components installed.  All user interaction and data display is done using HTML, DHTML, and JavaScript.

Copy the files included in the self-extracting .exe into a Microsoft Internet Information Server (IIS) virtual directory.  Start Internet Explorer and point it to test.htm.  This page allows you to input server, database, and cube name as well as what you want initially to see on rows and columns.  The cube that you want to browse should have user IUSR_<computer name> in one of its roles.

Click the Send button. On the next page you will see the list of dimensions in the cube and a grid displaying the results of the query.

On this page, you can:
- Click on a dimension name to open a new window displaying the dimension members.
- Click on a row or column header in the grid to drill down or up on the member.
- Drag a dimension name to the row or column header to replace the contents of the row or column.

MDXQuery.asp contains the script that displays the results of a query.
DimBrowser.asp contains the script that displays dimension members.
CubeBrowers.js contains the script that manages user interaction on the client.

-----------------------------------------
3.  INSTALLATION NOTES
-----------------------------------------
3.1 Prerequisites
    Microsoft Windows NT 
    IIS
    SQL Server version 7.0 OLAP Services 

3.2 Install sample files
    Expand the self-extracting zip file in an IIS directory.

3.3 Files
    CubeBrowser.js
    dim.bmp
    DimBrowser.asp
    MDXQuery.asp
    styles.css
    test.htm
    readme.txt
	