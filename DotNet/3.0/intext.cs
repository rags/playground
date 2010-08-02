using System;

public static class IntExt
{
        public static void Times(this int i,Action<int> action)
        {
                for(int j=0;j<i;j++) action(j);
        }

        public static void Main()
        {
                4.Times(i=>Console.WriteLine("hello world"));
        }
}
