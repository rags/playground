class A{
int a=10;
}
class B extends A{
int a=20;
}
public class Inheritance{
	public static void main(String [] args){
	A a = new B();
	System.out.println(a.a);
}
}
