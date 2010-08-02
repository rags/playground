class myobj
{
public static void Main()
{
    myobj x=new myobj(),y=new myobj(),z=x;
    System.Console.WriteLine(x.Equals(y));
    System.Console.WriteLine(x.Equals(z));

    System.Console.WriteLine(x==y);
    System.Console.WriteLine(x==z);

}
}
