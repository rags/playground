.assembly Array2 {}

/*
This program works as C# code:

            int[] px = new int[100];
            int i;

            for ( i = 1; i < 100; i++ )
            {
                px[i] = i + 1;
            }

            ShowNumber(px[5]);
            ShowNumber(px[10]);
            

        static void ShowNumber(int n)
        {
            Console.WriteLine(n.ToString());
        }

*/

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8


    // *****************************************************    
    // int[] x;
    // *****************************************************    
    // int i;
    .locals init ([0] int32[] px,
				  [1] int32 i)
    
    // *****************************************************    
    // x = new int[100]
    // *****************************************************    
    ldc.i4.s   100						// load constant onto stack
    newarr     [mscorlib]System.Int32	// allocate Int32 array and place ptr to stack
    stloc.0								// store to variable 0
    
    // *****************************************************    
    // i = 1
    // *****************************************************    
    ldc.i4.1					// load constant onto stack
    stloc.1						// store to variable 1
    
    br.s       CHECK_COUNTER	// goto CHECK_COUNTER
    
START_LOOP:
    // *****************************************************    
	// px[i] = i + 1;
    // *****************************************************    
    ldloc.0						// load variable 0 to stack
								// STACK: px
    ldloc.1						// load variable 1 to stack
                                // STACK; px -> i
    ldloc.1						// load variable 1 to stack
                                // STACK: px -> i -> i
    ldc.i4.1					// load constant to stack
                                // STACK: px -> i -> i -> 1.
    add							// add last two values
                                // STACK: px -> i -> i+1
                                //      (array,index,value)
    stelem.i4					// store value to array element:
                                // array[index] = value
                                // STACK: empty
    // *****************************************************    
    // i = i + 1
    // *****************************************************    
    ldloc.1						// load variable 1 onto stack
    ldc.i4.1					// load constant onto stack
    add							// add
    stloc.1						// store to variable 1
    
CHECK_COUNTER:
    // *****************************************************    
    // if i < 100 goto start f loop
    // *****************************************************    
    ldloc.1						// load variable 1 onto stack
    ldc.i4.s   100				// load constant onto stack
    blt.s      START_LOOP		// if value1 < value2 go to START_LOOP


    // ******************************************
    // ShowNumber(px[5]
    // ******************************************
    ldloc.0                     // load variable 0 onto stack (array)
    ldc.i4.5                    // load constant onto stack (index)
    ldelem.i4                   // load array element to stack
    call       void ShowNumber(int32)   // call ShowNumber
    
    // ******************************************
    // ShowNumber(px[10]
    // ******************************************
    ldloc.0
    ldc.i4.s   10
    ldelem.i4
    call       void ShowNumber(int32)
    
    
    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}

// print int to Console
.method static public void  ShowNumber(int32 n) il managed
{
  .maxstack  1
 
  ldarga.s   n          // load to stack address of argument n
  
  // call Int32::ToString for object pointed by stack element
  call       instance string [mscorlib]System.Int32::ToString()
  
  // call static WriteLine function
  call       void [mscorlib]System.Console::WriteLine(string)
  
  ret
} 


