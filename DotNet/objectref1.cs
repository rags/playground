public class MyObject
{
    public int x;

    public static void Main()
    {
        MyObject obj1 = new MyObject(),obj2=obj1;
        obj1.x = 10;
        Modify(obj1);
        
        if(obj1!=null) System.Console.WriteLine(obj1.x);
        else System.Console.WriteLine("obj1 is null");
        
        if(obj2!=null) System.Console.WriteLine(obj2.x);
        else System.Console.WriteLine("obj2 is null");        
    } 

    public static void Modify(MyObject obj)
    {
        obj.x = 20;
        obj = null;
    }
    
}
