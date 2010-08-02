public class Const
{
    public const string x = "xxx";
    public const int k = -999;
    public static string a = "xxx";
    public readonly string b = "xxx";
    public static readonly string c = "xxx";
    public static void Main()
    {
     const int i=9;
     int j = i;
     j++;
     string y="xxx";   
     //Const _const= new Const()   ;
     System.Console.WriteLine(object.ReferenceEquals("xxx",Const.x));
     System.Console.WriteLine(object.ReferenceEquals("xxx",y));
     System.Console.WriteLine(object.ReferenceEquals(y,Const.x));
    }
}
