class X
{
    int x;
    public static void Main()
    {
        X a = new X();
        fn(a);        
        System.Console.WriteLine(a.x);
    }
    public static void fn(X a)
    {
        a=null;
    }
}

