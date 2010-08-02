using System;
using System.Web;
using System.IO;

namespace RND
{
	/// <summary>
	/// Summary description for URLHandler.
	/// </summary>
	public class URLHandler :IHttpHandler 
	{
        public bool IsReusable
        {
            get{return true;}    
        }

        public void ProcessRequest(HttpContext context)
        {
            HttpRequest req=context.Request;
            HttpResponse res=context.Response;
            string path = req.Path;
            if(Path.GetExtension(path)==".aspx") context.RewritePath(path.Replace("/RAGS/","/"));
        }
	}

}
