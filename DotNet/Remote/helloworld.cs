class helloworld
{
        public static int Main()
        {

            try
            {
                System.IO.StreamWriter fileWriter
                = new System.IO.StreamWriter("x.txt");
                System.Console.SetOut(fileWriter);
                System.Console.WriteLine("hello");
                fileWriter.Close();
                return 1;
            }
            catch
            {
                return -999;
            }
        }
}

