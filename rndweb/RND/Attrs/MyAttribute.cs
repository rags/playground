using System;

namespace RND.Attrs
{
	/// <summary>
	/// Summary description for MyAttribute.
	/// </summary>
	[AttributeUsage(AttributeTargets.Class)]
	public class MyAttribute:Attribute 
	{
        int x,y;        
		public MyAttribute(int x)//positional param
		{            
			this.x=x;
		}
        public int Y//Named param
        {
            get
            {
                return y;
            }
            set
            {
                y=value;
            }
        }
        public int X//Named param
        {
            get
            {
                return x;
            }
         
        }
	}
}
