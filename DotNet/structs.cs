struct foo{
int x;
string y;
public static void Main(){
        foo foo1 = getfoo();
        foo foo2 = getfoo();
//        System.Console.WriteLine(foo1==foo2);
        System.Console.WriteLine(foo1.Equals(foo2));
}

 static foo getfoo(){
        foo foo1 = new foo();
        foo1.x=10;
        foo1.y="foo";
        return foo1;
}


}
