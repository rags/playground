abstract class Base
{
    public virtual void Print()
    {
        System.Console.WriteLine("BAse print");
    }
    public abstract void PrintA();
    public virtual void PrintB()
    {
        System.Console.WriteLine("Base B print");
    }

}
class Derived1: Base
{
    public override void Print()
    {
      System.Console.WriteLine("Derived1: print");  
    }
    public override void PrintA()
    {
      System.Console.WriteLine("Derived1: printA");  
    }
    public override void PrintB()
    {
      System.Console.WriteLine("Derived1: printB");  
    }


}

class Derived2: Derived1
{
    public override void Print()
    {
      System.Console.WriteLine("Derived2: print");  
    }
    public override void PrintA()
    {
      System.Console.WriteLine("Derived2: printA");  
    }
    public new void PrintB()
    {
      System.Console.WriteLine("Derived2: printB");  
    }

    public static void Main()
    {
       Derived2 d2 = new Derived2();
       Base @base = d2;
       Derived1 d1 =d2;

       @base.Print();
       @base.PrintA();
       @base.PrintB();

       d1.Print();
       d1.PrintA();
       d1.PrintB();

    }  

}

