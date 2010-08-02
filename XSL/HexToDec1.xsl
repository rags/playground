<?xml version="1.0" encoding="UTF-8" ?>
<stylesheet version="1.0" xmlns="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt"
      xmlns:myscript="http://www.rags.com">
 <output omit-xml-declaration="yes"/>     
 <msxsl:script language="JScript" implements-prefix="myscript">
   function convertToHex(hex,base) 
   {   
    if(!base) base=16;//Default value
    
    var len = hex.length
    var retVal=0;  
    for(var i=0;;i++)   
    {
      if(i==len) break;
      var curChar = hex.charAt(len -i -1);
      if("0123456789".indexOf(curChar)>-1) retVal += parseInt(curChar) *  Math.pow(base,i);      
      else
      {
        //criptic line : value for A is A is 10 and ascii value is 65 so 65-55 gives A's value. similarly for B,C..........
	      curChar =  curChar.toUpperCase().charCodeAt(0)-55;  
        retVal += curChar *  Math.pow(base,i);
      }
    }
    return retVal;
   }
</msxsl:script>
     
<template match="/">  
  <value-of select="myscript:convertToHex('AbCd9801',16)"/>
</template>
</stylesheet>

  