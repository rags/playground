struct MyStruct
{
    public int x;
    public static void Main()
    {
        MyStruct newObj  = new MyStruct(),noNewObj;
        System.Console.WriteLine(newObj.x);
        //System.Console.WriteLine(noNewObj.x);thats thorws an error
        newObj.x=noNewObj.x=20;
        System.Console.WriteLine(newObj.x + "\n" + noNewObj.x);
    }
}
