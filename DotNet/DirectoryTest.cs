using System.IO;
using System.Threading;
class DirectoryTest
{
        public static void Main()
        {
                Directory.CreateDirectory(@"e:\temp");
                Directory.Delete(@"e:\temp");         
        }
}
