using System;
using System.Web;
using System.IO;
namespace RND
{
	/// <summary>
	/// Summary description for MyModule.
	/// </summary>            
	public class MyModule : IHttpModule 
	{
        public void Dispose()
        {
        }
        public void Init(System.Web.HttpApplication context)
        {
            context.BeginRequest += new EventHandler(this.HandleBeginRequest);
        }
        
        public void HandleBeginRequest(object sender,EventArgs args)
        {
            HttpApplication context = (HttpApplication)sender;
            HttpRequest req=context.Request;
            HttpResponse res=context.Response;
            string path = req.Path;
            int ragsIndex = path.IndexOf("/RAGS/");
            if(ragsIndex>0)
            {
                string fileName = Path.GetFileName(path);
                String rootDir = context.Server.MapPath(path.Substring(0,ragsIndex));
                string serverRoot = context.Server.MapPath("/");
                string filePath = FindPath(rootDir,fileName);                
                context.Context.RewritePath("/" + filePath.Substring(filePath.IndexOf(serverRoot) + serverRoot.Length).Replace(Path.PathSeparator,'/') );                                 
            }
        }

        public static string FindPath(string dir,string file)
        {
            string [] filePaths = Directory.GetFileSystemEntries(dir,file);
            if(filePaths.Length>0)
            {
                return filePaths[0];
            }
            foreach(string subDir in Directory.GetDirectories(dir))
            {
                    string filePath = FindPath(subDir,file);
                    if(filePath.Length>0) return filePath;
             }
            return string.Empty;
        }
	}
}