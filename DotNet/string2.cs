public class c
{
        public static string x,y="sdghsdf";
}
public class string2
{
       static string x;
       static string y="sdghsdf";
       public static void Main()
       {
        x="sdghsdf";
        string z=x;
        c.x=x;
        System.Console.WriteLine("b4 call: x="+ x + ";y=" + y+ ";z="+z+";c.x="+c.x+"c.y="+c.y);
        System.Console.WriteLine("x=y?: "+ object.ReferenceEquals(x,y));
        System.Console.WriteLine("y=z?: "+ object.ReferenceEquals(y,z));

        
        System.Console.WriteLine("x=c.x?: "+ object.ReferenceEquals(x,c.x));
        System.Console.WriteLine("x=x.y?: "+ object.ReferenceEquals(x,c.y));


        modify(ref x);
        System.Console.WriteLine("After call: x="+ x + ";y=" + y+ ";z="+z+";c.x="+c.x+"c.y="+c.y);
        System.Console.WriteLine("x=y?: "+ object.ReferenceEquals(x,y));
        System.Console.WriteLine("y=z?: "+ object.ReferenceEquals(y,z));
        System.Console.WriteLine("x=z?: "+ object.ReferenceEquals(x,z));
        
        System.Console.WriteLine("x=c.x?: "+ object.ReferenceEquals(x,c.x));
        System.Console.WriteLine("y=x.y?: "+ object.ReferenceEquals(y,c.y));
        System.Console.WriteLine("c.x=c.y?: "+ object.ReferenceEquals(c.x,c.y));




       }
       static void modify(ref string x)
       {
        x="changed";
       }
}
