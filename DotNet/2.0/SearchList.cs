using System;
using System.Collections;
class MyClass:IComparable
{
    public int i;
    public string str;
    public MyClass(int i,string str)
    {
        this.i=i;
        this.str=str;
    }
    public int CompareTo(Object obj)
    {
        MyClass c = obj as MyClass;
        return string.Compare(this.str,c.str);
    }
    public static void Main()
    {
        ArrayList list = new ArrayList();
        list.add(new MyClass(10,"sdg"));
        list.add(new MyClass(13,"uy,k"));
        list.add(new MyClass(14,"tho"));
        list.sort();
    }
}
