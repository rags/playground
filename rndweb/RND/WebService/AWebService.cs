using System;
using System.Web.Services;

namespace RND.WebService
{
	public class AWebService : System.Web.Services.WebService
	{
    [WebMethod]
    public string HelloWorld()
    {
        return "Hello";
    }
	}
}
