using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Http;
using System;

class Server1
{
    public static void Main()
    {
         //RemotingConfiguration.Configure("server.config");
         ChannelServices.RegisterChannel(new HttpChannel(9000));
         RemotingConfiguration.RegisterWellKnownServiceType(typeof(RemoteObject),"Test",WellKnownObjectMode.Singleton);
        Console.WriteLine("there u go...");
         Console.ReadLine();
    }
}
