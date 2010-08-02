using System;
using System.Web;
using System.IO;
using System.Xml;

namespace RND.Handlers_Modules
{
	/// <summary>
	/// Summary description for HttpServer.
	/// </summary>
	public class HttpServer:IHttpHandler 
	{
		public HttpServer()
		{
			//
			// TODO: Add constructor logic here
			//
		}
        public void ProcessRequest(HttpContext context)
        {
            HttpRequest req=context.Request;
            HttpResponse res=context.Response;
            XmlDocument doc = new XmlDocument();            
            byte [] arr = new byte[req.ContentLength];
            req.InputStream.Read(arr,0,arr.Length);
            string str = System.Text.Encoding.ASCII.GetString(arr,0,arr.Length);            
            doc.LoadXml(str);
            doc.DocumentElement.AppendChild(doc.CreateElement("FromServer"));
            res.ContentType = "text/xml";
            res.Write(doc.OuterXml);
        }
        public bool IsReusable
        {
            get{return true;}    
        }
	}
}
