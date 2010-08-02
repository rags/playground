class X
{
    int x;
    public static void Main()
    {
        X _x=null;
        fn(_x);
        System.Console.WriteLine(_x.x);
        int a = 10;
        fn1(ref a);
    }
    public static void fn(X _x)
    {
        _x = new X();
        _x.x=10;
    }
    public static void fn1(ref int x){x=20;}
}
