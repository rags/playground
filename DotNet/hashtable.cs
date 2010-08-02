using System;
using System.Collections;
class x
{
    int a;
    public DateTime date;
    x(int a){this.a=a;}
    public static void Main()
    {
       Hashtable table = new Hashtable();
       string a = "rags",b = new string(new char [] {'r','a','g','s'}),c = new string(new char [] {'r','a','g'}),d = "rags";
       Console.WriteLine(object.ReferenceEquals(a,b) + " " + object.Equals(a,b));
      
       table.Add(a,20);
       table.Add(b,23);

//       Console.Flush();

//       table.Add(c + 's',23);
//       table.Add(d,23);
    }
}
