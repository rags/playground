abstract class x
{
    public abstract void a();
    protected abstract void b();
    public static void Main()
    {
        x _x = new y();
        _x.a();
    }
}
class y:x
{
    public override void a()
    {
        System.Console.Write("ok ok");
    }
    protected override void b(){}
}

