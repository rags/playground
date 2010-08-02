using System;
class x
{
    public static void Main()
    {
        int? x=null,Y=4;
        Console.WriteLine(x + " " + Y);
        Console.WriteLine(x.HasValue + " " + Y.HasValue);
        Console.WriteLine(x.GetValueOrDefault() + " " + Y.GetValueOrDefault());        
    }
}