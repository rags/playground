using PrinterSpace;
using System.Reflection;
class Test
{
    public static void Main()
    {
        Printer objPrint = new Printer();
        objPrint.Time = System.DateTime.Now.AddHours(5);
        Printer.Print("Hello");
        objPrint.Print("Hiya",20);
        //call private method
        objPrint.GetType().InvokeMember("Print",BindingFlags.NonPublic|BindingFlags.Instance|BindingFlags.InvokeMethod,null,objPrint,null);        
    }
}
