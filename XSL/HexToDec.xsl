<?xml version="1.0" encoding="UTF-8" ?>
<stylesheet version="1.0" xmlns="http://www.w3.org/1999/XSL/Transform">
<output omit-xml-declaration="yes"/>
<template match="/">
  Deci:
  <call-template name="ConvertToDecimal">
    <with-param name="input" select="'AbCd9801'" />
  </call-template>
  Hex:
  <call-template name="ConvertToBase">
    <with-param name="input" select="9845367621" />
    <with-param name="base" select="16" />
  </call-template>
</template>
<template name="ConvertToBase">
  <param name="input">2500<!--default value--></param>  
  <param name="base" select="16"/> <!--by def 16......... try 2 8 anthing less than or = 16-->
  <!--no need to pass these argument-->
  <param name="output"/> 
  <choose>
    <when test="$input&lt;=0">
      <value-of select="$output"/>
    </when>
    <otherwise>
      <variable name="remainder" select="$input mod $base"/>      
          <call-template name="ConvertToBase">
            <with-param name="input" select="floor($input div $base)" />
            <with-param name="base" select="$base" />
            <with-param name="output">
              <choose>
                <when test="$remainder &lt; 10">
                    <value-of select="concat($remainder,$output)" />
                </when>
                <when test="$remainder = 10"><value-of select="concat('A',$output)" /></when>
                <when test="$remainder = 11"><value-of select="concat('B',$output)" /></when>
                <when test="$remainder = 12"><value-of select="concat('C',$output)" /></when>
                <when test="$remainder = 13"><value-of select="concat('D',$output)" /></when>
                <when test="$remainder = 14"><value-of select="concat('E',$output)" /></when>
                <when test="$remainder = 15"><value-of select="concat('F',$output)" /></when>
              </choose>
            </with-param>
          </call-template>        
    </otherwise>
  </choose>
</template>

<template name="ConvertToDecimal">
  <param name="input">AbCd9801<!--default value--></param>  
  <param name="base" select="16"/> <!--by def 16......... try 2 8 anthing less than or = 16-->
  <!--no need to pass these argument-->
  <param name="output" select="0"/>
  <param name="loopIndex" select="0"/>  
  <param name="curWeight" select="1"/>  
  <variable name="len" select="string-length($input)"/>  
  <variable name="curNum" select="translate(substring($input,$len - $loopIndex,1),'abcdef','ABCDEF')" />
  <!--uncomment if power function has to be used and remove curWeight param
  <variable name="curWeight">
    <call-template name="Power">
      <with-param name="z" select="16" />
      <with-param name="a" select="$loopIndex" />
    </call-template>
  </variable>
  -->
  <variable name="curDecimal">
    <choose>
      <when test="$curNum &gt; -1 and $curNum &lt; 10">
        <value-of select="$curNum * $curWeight"/>
      </when>
      <when test="$curNum='A'">
        <value-of select="10 * $curWeight"/>
      </when>
      <when test="$curNum='B'">
        <value-of select="11 * $curWeight"/>
      </when>
      <when test="$curNum='C'">
        <value-of select="12 * $curWeight"/>
      </when>
      <when test="$curNum='D'">  
        <value-of select="13 * $curWeight"/>
      </when>
      <when test="$curNum='E'">  
        <value-of select="14 * $curWeight"/>
      </when>
      <when test="$curNum='F'">  
        <value-of select="15 * $curWeight"/>
      </when>      
    </choose>
  </variable>  
  <choose>
    <when test="$curDecimal=''"><!--error: return empty --></when>
    <when test="$loopIndex = $len - 1">
      <value-of select="$output + $curDecimal"/>
    </when>
    <otherwise>
      <call-template name="ConvertToDecimal">
        <with-param name="input" select="$input"/>
        <with-param name="output" select="$output + $curDecimal"/>
        <with-param name="loopIndex" select="$loopIndex + 1"/>
        <with-param name="curWeight" select="$curWeight *  $base"/>
      </call-template> 
    </otherwise>
  </choose>
</template>
<!--
<template name="Power"> 
    <param name="z" />
    <param name="a" />
    <param name="output" select="1"/> 
    <choose>
      <when test="$a=0">
        <value-of select="1"/>
      </when>
      <when test="$a=1">
        <value-of select="$output * $z"/>
      </when>
      <otherwise>
        <call-template name="Power">
          <with-param name="z" select="$z"/>
          <with-param name="a" select="$a - 1"/>
          <with-param name="output" select="$output * $z"/>
        </call-template>
      </otherwise>
    </choose>
  </template>
  -->
</stylesheet>

  