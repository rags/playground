using System;
using System.Threading;
using System.Collections.Generic;
using System.Collections;

class CarFactory
{
    private  Queue<int> beginQ;
    private  Queue<int> engineQ;
    private  Queue<int> tyreQ;
    private  Queue<int> paintQ;
    private  Queue<int> endQ;
    private  bool beginDone;
    private  bool engineDone;
    private  bool tyreDone;
    private  bool paintDone;
    private  bool done;
    private int noOfCars;
    public CarFactory(int noOfCars)
    {
        //create thread safe queues - but it cane be done
        //2.0 beta doesnt cantain Queue<T>.Synchronized method to do it
        //so has to be handle manually using lock
        beginQ = new Queue<int>(10);
        engineQ = new Queue<int>(10);
        tyreQ = new Queue<int>(10);
        paintQ = new Queue<int>(10);
        endQ = new Queue<int>(10);
        this.noOfCars = noOfCars;
    }

    public void MakeCar()
    {
        new Thread(new ThreadStart(BeginAssembly)).Start();
        new Thread(new ThreadStart(AssembleEngine)).Start();
        new Thread(new ThreadStart(AssembleTyres)).Start();
        new Thread(new ThreadStart(Paint)).Start();
        new Thread(new ThreadStart(EndAssembly)).Start();
        for(int i = 1; i <= noOfCars; i++)
        {               
            lock(beginQ) beginQ.Enqueue(i);
        }
        beginDone = true;        
    }

    private void BeginAssembly()
    {
        for(;;)
        {
            int curCar;
            lock(beginQ)
            {
                if(beginQ.Count==0)
                {
                    if(beginDone) break;
                    Thread.Sleep(100);
                    continue;
                    
                }
                curCar = beginQ.Dequeue();
            }
            Console.WriteLine("Assembling Car" + curCar + "...");
            lock(engineQ) engineQ.Enqueue(curCar);
            Thread.Sleep(10);
        }
        engineDone = true;
    }

    private void AssembleEngine()
    {
        for(;;)
        {
            int curCar;
            lock(engineQ)
            {
                if(engineQ.Count==0)
                {
                    if(engineDone) break;
                    Thread.Sleep(20);
                    continue;
                    
                }
                curCar = engineQ.Dequeue();
            }
            Console.WriteLine("Assembling Car" + curCar + " engine");
            lock(tyreQ) tyreQ.Enqueue(curCar);
        }
        tyreDone = true;
        
    }

    private void AssembleTyres()
    {
        for(;;)
        {
            int curCar;
            lock(tyreQ)
            {
                if(tyreQ.Count==0)
                {
                    if(tyreDone) break;
                    Thread.Sleep(30);
                    continue;
                    
                }
                curCar = tyreQ.Dequeue();
            }
            Console.WriteLine("Assembling Car" + curCar + " tyre");
            lock(paintQ) paintQ.Enqueue(curCar);
            Thread.Sleep(5);
        }
        paintDone = true;
        
    }

    private void Paint()
    {
        for(;;)
        {
            int curCar;
            lock(paintQ)
            {
                if(paintQ.Count==0)
                {
                    if(paintDone) break;
                    Thread.Sleep(70);
                    continue;
                    
                }
                curCar = paintQ.Dequeue();
            }
            Console.WriteLine("painting Car" + curCar);
            lock(endQ) endQ.Enqueue(curCar);
        }
        done = true;
    }

    private void EndAssembly()
    {
        while(true)
        {
            lock(endQ)
            {
                if(endQ.Count==0)
                {
                    if(done) break;
                    Thread.Sleep(5);
                    continue;
                    
                }
                Console.WriteLine("Car" + endQ.Dequeue() + " - Assembly complete");
            }         
        }

    }


    public static void Main()
    {
       new CarFactory(10).MakeCar();             
    }
}
