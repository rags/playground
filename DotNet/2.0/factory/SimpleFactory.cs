/*
Bad design:
1. base class has to know about all its deriving classes. breaks the ooad rules
2. needs code change,recompilation... if a new base class is added externally
*/
using System;
enum Shapes
{
    Circle,
    Triangle,
    Square,
    Rectangle
}

abstract class Shape
{       
    int sides;
    public Shape(int sides){this.sides=sides;}
    public int Sides
    {
        get
        {
            return sides;
        }
    }

    public abstract void Print();
    public static Shape CreateShape(Shapes shape)
    {
        switch(shape)
        {
            case Shapes.Circle: return new Circle();            
            case Shapes.Triangle: return new Triangle();
            case Shapes.Square: return new Square();
            case Shapes.Rectangle: return new Rectangle();
        }
        return null;
    }
    public static void Main()
    {
        Shape.CreateShape(Shapes.Circle).Print();
        Shape.CreateShape(Shapes.Triangle).Print();
        Shape.CreateShape(Shapes.Square).Print();
        Shape.CreateShape(Shapes.Rectangle).Print();
    }
}

sealed class Circle:Shape
{

    public Circle():base(0){}
    public override void Print(){Console.WriteLine("Circle is" + Sides + " Sided");}
}


sealed class Square:Shape
{

    public Square():base(4){}
    public override void Print(){Console.WriteLine("Square is" + Sides + " Sided");}
}

sealed class Rectangle:Shape
{

    public Rectangle():base(4){}
    public override void Print(){Console.WriteLine("Rectangle is" + Sides + " Sided");}
}

sealed class Triangle:Shape
{

    public Triangle():base(3){}
    public override void Print(){Console.WriteLine("Trianle is" + Sides + " Sided");}
}

