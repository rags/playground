using System;
namespace PrinterSpace
{
    //Does nothing gr8. it has private,public instance method,property,field and a static method
    public class Printer
    {
       DateTime time; 
        public Printer(DateTime time)
        {
            this.time=time;
        }

        public Printer()
        {
            time = DateTime.Now;
        }

        public DateTime Time
        {
            get
            {
                return time;
            }
            set
            {
                time = value;
            }
        }
       public DateTime x()
	{return time;}	
	public void y()
	{Console.Write(x());}	

       public static void Print(string msg)
       {
            Console.WriteLine(msg);
       }

       public /*instance*/ void Print(string msg,int times)
       {
            Print();
            for(int i=0;i<times;i++) Console.WriteLine(msg);
       }
        
        void Print()
        {
            Console.WriteLine(time.ToString());
        }
    }
}
