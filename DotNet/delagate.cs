struct XXX
{
    public int member;
    public delegate XXX ReturnThisDelegate();
    public XXX ReturnThis(){return this;}
    XXX(int x)
    {member=x;}
    
    public static void Main()
    {
        ReturnThisDelegate del;
        CreateInstance(out del);
        System.GC.Collect();
        if(del!=null) System.Console.WriteLine(del().member);
    }

    static void CreateInstance(out ReturnThisDelegate del)
    {
        del = new ReturnThisDelegate(new XXX(23).ReturnThis);//inline object       
    }
}
