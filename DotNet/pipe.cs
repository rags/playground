using System;
using System.Threading;
using System.Collections;

class MakeCar
{
    public static Queue engineQ;
    public static Queue tyreQ;
    public static Queue paintQ;
    public static Queue endQ;
    public static done;
    static MakeCar()
    {
        //create thread safe queues
        engineQ = Queue.Synchronized(new Queue(10));
        tyreQ = Queue.Synchronized(new Queue(10));
        paintQ = Queue.Synchronized(new Queue(10));
        endQ = Queue.Synchronized(new Queue(10));
        done = false;
    }

    public static void BeginAssembly(int noOfCars)
    {
        for(int i = 1; i <= noOfCars; i++)
        {
            Console.Write("Assembling Car" + 1 + "...");
            engineQ.Enqueue(i);
        }
    }

    public static void AssembleEngine()
    {
        Console.Write("Assembling Car" + 1 + " engine");
    }

    public static void AssembleTyres()
    {
        Console.Write("Assembling Car" + 1 + " tyre");
    }

    public static void Paint()
    {
        Console.Write("painting Car" + 1);
    }

    public static void EndAssembly()
    {
        Console.Write("Car" + 1 + " assembly complete.");
    }

    public static void Main()
    {
                    
    }
}
