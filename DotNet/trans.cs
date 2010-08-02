using System.Data;
using System.Data.SqlClient;
using System;
class trans
{
    public static void Main()
    {
        SqlConnection conn = new SqlConnection("server=(local);database=RND;integrated security=SSPI");
        SqlTransaction tran;
        conn.Open();
        SqlCommand comm = new SqlCommand("Insert into tblDepartment(DepartmentName) values('dept6')",conn,tran = conn.BeginTransaction());
        comm.ExecuteNonQuery();
        
        SqlConnection conn1 = new SqlConnection("server=(local);database=RND;uid=sa;pwd=sa;");
        conn1.Open();
        SqlCommand comm1 = new SqlCommand("select max(DepartmentId) from tblDepartment",conn,tran);
        Console.WriteLine((int)comm1.ExecuteScalar());
        tran.Rollback();
        Console.WriteLine((int)comm1.ExecuteScalar());
        conn.Close();
        conn1.Close();
    }
}
