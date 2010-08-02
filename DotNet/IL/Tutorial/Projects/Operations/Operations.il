.assembly Operations {}

/*
// This program works as C# code:

            int x, y, z;
            string s;

            Console.WriteLine("Enter x:");
            s = Console.ReadLine();
            x = Int32.Parse(s);

            Console.WriteLine("Enter y:");
            s = Console.ReadLine();
            y = Int32.Parse(s);

            z = x + y;
            Console.Write("x + y = ");
            Console.Write(z);
            Console.WriteLine("");

            z = x - y;
            Console.Write("x - y = ");
            Console.Write(z);
            Console.WriteLine("");

            z = x * y;
            Console.Write("x * y = ");
            Console.Write(z);
            Console.WriteLine("");
*/

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

    // *********************************************************
    // int x, y, z;
    // string s;
    // *********************************************************
	.locals init ([0] int32 x,
           [1] int32 y,
           [2] int32 z,
           [3] string s)

    // *********************************************************
    // Console.WriteLine("Enter x:");
    // *********************************************************
    ldstr      "Enter x:"       // load string onto stack
    call       void [mscorlib]System.Console::WriteLine(string)
    
    // *********************************************************
    // s = Console.ReadLine();
    // *********************************************************
    call       string [mscorlib]System.Console::ReadLine()
    stloc.3                     // store value to var. 3
    
    // *********************************************************
    // x = Int32.Parse(s);
    // *********************************************************
    ldloc.3                     // load variable 3 onto stack
    
    // Call System.Int32::Parse(string)
    // Function pops string from stack and pushes to stack
    // int32 value - result of parsing.
    call       int32 [mscorlib]System.Int32::Parse(string)
    
    stloc.0                     // store value to var. 0
    
    
    
    // *********************************************************
    // Same operations with variable y:
    // Console.WriteLine("Enter y:");
    // s = Console.ReadLine();
    // y = Int32.Parse(s);
    // *********************************************************
    ldstr      "Enter y:"										// load string	
	call       void [mscorlib]System.Console::WriteLine(string) // call
	call       string [mscorlib]System.Console::ReadLine()      // call
	stloc.3                                                     // store to var. 3
	ldloc.3                                                     // load var. 3
	call       int32 [mscorlib]System.Int32::Parse(string)      // call
    stloc.1                                                     // store to var. 1
    
    // ***********************************************
    // z = x + y;
    // ***********************************************
    ldloc.0             // load variable 0 onto stack
	ldloc.1             // load variable 1 onto stack
	
	// pop two values from the stack, add them and push result onto stack
	add
	
	stloc.2             // store to variable 2
	
    // ***********************************************
    // Console.Write("x + y = ");
    // ***********************************************
	ldstr      "x + y = "           // load string onto stack
    call       void [mscorlib]System.Console::Write(string)
    
    // ***********************************************
    // Console.Write(z);
    // ***********************************************
    ldloc.2                         // load variable 2 onto stack
	call       void [mscorlib]System.Console::Write(int32)
	
    // ***********************************************
    // Console.WriteLine("");
    // ***********************************************
	ldstr      ""                   // load string onto stack
    call       void [mscorlib]System.Console::WriteLine(string)

    // ***********************************************
    // Same operations with subtraction
    // z = x - y;
    // Console.Write("x - y = ");
    // Console.Write(z);
    // Console.WriteLine("");
    // ***********************************************
    ldloc.0
	ldloc.1
	sub
	stloc.2
	ldstr      "x - y = "
    call       void [mscorlib]System.Console::Write(string)
    ldloc.2
	call       void [mscorlib]System.Console::Write(int32)
	ldstr      ""
    call       void [mscorlib]System.Console::WriteLine(string)

    // ***********************************************
    // Same operations with multiplication
    // z = x - y;
    // Console.Write("x - y = ");
    // Console.Write(z);
    // Console.WriteLine("");
    // ***********************************************
    ldloc.0
	ldloc.1
	mul
	stloc.2
	ldstr      "x * y = "
    call       void [mscorlib]System.Console::Write(string)
    ldloc.2
	call       void [mscorlib]System.Console::Write(int32)
	ldstr      ""
    call       void [mscorlib]System.Console::WriteLine(string)

    
    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}
