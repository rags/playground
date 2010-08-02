using System;
interface IReader<T>
{
    T Get();
}
interface IWriter<T>
{
    void Put(T t);
}
class Test<T> : IReader<T>, IWriter<T>
{
    T t;
    public T Get() { return t; }
    public void Put(T t) { this.t = t; }
}
class Driver
{
    static void Main()
    {
        Test<string> t1 = new Test<string>();
        t1.Put("covariance");
        IReader<object> rdr = (IReader<object>)t1;
        Console.WriteLine(rdr.Get());
        Test<object> t2 = new Test<object>();
        IWriter<string> wrtr = t1;
        wrtr.Put("contravariance");
        Console.WriteLine(t2.Get());
    }
}

