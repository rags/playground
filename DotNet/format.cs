using System;
class form
{
    public static void Main()
    {
        string [] input = {"$23,345,456.56","$1,000,000,000.01","$100,000,111.00"};
        Console.WriteLine(23345456.56.ToString("$###,###.##"));
        Console.WriteLine(5456.56.ToString("$###,###.##"));
        Console.WriteLine(32567623856.00.ToString("$###,#00.00"));
        Console.WriteLine(0.56789.ToString("$###,#00.00"));
    }
}
