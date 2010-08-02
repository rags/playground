interface StupidInterface<T1,T2>
{
    void init(T2 length);
    T2 this[T1 i]
    {
        get;
        set;
    }

}

class FirstV2Class<T>:StupidInterface<T,int>
{
    T[] arr;
    public T this[int i]
    {
        get{return arr[i];}
        set{arr[i]=value;}
    }
    public void init(int n)
    {
        arr = new T[n];
    }
    public static void Main()
    {
        FirstV2Class<string> list = new FirstV2Class<string>(10);       
    }
}
