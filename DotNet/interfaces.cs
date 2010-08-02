namespace interfaces
{
public        interface i1
        {
                i2 GetItem();
        }
      public  interface i2
        {
                i1 GetItem();
        }
}
