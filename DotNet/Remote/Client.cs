using System;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Http;


class Client
{
    public static void Main(string [] args)
    {
//        RemotingConfiguration.Configure("client.config");        
        ChannelServices.RegisterChannel(new HttpChannel());
        RemoteObject obj = (RemoteObject)Activator.GetObject(typeof(RemoteObject),"http://ntech32:9000/Test");
//        RemoteObject obj = new RemoteObject();
        Console.WriteLine(RemotingServices.IsTransparentProxy(obj));
        obj.Test();
        if(args.Length==0) return;        
        string s=string.Empty;
        switch(args[0])
        {
            case "ForceShutdown":
                s=obj.ShutDown(RemoteObject.ExitFlags.EWX_SHUTDOWN | RemoteObject.ExitFlags.EWX_FORCE);
                break;
            case "Shutdown":
                s=obj.ShutDown(RemoteObject.ExitFlags.EWX_SHUTDOWN);
                break;
            case "Reboot":
                s=obj.ShutDown(RemoteObject.ExitFlags.EWX_REBOOT);
                break;
            case "LogOff":
                s=obj.ShutDown(RemoteObject.ExitFlags.EWX_LogOff);
                break;            
        }
        Console.WriteLine(s);
    }
}
