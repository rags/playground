using System;
using System.Collections;
using System.Collections.Specialized;
class NameObjectCollection:NameObjectCollectionBase,IComparable
{
    public int Compare(object a,object b)
    {
        Item _a = a as Item, _b = b as Item;
        if(_a==null || _b==null) throw new Exception("Invalid arsg");
        return (_a.x>_b.x)?1:(_a.x<_b.x)?-1:0;
    }
    public void Sort()
    {
        
    }

}
class Item
{
    int x;
    Item()
    {
        int x = new Random().Next();
    }
    public static void Main()
    {
        HashProvider hashProvider = new HashProvider()
        HashTable table = new HashTable(hashProvider,hashProvider);
        table.add(1,new Item());
        table.add(2,new Item());
        table.add("45",new Item());
        table.add(10,new Item());
        table.add("deg",new Item());

    }
}


