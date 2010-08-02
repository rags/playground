.assembly Compare {}

/*
This program works as C# code:

            int x, y, z;
            string s;

            Console.WriteLine("Enter x:");
            s = Console.ReadLine();
            x = Int32.Parse(s);

            Console.WriteLine("Enter y:");
            s = Console.ReadLine();
            y = Int32.Parse(s);

            if ( x < y )
                z = x;
            else
                z = y;

            Console.WriteLine("{0:d}", z);

*/

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

    
	// ***************************************************************
	// int x, y, x;
	// string s;
	// ***************************************************************
    .locals init ([0] int32 x,
                  [1] int32 y,
                  [2] int32 z,
                  [3] string s)

	// ***************************************************************
	// Console.WriteLine("Enter x:");
	// ***************************************************************
	ldstr      "Enter x:"				// load string onto stack
	call  void [mscorlib]System.Console::WriteLine(string)
	
	// ***************************************************************
    // s = Console.ReadLine();
	// ***************************************************************
	call       string [mscorlib]System.Console::ReadLine()
	stloc.3								// store to var. 3
	
	
	// ***************************************************************
    // x = Int32.Parse(s);
	// ***************************************************************
	ldloc.3								// load var. 3 onto stack
	call       int32 [mscorlib]System.Int32::Parse(string)
	stloc.0								// store to var. 0


	// ***************************************************************
	// The same operations for y:
	// Console.WriteLine("Enter y:");
    // s = Console.ReadLine();
    // y = Int32.Parse(s);
	// ***************************************************************
	ldstr      "Enter y:"									// load string onto stack
	call  void [mscorlib]System.Console::WriteLine(string)  // call WriteLine
	call       string [mscorlib]System.Console::ReadLine()  // call ReadLine
	stloc.3													// store to s
	ldloc.3													// load s
	call       int32 [mscorlib]System.Int32::Parse(string)  // call Parse
	stloc.1													// store to y
	
	// ***************************************************************
	// branch
	// if ( x >= y ) goto L_GR;
	// ***************************************************************
	ldloc.0						// load x onto stack (value 1)
	ldloc.1						// load y onto stack (value 2)
	
	// The bge instruction transfers control to target if value1 
	// is greater than or equal to value2
	bge.s      L_GR
	
	// ***************************************************************
	// z = x
	// ***************************************************************
	ldloc.0				// load variable 0 onto stack
	stloc.2				// store to variable 2
	
	// ***************************************************************
	// go to (unconditional branch)
	// ***************************************************************
	br.s       L_CONTINUE
	
	L_GR:
	
	// ***************************************************************
	// z = y
	// ***************************************************************
	ldloc.1				// load variable 1 onto stack
	stloc.2				// store to variable 2
	
	L_CONTINUE:
	
	// ***************************************************************
    // Console.WriteLine("{0:d}", z);
    // NOTE: this line causes boxing.
	// ***************************************************************
	ldstr      "{0:d}"	// load string onto stack
	ldloc.2				// load variable 2 to stack (z)
	
	// The box instruction converts the ‘raw’ valueType 
	// (an unboxed value type) into an instance of type Object 
	// (of type O).
	// Value is removed from stack; object is placed to stack.
	box        [mscorlib]System.Int32
	
	// Call static WriteLine function.
	// It is applied to last two values on the stack:
	// string "{0:d}" and object with number - result of boxing.
	call   void [mscorlib]System.Console::WriteLine(string, object)

    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}
