using System;

public class Test
{
    static void Main()
    {
        string a = new string(new char[] {'a', 'e', 'i', 'o', 'u'});
        string b = new string(new char[] {'a', 'e', 'i', 'o', 'u'});
        //a,b point to 2 diff objects

        

        Console.WriteLine (a==b);//string class implements ==
        Console.WriteLine (a.Equals(b));//it overides Equals
        Console.WriteLine (object.ReferenceEquals(a,b));//see? they r diff objs indeed

        object c = a;
        object d = b;

        Console.WriteLine (c==d);//object has no defnition for ==
        Console.WriteLine (c.Equals(d));
        //runtime polymorphism @ work string.Equals is called
        //(since Equlas is virtual fn), not object.Equals

        string x="aeiou",y="aeiou";
        //x,y point to same object
        Console.WriteLine (object.ReferenceEquals(x,y));//thats the proof
        c=x;d=y;
        Console.WriteLine (c==d);//well they point to same object
        Console.WriteLine (c.Equals(d));//again string.Equals is called
    }
}
