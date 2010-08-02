interface IA
{}
struct B:IA
{
    public int x;
    public B(int x){this.x=x;}
    public static void Main()
    {
        IA a1,a2;
        B b = new B(12);
        a1 = b;
        a2=a1;
        B b2 = (B)a2;
        b2.x=20;
        System.Console.WriteLine(b.x);
        System.Console.WriteLine(b2.x);
    }
}
