#include <stdio.h>

const int rows=5;
const int cols=3;
void out(int [rows][cols], void (*fn)(int[rows][cols],int,int));
void populate(int[rows][cols]);
void print(int[rows][cols],int,int);

int  main(){
  int a[rows][cols];
  populate(a);
  out(a,print);
}

void populate(int a[rows][cols]){
  int i,j;
  for(i=0;i<rows;i++){
	for(j=0;j<cols;j++){
    a[i][j] = i*cols + j+1;
	}
  }
}


void out(int a[rows][cols], void (*fn)(int[rows][cols],int,int)){
  int i;
  for(i=0;i<rows*cols;i++){	
    fn(a,i/cols,i%cols);
  }
}

void print(int a[rows][cols],int i,int j){
  printf("%d %c",*(*(a+i)+j), (((1+j)%cols==0)?'\n':' '));  
}
