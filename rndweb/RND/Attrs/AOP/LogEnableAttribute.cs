using  System;


namespace RND.Attrs.AOP
{
	/// <summary>
	/// Summary description for LogEnableAttribute.
	/// </summary>	
	public class LogEnableAttribute:Attribute,System.Runtime.Remoting.Contexts.IContextAttribute  
	{
        string logFileName;
		public LogEnableAttribute(string fileName)
		{
			this.logFileName = fileName;
		}
        public string LogFile
        {
            get
            {
                return logFileName;
            }
            set
            {
                logFileName = value;
            }
        }
        
        void System.Runtime.Remoting.Contexts.IContextAttribute.GetPropertiesForNewContext(System.Runtime.Remoting.Activation.IConstructionCallMessage msg)
        {
            msg.ContextProperties.Add(new MyContextProperty(logFileName));
        }

        bool System.Runtime.Remoting.Contexts.IContextAttribute.IsContextOK(System.Runtime.Remoting.Contexts.Context ctx, System.Runtime.Remoting.Activation.IConstructionCallMessage msg)
        {
            if(ctx.GetProperty("ok ok")==null) return false;
            return true;
        }
	}
}
