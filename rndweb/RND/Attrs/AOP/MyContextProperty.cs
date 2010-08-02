using System;
using System.IO;

namespace RND.Attrs.AOP
{
	/// <summary>
	/// Summary description for MyContextProperty.
	/// </summary>
	public class MyContextProperty:System.Runtime.Remoting.Contexts.IContextProperty,System.Runtime.Remoting.Contexts.IContributeObjectSink
	{
		string fileName;
        public MyContextProperty(string fileName)
		{
			this.fileName = fileName;
		}
        
        string System.Runtime.Remoting.Contexts.IContextProperty.Name 
        {
            get
            {
                return "ok ok";
            }
        }
        
        void System.Runtime.Remoting.Contexts.IContextProperty.Freeze(System.Runtime.Remoting.Contexts.Context newContext)
        {
            //do nothing
            //newContext.Freeze();
        }
        
        bool System.Runtime.Remoting.Contexts.IContextProperty.IsNewContextOK(System.Runtime.Remoting.Contexts.Context newContext)
        {
            return true;
        }
        
        System.Runtime.Remoting.Messaging.IMessageSink System.Runtime.Remoting.Contexts.IContributeObjectSink.GetObjectSink(System.MarshalByRefObject obj,System.Runtime.Remoting.Messaging.IMessageSink nextSink)
        {
            return new MyMessageSink(nextSink);
        }

        //logging funtion
        public void doLog(System.Runtime.Remoting.Messaging.IMessage msg)
        {
            StreamWriter sw = new StreamWriter(fileName,true);
            System.Collections.IDictionary dict = msg.Properties;
            foreach(string key in dict.Keys)
            {
                sw.WriteLine("Key: " + key +  "; Value : " + dict[key]);
            }
            sw.WriteLine("-------------------------------------------");
            sw.Close();            
        }
	}
}
