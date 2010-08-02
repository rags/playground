class Params
{
      public int x;
      public static void Main()
      {
        Params p1=new Params(),p2=new Params();
        p1.x=p2.x=100;
        modify(ref p1);
        modify1(p2);
        System.Console.WriteLine(p1.x + " " + p2.x);
      }
      public static void modify(ref Params p1)
      {
        p1.x=99;
      }
      public static void modify1(Params p1)
      {
        p1.x=99;
      }
      
}
