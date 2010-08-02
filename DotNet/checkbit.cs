
class x
{
    public static void Main()
    {
/*        int i= 0xbf;
        int j=0x3f;
        System.Console.WriteLine(i + " " + (i>>7));
        System.Console.WriteLine(j + " " + (j>>7));

        System.Console.WriteLine((i>>7)%2==0);
        System.Console.WriteLine((j>>7)%2==0);
        */

        int j = (int)System.Math.Pow(2,30);
        System.Console.WriteLine("{0:x} {1:x} {2}",j,(j<<1)+1,(j<<1).ToString("x"));
    }
}
