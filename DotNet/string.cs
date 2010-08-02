class hmm
{
        public static void Main()
        {
                System.String w = "xxx";
//                string x = "xx" + "x";
                string x = "xx";
                string y = "yyy";
                string z = w;
                x += "x";
                System.Console.WriteLine("w:"+ w + "; x:" + x + "; y:" + y +  "; z(=w)" + z);
                System.Console.WriteLine("x,y : \n");
                CompareStrings(w,x);
                System.Console.WriteLine("w,z : \n");
                CompareStrings(w,z);
                System.Console.WriteLine("---------------");
                w="yyy";
                System.Console.WriteLine("w:"+ w + "; x:" + x + "; y:" + y +  "; z(=w)" + z);
                CompareStrings(w,y);
                CompareStrings(w,z);

                System.Console.WriteLine("---------------");
                System.Console.WriteLine("w:"+ w + "; x:" + x + "; y:" + y +  "; z(=w)" + z);
                w=y;
                CompareStrings(w,y);
                CompareStrings(w,z);



        }
        public static void CompareStrings(string x,string y)
        {
                System.Console.WriteLine(
                                          "=? : " + x.Equals(y) +
                                          "\nref? : " + object.ReferenceEquals(x,y) +
                                          "\neq? : " + object.Equals(x,y) + "\n"

                                        );


        }
}
