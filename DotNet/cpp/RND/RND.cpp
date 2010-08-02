// This is the main project file for VC++ application project 
// generated using an Application Wizard.

#include "stdafx.h"
#include <iostream>
#using <mscorlib.dll>
#include <tchar.h>
__gc class xxx
{
public:
	int y;
};
using namespace System;
using namespace std;
class C
{
public:
    const int i;
    C():i(10)
    {
    }    
};
void modify(System::String*  s,xxx* x)
{	
	cout<<&s<<&x<<endl;
	s = "changed";
	cout<<&s<<&x<<endl;
}
// This is the entry point for this application
int _tmain(void)
{
    // TODO: Please replace the sample code below with your own.    
	xxx* x = new xxx;
	x->y = 10;
    System::String*  s = "hello world";
	//Console::WriteLine(S"{0}",__box(&s));
	cout<<&x<<&s<<endl;
	modify(s,x);
	cout<<&x<<&s<<endl;
	//Console::WriteLine(S"{0}",__box(&s));
	Console::ReadLine();
    return 0;
}

