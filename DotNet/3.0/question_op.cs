class x{
        public static void Main(){
                int? i=null;
                string s = null;
                System.Console.WriteLine(i??0 );//+
                System.Console.WriteLine(s??"foo");
                System.Console.WriteLine(i + " " + s);
        }
}
