
//  Microsoft (R) .NET Framework IL Disassembler.  Version 1.1.4322.573
//  Copyright (C) Microsoft Corporation 1998-2002. All rights reserved.

.assembly extern mscorlib
{
  .ver 0:0:0:0
}
.assembly FirstIL
{
  .ver 1:0:0:0
}
.module FirstIL.exe
// MVID: {C7E2BA9E-64A9-4781-814D-0733D1B0FBAE}
.imagebase 0x00400000
.subsystem 0x00000003
.file alignment 512
.corflags 0x00000001
// Image base: 0x06e00000
//
// ============== CLASS STRUCTURE DECLARATION ==================
//
.class private auto ansi beforefieldinit MyClass
       extends [mscorlib]System.Object
{
} // end of class MyClass


// =============================================================


// =============== GLOBAL FIELDS AND METHODS ===================

//Global methods
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.method public hidebysig static void  Cool() cil managed
{
  .entrypoint
  // Code size       29 (0x1d)
  .maxstack  1
  .locals init (class MyClass V_0)
  IL_0000:  ldstr      "First one 4 me"
  IL_0005:  call       void [mscorlib]System.Console::WriteLine(string)
  IL_000a:  newobj     instance void MyClass::.ctor()
  IL_000f:  stloc.0
  IL_0010:  ldloc.0
  IL_0011:  call       instance void MyClass::CallMe()
  IL_0016:  call       string [mscorlib]System.Console::ReadLine()
  IL_001b:  pop
  IL_001c:  ret
} // end of global method Cool


// =============================================================


// =============== CLASS MEMBERS DECLARATION ===================
//   note that class flags, 'extends' and 'implements' clauses
//          are provided here for information only

.class private auto ansi beforefieldinit MyClass
       extends [mscorlib]System.Object
{
  .method public hidebysig instance void 
          CallMe() cil managed
  {
    // Code size       11 (0xb)
    .maxstack  1
    IL_0000:  ldstr      "In call me"
    IL_0005:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_000a:  ret
  } // end of method MyClass::CallMe

  .method public hidebysig specialname rtspecialname 
          instance void  .ctor() cil managed
  {
    // Code size       1 (0x1)
    .maxstack  8
    IL_0000:  ret
  } // end of method MyClass::.ctor

} // end of class MyClass


// =============================================================

//*********** DISASSEMBLY COMPLETE ***********************
