set path="D:\Program Files\Java\jdk1.6.0_03\bin";%path%
set classpath=D:\Tools\antlr\lib\antlr-3.0.1.jar;D:\Tools\antlr\lib\antlr-2.7.7.jar;D:\Tools\antlr\lib\stringtemplate-3.1b1.jar
java org.antlr.Tool -o ..\generated -lib ..\generated Exp.g ExpTreeParser.g
