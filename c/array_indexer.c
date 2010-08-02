#include <stdio.h>
const int rows=5;
const int cols=3;
void foo(int [rows][cols], void (*fn)(int[rows][cols],int,int));
void bar(int[rows][cols]);
void print(int[rows][cols],int,int);

int  main(){
  int a[rows][cols];
  bar(a);
  foo(a,print);
  

}

void bar(int a[rows][cols]){
  int i;
  for(i=0;i<rows*cols;i++){
    a[i/cols][i%cols] = i+1;
  }
}


void foo(int a[rows][cols], void (*fn)(int[rows][cols],int,int)){
  int i;
  for(i=0;i<rows*cols;i++){	
    fn(a,i/cols,i%cols);
  }
}

void print(int a[rows][cols],int i,int j){
  printf("%d %c",*(*(a+i)+j), (((1+j)%cols==0)?'\n':' '));  
}
