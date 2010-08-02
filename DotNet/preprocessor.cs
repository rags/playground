#define XXX
#undef XXX
class X
{
    public static void Main()
    {
        #if XXX
            System.Console.WriteLine("Dephined")
        #else 
            System.Console.WriteLine("Naat Dephined");
        #endif
    }
}
