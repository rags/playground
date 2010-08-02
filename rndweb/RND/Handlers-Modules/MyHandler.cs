using System;
using System.Web;
namespace RND
{
	/// <summary>
	/// Summary description for MyHandler.
	/// </summary>
	public class MyHandler :IHttpHandler 
	{
		public MyHandler()
		{
			//
			// TODO: Add constructor logic here
			//
		}
    public void ProcessRequest(HttpContext context)
    {
      HttpRequest req=context.Request;
      HttpResponse res=context.Response;
      res.Write("Output from handler");
      res.Write("Query: [" + req.QueryString["query"] +"]");
    }
    public bool IsReusable
    {
      get{return false;}    
    }

	}
}
