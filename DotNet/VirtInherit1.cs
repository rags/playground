class A
{
    public virtual void X()
    {
        System.Console.WriteLine("A");
    }
}

class B:A
{
    public override void X()
    {
        System.Console.WriteLine("B");
    }
}

class C:B
{
    public new virtual void X()
    {
        System.Console.WriteLine("C");
    }
    
}
class D:C
{
    public override void X()
    {
        System.Console.WriteLine("D");
    }
    public static void Main()
    {
        A a;
        B b;
        C c;
        D d;
        a=b=c=d=new D();
        a.X();
        b.X();
        c.X();
        d.X();
    }
}

