<%@ Page Language="vb" CodeBehind="VBFILE.aspx.cs" AutoEventWireup="false" Inherits="RND.VBFILE" %>
<script>
external.AddFavorite(
    'http://www.bme.ie',
    'BME - Baumeister Mediasoft Engineering'
    ); 
</script>
<html>
    <head>
        <LINK REL="SHORTCUT ICON" HREF="http://localhost/pickm3/smiley.ico">
            <title>VB file</title></head>
    <body>
        <% 
        dim s as string = "hi" 
        Response.Write(s & "hello")
         %>
    </body>
</html>
