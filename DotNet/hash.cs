using System;
class hash
{
    public static void Main()
    {
      string[] args = Environment.GetCommandLineArgs();
      if(args.Length==1 || (args.Length==2 && args[1].Equals("/?")))
      {
       Console.Write("Usage: " + args[0] + " string [sha1/md5]\nex: " + args[0] + " myString sha1");
       return;
      }
      if(args.Length>1)
      {
        string data = args[1];
        string algo = (args.Length>2 && (args[2].Equals("sha1")||args[2].Equals("md5")))?args[2]:"md5";
        Console.Write(System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(data,algo));
        return;
      }

    }
}
