class Power
{
    enum x{a,b,c234}
    public static void Main()
    {
        for(int i=0;i<64;i++)
        {
            System.Console.WriteLine(2 + "^"+i+": "+ _Power(i,2));
        }
    }
    private static ulong _Power(int x,int y)
    {
        ulong retVal=1;
        for(int i=0;i<x;i++) retVal *= 2;
        return retVal;
    }

}
