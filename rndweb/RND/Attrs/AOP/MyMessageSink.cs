using System;

namespace RND.Attrs.AOP
{
	/// <summary>
	/// Summary description for MyMessageSink.
	/// </summary>
	public class MyMessageSink:System.Runtime.Remoting.Messaging.IMessageSink 
	{
        System.Runtime.Remoting.Messaging.IMessageSink next;
		public MyMessageSink(System.Runtime.Remoting.Messaging.IMessageSink next)
		{
			this.next = next;
		}
        System.Runtime.Remoting.Messaging.IMessageSink System.Runtime.Remoting.Messaging.IMessageSink.NextSink 
        { 
            get
            {
                return next;
            }
        }

        // Methods
        System.Runtime.Remoting.Messaging.IMessageCtrl System.Runtime.Remoting.Messaging.IMessageSink.AsyncProcessMessage(System.Runtime.Remoting.Messaging.IMessage msg, System.Runtime.Remoting.Messaging.IMessageSink replySink)
        {
            (System.Threading.Thread.CurrentContext.GetProperty("ok ok") as MyContextProperty).doLog(msg);
            return next.AsyncProcessMessage(msg,replySink);
        }
        
        System.Runtime.Remoting.Messaging.IMessage System.Runtime.Remoting.Messaging.IMessageSink.SyncProcessMessage(System.Runtime.Remoting.Messaging.IMessage msg)
        {
            (System.Threading.Thread.CurrentContext.GetProperty("ok ok") as MyContextProperty).doLog(msg);
            return next.SyncProcessMessage(msg);
        }
	}
}
