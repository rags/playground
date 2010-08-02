.assembly extern mscorlib{}

.assembly FirstIL
{
	.ver 1:0:0:0
}
.module FirstIL.exe



.class private auto ansi beforefieldinit MyClass
{
	.method public hidebysig void CallMe() //cil managed
	{
		.maxstack 1
		ldstr "In call me"
		call void [mscorlib] System.Console::WriteLine(string)
		ret
	}
    .method public hidebysig specialname rtspecialname instance void .ctor()
    {
        ret
    }
}

.method public hidebysig static void Cool() cil managed
{
	.entrypoint
	.maxstack 1
	.locals init(class MyClass objMyClass)
	ldstr "First one 4 me"
	call void [mscorlib]System.Console::WriteLine(string)
    newobj instance void MyClass::.ctor()
	stloc.0
    ldloc.0                              
    call instance void  MyClass::CallMe()

	call string [mscorlib]System.Console::ReadLine()
	pop
	ret	
}

