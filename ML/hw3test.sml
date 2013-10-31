(* Homework3 Simple Test*)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)

val test1 = only_capitals ["A","B","C"] = ["A","B","C"]

val test2 = longest_string1 ["A","bc","C"] = "bc"

val test3 = longest_string2 ["A","bc","C"] = "bc"

val test4a= longest_string3 ["A","bc","C"] = "bc"

val test4b= longest_string4 ["A","B","C"] = "C"

val test5 = longest_capitalized ["A","bc","C"] = "A";

val test6 = rev_string "abc" = "cba";

val test7 = first_answer (fn x => if x > 3 then SOME x else NONE) [1,2,3,4,5] = 4

val test8 = all_answers (fn x => if x = 1 then SOME [x] else NONE) [2,3,4,5,6,7] = NONE

val test9a = count_wildcards Wildcard = 1
val test9a1 = count_wildcards(TupleP[Wildcard,TupleP[Wildcard,Wildcard, Variable("as")], Variable("xx")]) = 3

val test9b = count_wild_and_variable_lengths (Variable("a")) = 1
val test9b1 = count_wild_and_variable_lengths(TupleP[Wildcard,TupleP[Wildcard,Wildcard, Variable("as")], Variable("x")]) = 6

val test9c = count_some_var ("x", Variable("x")) = 1;

val test10 = check_pat (Variable("x"))
val test10_1 = check_pat (ConstructorP("df", TupleP[Variable("x"),Variable("y"),Variable("z")])) 
val test10_2 = check_pat (TupleP[ConstructorP("df", TupleP[Variable("x"),Variable("y"),Variable("z")]), Variable("x")])=false 

val test11 = match (Const(1), UnitP) = NONE

val test11_1 = match (Constructor("df", Tuple[Const 1, Unit, Const 1]),ConstructorP("df", TupleP[Variable("x"),Variable("y"), ConstP 1])) = SOME [("x", Const 1), ("y", Unit)];

val test12 = first_match Unit [UnitP] = SOME []

val test12_1 = first_match (Constructor("df", (Tuple[Const 1, Unit, Const 1])))
							[UnitP, 
							 (ConstructorP("df", (TupleP[Variable("x"),
													   Variable("y"), 
													   ConstP 11]))),
							 (ConstructorP("df", (TupleP[Variable("x"),
													   Variable("y"), 
													   ConstP 1]))), ConstP 11] = SOME [("x", Const 1), ("y", Unit)];

val test13 = typecheck_patterns([],[TupleP[Variable("x"),Variable("y")], TupleP[Wildcard,Wildcard]]) = SOME (TupleT [Anything,Anything]);
val test13_1 = typecheck_patterns([("foo","bar",IntT)],[TupleP[Variable("x"),Variable("y")], TupleP[Wildcard, ConstructorP("foo", ConstP 12)]]) = SOME (TupleT [Anything,Datatype "bar"]);
val test13_2 = typecheck_patterns([],[TupleP[Wildcard,Wildcard],
TupleP[Wildcard,TupleP[Wildcard,Wildcard]], TupleP[ConstP 12,Wildcard]]) = SOME (TupleT [IntT,TupleT[Anything,Anything]]);
val test13_3 = typecheck_patterns([],[UnitP, TupleP[Wildcard,Wildcard], ConstP 1]) = NONE;
val test13_4 = typecheck_patterns([("foo1","bar1",IntT),("foo2","bar2",UnitT)],[ConstructorP("foo1", ConstP 1), ConstructorP("foo2",UnitP)]) = NONE;

val Q13l = typecheck_patterns([("foo1","bar1",Datatype "bar2"),("foo2","bar2",UnitT)],
                                  [ConstructorP("foo1", Variable "x")]) = NONE;

