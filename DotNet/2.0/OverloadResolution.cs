class OverloadResolution
{

        public void foo(V res)
        {
                System.Console.WriteLine("V");
               res.move();
        }

        public void foo(Bus o)
        {
                 System.Console.WriteLine("bus");
        }



        public static void Main()
        {
              Bus o = new Bus();
                new OverloadResolution().foo(o);

        }


}

public interface V
{
   void move();
}

class Car : V{
   public virtual void move(){
        System.Console.Write("Car");
        }
}

class Bus : Car{
   public override void move(){
        System.Console.Write("bus");
        }
}
