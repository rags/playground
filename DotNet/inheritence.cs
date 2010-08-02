class MyBase
{
    public virtual void VirtFn()
    {
        System.Console.WriteLine("base virtual fn....");
    }
    public void NonVirtFn()
    {
        System.Console.WriteLine("base non virtual fn....");
    }

}

class Derived1 : MyBase
{
    public override void VirtFn()
    {
        System.Console.WriteLine("derived1 override fn....");
    }
    public new void NonVirtFn()
    {
        System.Console.WriteLine("derived1 non virtual fn....");
    }
}

class Derived2 : MyBase
{
    /*public new void VirtFn()
    {
        System.Console.WriteLine("derived1 virtual fn....");
    } */
    public new void NonVirtFn()
    {
        System.Console.WriteLine("base virtual fn....");
    }
    public static void Main(){}
    
}

