using System.Text.RegularExpressions;
using System;
class RegEx_       
{
    public static void Main()
    {
    /*
        Console.WriteLine(Regex.Match("[Purchaser].[All Purchaser].[COMMERCIAL].[ABBOTT ENTERPRISES INC].[ABBOTT ENTERPRISES INC - GENERAL].[GENERAL - ABBOTT ENTERPRISES INC (524000|1)]",@"(?<=\]\.\[)[^\]]+(?=\]$)").Value);
        
        Console.WriteLine(Regex.Replace("[Purchaser].[All Purchaser].[COMMERCIAL].[ABBOTT ENTERPRISES INC].[ABBOTT ENTERPRISES INC - GENERAL].[GENERAL - ABBOTT ENTERPRISES INC (524000|1)]",@"(?<=\])\.\[[^\]]+\]$",string.Empty));
        Console.WriteLine((Regex.Split("[Purchaser].[All Purchaser].[COMMERCIAL].[ABBOTT ENTERPRISES INC].[ABBOTT ENTERPRISES INC - GENERAL].[GENERAL - ABBOTT ENTERPRISES INC (524000|1)]",@"\]\.\[").Length - 2).ToString());
     */
        Match match = Regex.Match("CustTmplt_PersnlCat_100",@"(?<=^(CustTmplt_PersnlCat_|CustTmplt_CustCat_))\d+$");
        Console.WriteLine(match.Value);
        Console.WriteLine(match.Groups[1]);

        Console.WriteLine(Regex.Match("CustTmplt_CustCat_5467",@"(?<=^(?:CustTmplt_PersnlCat_|CustTmplt_CustCat_))\d+$").Value);
      

    }
}
