#define X
#define y
#undef y
using System;
using System.Diagnostics;

class C
{
    [Conditional("X")]
    void x(){}
    #if y
    void x(int x)
    {
        Console.WriteLine(x + " 1 ");
    }
    #else
    void x(int x)
    {
        Console.WriteLine(x + " 2 ");
    }
    #endif
    public static void Main()
    {
        new C().x(4);
    }
}

