.assembly Unsafe {}

/*
// This program works as C# code:

int[] nArray = new int[5];
int i;
int* pCurrent;

fixed ( int* pArray = nArray )
{
    pCurrent = pArray;

    for ( i = 0; i < 5; i++ )
    {
        *pCurrent++ = i + 1;
    }
}

for ( i = 0; i < 5; i++ )
{
    Console.WriteLine(nArray[i].ToString());
}

*/

.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

    // ************************************************************************* 
    // int[] nArray;
    // int i;
    // int* pCurrent;
    // ************************************************************************* 
    .locals ([0] int32[] nArray,
             [1] int32 i,
             [2] int32* pCurrent,
             [3] int32& pinned pArray)
             
             /*
             About pinned keyword:
             
             The signature encoding for pinned shall appear only in signatures that 
             describe local variables.  While a method with a pinned local variable 
             is executing the VES shall not relocate the object to which the local 
             refers.  That is, if the implementation of the CLI uses a garbage 
             collector that moves objects, the collector shall not move objects 
             that are referenced by an active pinned local variable.
             */

    
    // **************************************************************************       
    // nArray = new int[5];
    // **************************************************************************       
    ldc.i4.5                            // load constant 5 onto stack
    newarr     [mscorlib]System.Int32   // create array Int32[5]
    stloc.0                             // store value from stack to local var. o
    
    // **************************************************************************       
    // pArray = nArray    (pArray = &nArray[0])
    // **************************************************************************       
    ldloc.0                             // load variable 0 onto stack (array)
    ldc.i4.0                            // load constant 0 onto stack (index)
    ldelema    [mscorlib]System.Int32   // load address of array[index] to stack
    stloc.3                             // store value from stack to local var. 3
    
    // **************************************************************************       
    // pCurrent = pArray;
    // **************************************************************************       
    ldloc.3                             // load variable 3 onto stack
    conv.i                              // convert to native int, pushing native int on stack
    stloc.2                             // store to variable 2
    
    // **************************************************************************       
    // i = 0
    // **************************************************************************       
    ldc.i4.0                            // load constant 0 onto stack
    stloc.1                             // store value to var. 1
    
    // **************************************************************************       
    // goto CHECK_COUNTER
    // **************************************************************************       
    br.s       CHECK_COUNTER
    
START_LOOP:  

    // **************************************************************************       
    // *pCurrent++ = i + 1                                          [STACK]
    // ************************************************************************** 
    // 1) keep old pCurrent value on the stack and increment pCurrent      
    ldloc.2             // load variable 2 onto stack            [pCurrent]
    dup                 // duplicate the top value of the stack  [pCurrent pCurrent]
    ldc.i4.4            // load constant 4 onto stack            [pCurrent pCurrent 4]
    add                 // add                                   [pCurrent pCurrent + 4]
    stloc.2             // store from stack to variable 2        [pCurrent]
    
    // 2) write (i+1) by old pCurrent value kept on the stack
    ldloc.1             // load variable 1 onto stack            [pCurrent i]
    ldc.i4.1            // load constant 1 onto stack            [pCurrent i 1]
    add                 // add                                   [pCurrent i+1]
    //                                                            address  value
    stind.i4            // store value by address                [empty]
    
    // **************************************************************************       
    // i = i + 1
    // **************************************************************************       
    ldloc.1             // load variable 1 onto stack
    ldc.i4.1            // load constant 1 onto stack
    add                 // add
    stloc.1             // store to variable 1
    
CHECK_COUNTER:

    // **************************************************************************       
    // if (i < 5) goto START_LOOP;
    // **************************************************************************       
    ldloc.1                     // load variable 1 onto stack
    ldc.i4.5                    // load constant 5 onto stack
    blt.s      START_LOOP       // goto if less
    
    // **************************************************************************       
    // pArray = 0               fixed block finished
    // **************************************************************************       
    ldc.i4.0                    // load constant 0 to stack
    conv.u                      // convert to native unsigned  int, pushing native int on stack
    stloc.3                     // store in variable 3
    
    // **************************************************************************       
    // i = 1
    // **************************************************************************       
    ldc.i4.0                    // load constant 0 onto stack
    stloc.1                     // store to variable 1
    
    
    // **************************************************************************       
    // goto CHECK_COUNTER1
    // **************************************************************************       
    br.s       CHECK_COUNTER1
    
START_LOOP1:  

    // **************************************************************************       
    // Console.WriteLine(nArray[i].ToString());
    // **************************************************************************       
    ldloc.0                             // load variable 0 (array)
    ldloc.1                             // load constant 1 (index)
    ldelema    [mscorlib]System.Int32   // load address of array[index] to stack
    // Call ToString for instance from stack
    call       instance string [mscorlib]System.Int32::ToString()
    // call static WriteLine passing string from stack
    call       void [mscorlib]System.Console::WriteLine(string)
    
    // **************************************************************************       
    // i = i + 1
    // **************************************************************************       
    ldloc.1                             // load variable 1
    ldc.i4.1                            // load constant 1
    add                                 // add
    stloc.1                             // store to variable 1
    
CHECK_COUNTER1:  

    // **************************************************************************       
    // if ( i < 5 ) goto START_LOOP1
    // **************************************************************************       
    ldloc.1                             // load variable 1
    ldc.i4.5                            // load constant 5
    blt.s      START_LOOP1              // goto if less
    

    // *****************************************************************
    ldstr "Press Enter to continue"
    call   void [mscorlib]System.Console::WriteLine(class System.String)
    call int32 [mscorlib]System.Console::Read()
    pop
    // *****************************************************************

    ret
}
