class tmp
{
public void Main(int x)
{}

public static void Main()
{
       System.Console.WriteLine(string.Join(",",new string[]{"what"}));
       return;

       System.Console.WriteLine(int.MaxValue);
       /* for(int i=0;i<=3;i++)
        {
                int jack = i;
        }*/
        /*
        System.String s = "ford";
        string s1 = s;
        string str = "ikon";
        string str1 = str;
        modify(ref s,str);
        System.Console.Write(s+ " " + s1);
        System.Console.Write(str+ " " + str1);
        int i=5,j=5,k=i;
        System.Console.Write("i,j: eq? : " + object.Equals(i,j) + " ref? : " + object.ReferenceEquals(i,j));
        System.Console.Write("i,k: eq? : " + object.Equals(i,k) + " ref? : " + object.ReferenceEquals(i,k));
        */
        string a;
        x(out a);
        System.Console.Write(a);

}
public static void modify(ref string s,string str)
{s="hyundai"; str="Accent";}


public static void x(out string y){y="yyy";_x(out y);}

public static void _x(out string _y){_y="xxx";}

}
