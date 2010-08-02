class Class
{
    int  x;
    public int getX()
    {
        return x;
    }
    public void setX(int x)
    {
        this.x = x;
    }

    public int X
    {
        get{return x;}
        set{x=value;}
    }
    public static void Main()
    {
        Class onj = new Class();
       onj.setX(onj.getX()+1);
       onj.X++;
    }
}
