using System;
class Event
{
    private EventHandler exitHandler;
    public  event EventHandler Exit
    {
        add{ exitHandler += value; }
        remove{ exitHandler -= value; }
    }
    ~Event()
    {
        if(exitHandler!=null) exitHandler(null,null);
    }
    public static void Main()
    {
        new Event().Exit += new EventHandler(HandleExit);
    }
    public static void HandleExit(object sender,EventArgs e)
    {
        System.Console.WriteLine("Handler called");
    }
}

