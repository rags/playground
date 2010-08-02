.assembly PInvoke {}

/*
// This program works as C# code:

        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern int GetComputerName(
            [MarshalAs(UnmanagedType.LPTStr)]
            StringBuilder buffer,
            ref int size);

        [DllImport("User32.dll", CharSet = CharSet.Auto)]
        public static extern int MessageBox(
            IntPtr hWnd,
            [MarshalAs(UnmanagedType.LPTStr)]
            string lpText,
            [MarshalAs(UnmanagedType.LPTStr)]
            string lpCaption,
            int uType);

        
		[STAThread]
		static void Main(string[] args)
		{
            string s = "Computer name";
            int n = 100;
            StringBuilder sName = new StringBuilder(100);

            GetComputerName(sName, ref n);

            MessageBox(IntPtr.Zero, sName.ToString(), s, 0);
        }

*/

// API functions
.method public hidebysig static pinvokeimpl("kernel32.dll" autochar winapi) 
        int32  GetComputerName(class [mscorlib]System.Text.StringBuilder  marshal( lptstr) buffer,
                               int32& size) cil managed preservesig
{
}

.method public hidebysig static pinvokeimpl("User32.dll" autochar winapi) 
        int32  MessageBox(native int hWnd,
                          string  marshal( lptstr) lpText,
                          string  marshal( lptstr) lpCaption,
                          int32 uType) cil managed preservesig
{
}


.method static public void main() il managed
{
    .entrypoint

    .maxstack 8

    // *******************************************************************    
    // string s;
    // int n;
    // StringBuilder sName;
    // *******************************************************************    
    .locals ([0] string s,
             [1] int32 n,
             [2] class [mscorlib]System.Text.StringBuilder sName)

    // ********************************************************************           
    // s = "Computer name";       
    // ********************************************************************           
    ldstr      "Computer name"          // load string constant onto stack
    stloc.0                             // store to variable 0
    
    // ********************************************************************           
    // n = 100;
    // ********************************************************************           
    ldc.i4.s   100                      // load constant onto stack
    stloc.1                             // store to variable 1
    
    // ********************************************************************           
    // sName = new StringBuilder(100);     
    // ********************************************************************           
    ldc.i4.s   100                      // load constant 0 on stack
    
    // The newobj instruction creates a new object or a new instance of an object.
    // It calls constructor and pushes initialized object reference onto stack.
    newobj     instance void [mscorlib]System.Text.StringBuilder::.ctor(int32)
    
    stloc.2                             // store to variable 2
    
    // ********************************************************************           
    // GetComputerName(sName, ref n);
    // ********************************************************************           
    ldloc.2                             // load variable 2
    ldloca.s   n                        // load address of n
    call       int32 GetComputerName(class [mscorlib]System.Text.StringBuilder, int32&)
    pop                                 // pop value returned by function
    
    // ********************************************************************           
    // MessageBox(IntPtr.Zero, sName.ToString(), s, 0);
    // ********************************************************************           
    ldsfld     native int [mscorlib]System.IntPtr::Zero  // load static field of a class
    ldloc.2                                              // load variable 2
    // call virtual method ToString
    callvirt   instance string [mscorlib]System.Text.StringBuilder::ToString()
    ldloc.0                                             // load variable 0 on stack
    ldc.i4.0                                            // load constant 0
    // call MessageBox
    call       int32 MessageBox(native int, string, string, int32)
    pop                                                 // pop value returned by function
    
 
    ret
}
