using System;
using System.Collections;
using System.Reflection;

class ShapeFactory
{
    ShapeFactory(){}
    static Hashtable registry;
    static ShapeFactory()
    {
        registry = new Hashtable();
        Type typeShape = typeof(Base.Shape);
        Assembly asm = Assembly.GetExecutingAssembly();
        Type [] types = asm.GetTypes();
        foreach(Type type in types)
        {
            if(!type.IsSubclassOf(typeShape)) continue;
            Activator.CreateInstance(type,true);
        }
    }
    public static void Register(Type type)
    {
        //if(registry==null) registry = new Hashtable();// is this required?
        lock(registry)
        {
            registry.Add(type.Name,type);
        }
    }
    public static Base.Shape CreateShape(string shape)
    {

        return (Base.Shape)((Type)registry[shape]).InvokeMember("CreateShape",BindingFlags.Static | BindingFlags.Public | BindingFlags.InvokeMethod,null,null,new object[0]);
    }

}
namespace Base
{
abstract class Shape
{       
    int sides;
    protected Shape(int sides){this.sides=sides;}
    public int Sides
    {
        get
        {
            return sides;
        }
    }

    public abstract void Print();
    public static void Main()
    {

        ShapeFactory.CreateShape("Circle").Print();
        ShapeFactory.CreateShape("Triangle").Print();
        ShapeFactory.CreateShape("Square").Print();
        ShapeFactory.CreateShape("Rectangle").Print();

    }
}
}

namespace Derived
{

sealed class Circle:Base.Shape
{
    static Circle(){ShapeFactory.Register(typeof(Circle));}
    Circle():base(0){}
    public override void Print(){Console.WriteLine("Circle is" + Sides + " Sided");}
    public static Base.Shape CreateShape()
    {return new Circle();}
}


sealed class Square:Base.Shape
{
    static Square(){ShapeFactory.Register(typeof(Square));}
    Square():base(4){}
    public override void Print(){Console.WriteLine("Square is" + Sides + " Sided");}
    public static Base.Shape CreateShape()
    {return new Square();}

}

sealed class Rectangle:Base.Shape
{
    static Rectangle(){ShapeFactory.Register(typeof(Rectangle));}
    public Rectangle():base(4){}
    public override void Print(){Console.WriteLine("Rectangle is" + Sides + " Sided");}
    public static Base.Shape CreateShape()
    {return new Rectangle();}

}

sealed class Triangle:Base.Shape
{
    static Triangle(){ShapeFactory.Register(typeof(Triangle));}
    public Triangle():base(3){}
    public override void Print(){Console.WriteLine("Trianle is" + Sides + " Sided");}
    public static Base.Shape CreateShape()
    {return new Triangle();}

}

}
