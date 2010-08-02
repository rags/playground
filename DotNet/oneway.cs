using System.Runtime.Remoting.Messaging;
class oneway
{
    public static void Main()
    {
        x();
        System.Console.WriteLine("End of Main");
    }
    [OneWay]
    static void x()
    {
        System.Console.WriteLine("Begin x");
        System.Threading.Thread.Sleep(5000);
        System.Console.WriteLine("End x");
    }

}
