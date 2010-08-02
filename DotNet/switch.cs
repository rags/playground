using System;
class x
{
    public static int Main(string [] z)
    {
      int x = int.Parse(z[0]);
      switch(x)
      {
        case 45:
            Console.WriteLine(45);
            break;
        case 5:
            Console.WriteLine(5);
            break;
        default:
            Console.WriteLine(x);
            break;            
        
      }
      int y;
      switch(x)
      {
        case 54:
            return 7;
        case 55:
            return 90;
        case 5:
            return 90;
        case 53:
            return 90;
        default:
            return 0;
            
      }

    }
}
