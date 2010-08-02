using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

//[Serializable]
public class RemoteObject : MarshalByRefObject 
{
    public enum ExitFlags
    {
        EWX_LogOff= 0,
        EWX_SHUTDOWN = 1,
        EWX_REBOOT= 2,
        EWX_FORCE= 4,
        EWX_POWEROFF= 8
    }

    [DllImport("user32.dll")]
    public extern static bool ExitWindowsEx(ExitFlags uFlags,int dwReason);

    public RemoteObject()
    {
        Console.Write("In constructor...");
    }
    public void Test()    
    {
        Console.Write("test success!");
        Process proc = Process.Start(@"C:\Documents and Settings\raghunandanr\Desktop\temp\DOTNET\Remote\helloworld.exe");        
    }
    public string ShutDown(ExitFlags flag)
    {
        try
        {
            ExitWindowsEx(flag,0);
            return "doing... " + flag.ToString();
        }
        catch(Exception ex){return ex.Message;}
    }
}