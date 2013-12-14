package com.raghu;

import com.sun.xml.internal.fastinfoset.util.CharArray;
import sun.plugin.javascript.navig.Array;

import java.io.*;

public class CommentRemover {

    public static void main(String[] args) throws Exception {

        CommentRemover commentRemover = new CommentRemover();
        /*commentRemover.removeComments(new File(CommentRemover.class.getResource("gtest-death-test.cc").getPath()));
        commentRemover.removeComments(new File(CommentRemover.class.getResource("greeglut.h").getPath()));
        commentRemover.removeComments(new File(CommentRemover.class.getResource("mySample.cpp").getPath()));
        */
        if(args.length>0){
           commentRemover.removeComments(new File(args[0]));
        }
        else{
            System.out.println("Usage: java com.Raghu.CommentRemover <filepath>");
        }

    }

    public void copyUntil(InputStream inputStream, OutputStream out,char till) throws IOException {
        int cur=0;
        while(true){
            cur=inputStream.read();
            if(cur==-1){
                return;
            }
            out.write(cur);
            if(till==(char)cur){
                return;
            }
        }
    }

    public void ignoreUntil(InputStream inputStream, String end) throws IOException {
        char [] acc=new char[end.length()];
        int cur=0,i=0;
        while(true){
            cur=inputStream.read();
            if(cur==-1){
                return;
            }
            if(i==acc.length){
               System.arraycopy(acc,1,acc,0,acc.length-1);
               i=acc.length-1;
            }
            acc[i++]=(char)cur;
            if(end.equals(new String(acc))){
                return;
            }
        }
    }



    public void removeComments(File file) throws Exception {
        String outFile = outputFileName(file);
        FileOutputStream outputStream = new FileOutputStream(outFile);
        InputStream inputStream = new FileInputStream(file);
        System.out.println("Writing to... " + outFile);
        int cur = 0;
        char curChar='\0';
        char prevChar='\0';
        while (true) {
            cur = inputStream.read();
            if(prevChar!='\0' && prevChar!='\\'){
                outputStream.write(prevChar);
            }
            if (cur == -1) break;
            boolean onNewLine = prevChar=='\n' || prevChar=='\0';
            prevChar=curChar;
            curChar=(char)cur;
            if(prevChar=='/' && (curChar=='/')){
                curChar=prevChar='\0';
                ignoreUntil(inputStream,"\n");
                if(!onNewLine) outputStream.write('\n');
            }
            if(prevChar=='/' && (curChar=='*')){
                curChar=prevChar='\0';
                ignoreUntil(inputStream,"*/");
            }
            if(curChar=='"'){
              outputStream.write(curChar);
              curChar=prevChar='\0';
              copyUntil(inputStream, outputStream, '"');
            }
        }


    }

    private String outputFileName(File file) {
        String absolutePath = file.getAbsolutePath();
        int ext = absolutePath.lastIndexOf(".");
        return absolutePath.substring(0,ext) + "_no-comment" + absolutePath.substring(ext);
    }
}
