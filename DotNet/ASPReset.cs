using System;
using System.Diagnostics;
using System.DirectoryServices;
using System.Collections;
using System.Reflection;
class ASPReset
{
    public static void Main()
    {
      string [] args = Environment.GetCommandLineArgs();
      if(args.Length>1)
      {
        if(args[1].Equals("/?"))
        {
            Console.WriteLine("usage: " + args[0] + " [AppName]\nex:\n" + args[0] +" - To restart asp.net\n" + args[0]+" WebApp1 - To restart WebApp1");
            return;
        }
          
        DirectoryEntry _dir = new DirectoryEntry("IIS://localhost/W3SVC/1/Root");
          foreach(DirectoryEntry dir in _dir.Children)
          {

    //          try
  //            {

                if(args[1].ToLower().Equals(dir.Name.ToLower()))
                {
                    PropertyCollection props = dir.Properties;
                    Console.WriteLine("ok ok");
                    Console.WriteLine(typeof(PropertyCollection).InvokeMember("get_Count",BindingFlags.GetProperty | BindingFlags.Public,null,props,new object[0]));
                    Console.WriteLine("ok ok1");
                    Console.WriteLine(dir.Name + " " + dir.Properties["Path"][0]);
                }
//              }
                  // catch{}
          }
        return;
      }
      Console.WriteLine("Attempting restart...");
      Process [] procs = Process.GetProcessesByName("aspnet_wp");
      if(procs.Length==0)
      {
        Console.WriteLine("ASP.net is not running...");
        return;
      }

      procs[0].Kill();
      Console.WriteLine("restarted...");
  
    }

}
