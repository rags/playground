using System;
class exceptions
{
    public static void Main()
    {
        try
        {
            fn();    
        }
        catch(Exception ex)
        {
           Console.WriteLine(ex.Message);
        }
  
    }
    public static void fn()    
    {
        try
        {
            throw new Exception("foo");
        }
        catch(Exception ex)
        {
            try
            {
                throw ex;
            }
            finally
            {
                throw new Exception("blah");
            }
        }
        finally
        {
            throw new Exception("bar");
        }
    }
}
