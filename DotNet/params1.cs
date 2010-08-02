class v
{
    public static void Main()
    {
        fn(1,2);
        fn(1);
        fn(1,2,3);
    }
    public static void fn(int a,int b)
    {
        System.Console.WriteLine("fn");
    }
    public static void fn(params int[] a)
    {
        System.Console.WriteLine("params fn");
    }

}
