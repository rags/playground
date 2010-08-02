class a
{
 public virtual void x()
 {

    System.Console.WriteLine("a");

 }
}

class b:a
{
 public override void x()
 {                                
    System.Console.WriteLine("b");
 }
}

class c:b
{
 public override void x()
 {  
    System.Console.WriteLine("c");
    ((a)this).x();    
 }


 public static void Main()
 {
    new c().x();
 }
}



