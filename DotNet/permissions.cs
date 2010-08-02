//use "csc permissions.cs" to compile to permisssions.exe
using System;
/*

//[Flags]//Not really required
enum Permissions
{
    None = 0,
    Read = 1,
    Write = 2,
    Execute = 4,
    Delete = 8,
    Update = 16,
    Alter = 32,
    PermX = 64,
    permY = 128
}
*/
[Flags]//Not really required
public enum Privilege : long
{
    None,
    CostUtilizationViews,
    CostUtilizationTemplates,
    CostUtilizationModels = 4,
    HealthProductivityViews = 8,
    HealthProductivityTemplates = 16,
    HealthProductivityModels = 32,
    QualityOutcomesViews = 64,
    QualityOutcomesTemplates = 128,
    QualityOutcomesModels =256,
    CostUtilizationDrillthru =   512,
    CostUtilizationCorpBenchmarks = 1024,
    CostUtilizationExtBenchmarks = 2048,
    HealthProductivityDrillthru = 4096,
    HealthProductivityCorpBenchmarks = 8192,
    HealthProductivityExtBenchmarks = 16384,
    QualityOutcomesDrillthru = 32768,
    QualityOutcomesCorpBenchmarks = 65536,
    QualityOutcomesExtBenchmarks = 131072,
    PromoteKeyIndicators = 262144,
    PromoteStandardReports =  524288,
    PromoteStoredAnalyses = 1048576,
    DemoteKeyIndicators = 2097152,
    DemoteStandardReports = 4194304,
    DemoteStoredAnalyses = 8388608,
    DeleteKeyIndicators = 16777216,
    DeleteStandardReports = 33554432,
    DeleteStoredAnalyses = 67108864,
    PersonalKeyIndicatorCatlg = 134217728,
    PersonalStoredAnalysisCatlg = 268435456,
    BatchReportingControl = 536870912,
    CommunicationSettings = 1073741824,
    DefaultLogic = 2147483648,
//    All = 4294967295 //long.MaxValue
    //if a new permission is added change the all value appropriately
}
class CheckPerms
{
    public static void Main(string [] _args)
    {
        if(_args.Length>0)
            try
            {
                Privilege p  = (Privilege)long.Parse(_args[0]);
                System.Console.WriteLine("Previleges : " + p + p.ToString().Split(',').Length);
                /*

                System.Console.WriteLine("Previleges : " + (p & Previlege.DefaultLogic));
                System.Console.WriteLine("Previleges : " + (p & Previlege.BatchRptingControl));
                System.Console.WriteLine("Previleges : " + (p & Previlege.CUViews));
                System.Console.WriteLine("Previleges : " + (p & Previlege.DemoteSR));
                System.Console.WriteLine("Previleges : " + (p & Previlege.HPCorpBenchmarks));
                */
            }
            catch{}
        //else System.Console.WriteLine((long)Previlege.All);
    }
    /*
    public static void Main()
    {
        int [] userPerms = GetRandomPermission();
        System.Console.WriteLine("User 1 has read permission? : " + CheckPerm(userPerms[0],Permissions.Read));
        System.Console.WriteLine("User 1 has read permission? : " + (CheckPerm((Permissions)userPerms[0],Permissions.Read)==Permissions.Read));
        System.Console.WriteLine("User 2 has no write permission? : " + (CheckPerm((Permissions)userPerms[1],Permissions.Write)==Permissions.None));
        System.Console.WriteLine("User 3 has no Execute permission? : " + !CheckPerm(userPerms[2],Permissions.Execute));
        System.Console.WriteLine("User 4 has no read permission? : " + (CheckPerm((Permissions)userPerms[3],Permissions.Read)==Permissions.None));
        for(int i=0;i<userPerms.Length;i++)
            System.Console.WriteLine("User " + (i+1) + " : " + (Permissions)userPerms[i] + " ("+userPerms[i]+")");
        //(Permissions)userPerms[i] will get comma seperated string representation of aggregated enum only if Flags Attribute is used
        System.Console.WriteLine(Math.Pow(2,64));
        System.Console.WriteLine(562949953421312*2);
        System.Console.WriteLine(Math.Pow(2,49)*2);
        System.Console.WriteLine(Math.Pow(2,50));
        System.Console.WriteLine(Pow(2,63));
        System.Console.WriteLine(int.MaxValue + " " + long.MaxValue);
        System.Console.WriteLine(uint.MaxValue + " " + ulong.MaxValue);

    }

    static int [] GetRandomPermission()
    {
        return new int [] {
                            (int)(Permissions.Read | Permissions.Write | Permissions.Execute),//user 1
                            (int)(Permissions.Read | Permissions.Execute | Permissions.Update),//user 2
                            (int)(Permissions.Read | Permissions.Read | Permissions.Read), //user 3: only read. can repeat- doesnt make a differnce
                            (int)(Permissions.Read | Permissions.Write)
                           };
    }

    static bool CheckPerm(int userPerm,Permissions perm)
    {
        return (userPerm & (int)perm) > 0;
    }

    ///return Permission.None if the permisssion is not there or return==perm 
    static Permissions CheckPerm(Permissions userPerm,Permissions perm)
    {
        return (userPerm & perm);
    }
    static ulong Pow(int x,int y)
    {
       ulong result = 1;
        ulong _x = (ulong)x;
       for(int i=0;i<y;i++) result *= _x;
       return result;
    }
*/
}
