.assembly XequalN {}


// This program works as C# code:
// int x;
// x = 7;
// Console.WriteLine(x);

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

    // *****************************************************
    // int x;
    // *****************************************************
    .locals init ([0] int32 x)  // Allocate local variable

    // *****************************************************
    // x = 7;
    // *****************************************************
    ldc.i4.7                    // load constant onto stack
    stloc.0                     // store value from stack to var. 0
    
    // *****************************************************
    // Console.WriteLine(x);
    // *****************************************************
    ldloc.0                     // load var.0 onto stack

    // call static System.Console::WriteLine(int32) function.
	call void [mscorlib]System.Console::WriteLine(int32)    

    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}
