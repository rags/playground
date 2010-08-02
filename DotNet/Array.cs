//Filename Array.cs
//css Array.cs - compile 
//Array - to run
class Array
{
public static void Main()
{
int [] a ={1,2,3,4};
int [] a_ ={1,2,3,4};
string [] _a ={"1","2","3","4"};
object [] __a ={"1",2,3,'4'};
char [] ___a ={'1','2','3','4'};
int [] x = new int[2];
x[0] = 89;
x[1] = 23;
System.Console.WriteLine("-----------Before--------------");
foreach(int i in a) System.Console.WriteLine(i);
addOne(a);
  System.Console.WriteLine("-----------After--------------");
foreach(int i in a) System.Console.WriteLine(i);
}

static void addOne(int[] a)
{
for(int i=0;i< a.Length;i++) a[i]++;
}
}
