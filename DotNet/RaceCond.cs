using System;
public class A {
public static string staticVariableCopiedFromB = B.staticVariable;
public static string staticVariable = "This is a string defined in A";
}

public class B {
public static string staticVariableCopiedFromA = A.staticVariable;
public static string staticVariable = "This is a string defined in B";
}

public class Test {
static void Main(string[] args)
{
Console.WriteLine(A.staticVariableCopiedFromB);
Console.WriteLine(B.staticVariableCopiedFromA==null);
}
}
