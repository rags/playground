.assembly Array1 {}

/*
// This program works as C# code:

int[] x = new int[5];
x[0] = 10;
x[1] = 20;

Console.WriteLine("x[0] = " + x[0].ToString());
Console.WriteLine("x[1] = " + x[1].ToString());

Console.WriteLine("Array length = " + x.Length.ToString());

*/

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

   
    // ***********************************************************
    // int[] x;
    // int tmp;    // work variable
    // ***********************************************************
    .locals init ([0] int32[] x,
                  [1] int32 tmp)
      

    // ***********************************************************
    // x = new int[5];
    // ***********************************************************
    ldc.i4.5                        // load constant onto stack
    
    // newarr (create a zero-based, one-dimensional array). 
    // This instruction creates a new array of the specified type 
    // with the number of elements indicated by the value 
    // on the top of the stack. The number of elements 
    // is removed from the stack and reference to new array is placed 
    // on the top of the stack. 
    newarr     [mscorlib]System.Int32

    // Store (pop) value from the stack and place it to local variable 0.
    // After this x contains reference to array allocated in newarr.
	stloc.0
	
	// ***************************************************
	// x[0] = 10;
	// ***************************************************
	ldloc.0             // Load local variable 0 onto stack
	ldc.i4.0		    // Load constant 0 to the stack 
	ldc.i4.s   10	    // Load constant 10 to the stack (s form is used for n > 8)
	
	// pop from stack:
	// 1) array
	// 2) index
	// 3) value
	// and store value in array member.
	// That means, x[0] = 10
	// i4 means that value assigned to array element is Int32
	stelem.i4
	

	// ***************************************************
	// x[1] = 20;
	// ***************************************************
	ldloc.0				// load x onto stack
	ldc.i4.1			// load 1 onto stack
	ldc.i4.s   20		// load 20 onto stack
	stelem.i4			// x[1] = 20
	
	
	// ***************************************************
	// Console.WriteLine("x[0] = " + x[0].ToString());
	// ***************************************************
	ldstr      "x[0] = "            // load string onto stack
				// STACK: "x[0] = "  (stack is shown from local variables)
	
	ldloc.0                         // load variable 0 onto stack
	ldc.i4.0                        // load constant 0 onto stack
				// STACK: "x[0] = " -> x -> 0
	
	// The "ldelema <class>" instruction loads the address of the element 
	// with index (of type native int) in the zero-based 
	// one-dimensional array and places it on the top of the stack. 
	// Arrays are objects  and hence represented by a value of type O. 
	// The return address is a managed pointer (type &).
	ldelema    [mscorlib]System.Int32
				// STACK: "x[0] = " -> pointer to Int32 instance 10
	
	// Call function System.Int32::ToString().
	// On the top of stack we have pointer to Int32 object instance.
	// ToString is applied to this instance and loads to
	// the stack result string.
	// Instance pointer is removed from stack.
	call       instance string [mscorlib]System.Int32::ToString()
				// STACK: "x[0] = " -> "10"
				
					// NOTE: there is no need for boxing here since Int32 
					//       has function ToString.
					//       Line:
					//       Console.WriteLine(n.ToString())
					//       doesn't cause boxing.
					//       Line:
					//       Console.WriteLine("{0}", n);
					//       is written in IL using boxing because
					//       second parameter is converted to Object.

	
	// call System.String::Concat(string, string)
	call       string [mscorlib]System.String::Concat(string, string)	
				// STACK: "x[0] = 10"

	// call System.Console::WriteLine(string)				
	call       void [mscorlib]System.Console::WriteLine(string)
				// STACK: empty
	

	// ***************************************************
	// The same operations with element number 1
	// Console.WriteLine("x[1] = " + x[1].ToString());
	// ***************************************************
	ldstr      "x[1] = "				// load string onto the stack
	ldloc.0								// load variable 0 onto stack (x)
	ldc.i4.1							// load constant 0 onto stack (index)
	ldelema    [mscorlib]System.Int32   // load address if Int32 object x[1] onto stack
	call       instance string [mscorlib]System.Int32::ToString()
	call       string [mscorlib]System.String::Concat(string, string)	
	call       void [mscorlib]System.Console::WriteLine(string)


	// ***********************************************************
	// Console.WriteLine("Array length = " + x.Length.ToString());	
	// ***********************************************************
	
	ldstr      "Array length = "		// load string onto stack
				// STACK: "Array length = "
	ldloc.0								// load variable 0 to stack
				// STACK: "Array length = " -> x
	// push the length (of type native unsigned int) of array on the stack
	ldlen
				// STACK: "Array length = " -> 5
	// Convert to int32, pushing int32 on stack
	conv.i4
				// STACK: "Array length = " -> 5
	// store value from the stack to local variable 1 (tmp)
	stloc.1
				// STACK: "Array length = "
	// load address of variable tmp to the stack
	ldloca.s   tmp
				// STACK: "Array length = " -> &tmp
	// Convert tmp to string
	call       instance string [mscorlib]System.Int32::ToString()
				// STACK: "Array length = " -> "5"
	// call System.String::Concat(string, string)	
	call       string [mscorlib]System.String::Concat(string, string)
				// STACK: "Array length = 5"
	// call System.Console::WriteLine(string)	
	call       void [mscorlib]System.Console::WriteLine(string)
				// STACK: empty
   
    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}
