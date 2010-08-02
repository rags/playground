.assembly PrintString {}

/*
    Console.WriteLine("Hello, World)"
*/

.method static public void main() il managed
{
    .entrypoint             // this function is application entry point

    .maxstack 8

    
    // *****************************************************
    // Console.WriteLine("Hello, World)";
    // *****************************************************
    ldstr "Hello, World"        // load string onto stack
    
    // Call static System.Console.Writeline function
    // (function pops string from the stack)
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    
    
    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    
    
    // Call the System.Console.Read function
    call int32 [mscorlib]System.Console::Read()
    
    // The pop instruction removes the top element from the stack.
    // (remove number returned by Read() function)
    pop
    // *****************************************************************

    ret
}
