using System;
class test
{
    public static string GetRandomPassword()
    {
            
        char [] pwdChars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','_'};
        const int lastInd = 62;
        Random rand = new Random();
        int pwdLen = rand.Next(6,12);
        char [] pwd = new char[pwdLen];//password of length b/w 6 and 12
        pwd[0] = pwdChars[rand.Next(51)];//51 = indxed of 'Z', i.e only alphabet for first char
        for(int i=1;i<pwdLen;i++) pwd[i] =  pwdChars[rand.Next(lastInd)];
        //rand = null;
        return new string(pwd);
    }
    public static void Main()
    {
        Console.WriteLine(GetRandomPassword());
        Console.WriteLine(GetRandomPassword() + "");
        Console.WriteLine(GetRandomPassword() + "");
        Console.WriteLine(GetRandomPassword() + "");
        Console.WriteLine(GetRandomPassword() + "");
    }
}