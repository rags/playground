partial class XXX
{
    int x;
    public int X
    {
        set{x=value;}
        get{return x;}
    }
    public int Y
    {
        set{y=value;}
        get{return y;}
    }

    XXX(int x,int y,int z)
    {
       this.x = x;
       this.y = y;
       this.z = z;
    }
    public void Print()
    {
        System.Console.WriteLine("X : " + X + ";Y : " + Y + ";Z : " + Z);
    }
}
