class C
{
    public int x,y;
    public C(int x,int y)
    {
        this.x=x;
        this.y=y;
    }
    public C(C c)
    {
        this.x = c.x;
        this.y = 0;//dont copy y;
    }
    public static void Main()
    {
        C a = new C(10,20);
        C b = a;
        C c = new C(a);
        System.Console.WriteLine("a" + a.x + " " + a.y);
        System.Console.WriteLine("b" + b.x + " " + b.y);
        System.Console.WriteLine("c" + c.x + " " + c.y);
        System.Console.WriteLine(a==b);
    }


}
