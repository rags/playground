public class MyObject
{
    public int x;

    public static void Main()
    {
        MyObject obj1 = new MyObject(),obj2 = new MyObject(),obj3=obj1;
        obj1.x = 
        obj2.x = 10;
        ModifyByRef(ref obj1);
        ModifyByVal(obj2);
        if(obj1!=null) System.Console.WriteLine(obj1.x);
        else System.Console.WriteLine("obj1 is null");
        if(obj2!=null) System.Console.WriteLine(obj2.x);
        else System.Console.WriteLine("obj2 is null");
        if(obj3!=null) System.Console.WriteLine(obj3.x);
        else System.Console.WriteLine("obj3 is null");

    } 
    public static void ModifyByRef(ref MyObject obj)
    {
        obj.x = 20;
        obj = null;
    }
    public static void ModifyByVal(MyObject obj)
    {
        obj.x = 20;
        obj = null;
    }

}
