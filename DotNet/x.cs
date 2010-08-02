using System;
class x
{
    public static void Main()
    {
        long lng=2147483648;
        long res=0;
        for(;lng>0;lng=lng/2) res |= lng;
        Console.WriteLine(res);
        
        Console.WriteLine( "[" + new TimeSpan(365,0,0,0).TotalMinutes  +"]");
        /*

        float f = 123.00000f;
        System.Console.WriteLine(f);*/
    }
}
