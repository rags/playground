val only_capitals = List.filter (fn s => Char.isUpper(String.sub(s,0)));

val (longest_string1, longest_string2, longest_string_helper) = 
	let
		fun str_len_cmp cmp (str1, str2) = 
			if cmp(String.size(str1),String.size(str2)) 
			then str1 
			else str2
	in
		(foldl (str_len_cmp op>) "", 
		 foldl (str_len_cmp op>=) "", 
		 fn cmp => foldl (str_len_cmp cmp)  "")
	end

val longest_string3 = longest_string_helper op> (* OR fn(i,j) => i>j *)

val longest_string4 = longest_string_helper op>= (* OR fn(i,j) => i>=j *)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = String.implode o List.rev o String.explode


fun first_answer f [] = raise NoAnswer
  | first_answer f (x::xs) = case (f x) of
							   SOME value => value
							 | NONE => first_answer f xs

fun all_answers f [] = SOME []
  | all_answers f (x::xs) = case (f x) of 
							   SOME lst => 
							   (case (all_answers f xs) of 
								   SOME rest => SOME (lst @ rest)
								 | NONE => NONE)
							 | NONE => NONE  

val count_wild_and_ = (g (fn () => 1)) 
val count_wildcards = count_wild_and_ (fn _ => 0)
val count_wild_and_variable_lengths = count_wild_and_ (fn str => String.size(str))

fun count_some_var(str, pattern) =
	(g (fn () => 0) (fn var => if var=str then 1 else 0) pattern)

fun check_pat pattern =
	let 
		fun collect_vars(pattern,lst) =
			case pattern of 
				Variable x => x::lst
			  | TupleP ps  => List.foldl (fn (pat, l) => collect_vars(pat, l)) lst ps
			  | ConstructorP(_,pat) => collect_vars(pat, lst)
			  | _ => lst
		
		fun has_no_dups [] = true
		  | has_no_dups (x::xs) = 
			(not (List.exists (fn cur => x=cur) xs)) andalso (has_no_dups xs)
	in
		has_no_dups(collect_vars(pattern,[]))
	end

fun match(value, pattern) = 
	let 
		fun collect_vars (value, pattern, accumulator)=
			case (value, pattern) of 
				(v, Variable s) => SOME ((s,v)::accumulator)
			  | (_, Wildcard) => SOME accumulator
			  | (Unit, UnitP) => SOME accumulator
			  | (Const c1, ConstP c2) => if c1=c2 then (SOME accumulator) else NONE
			  | (Tuple tlst, TupleP plst) =>
				((case (all_answers match (ListPair.zipEq(tlst, plst))) of
					 SOME lst => SOME (accumulator @ lst)
				   | NONE => NONE) 
				 handle UnequalLengths => NONE)
			  | (Constructor (n1, v), ConstructorP (n2, p)) => 
				if n1=n2 then collect_vars(v, p, accumulator) else NONE  
			  | _  => NONE
	in
		collect_vars(value, pattern,[])
	end


fun first_match value plist =
	(SOME (first_answer (fn p => match(value, p)) plist) handle NoAnswer => NONE)


exception TypeErr

fun typecheck_pattern typedefs pattern =
	let
		fun find_type(name, typ)=
			case (List.find (fn (constr, dtype, t) =>constr = name andalso t=typ) typedefs) of
				SOME (c,t,dt) => t
			  | NONE => raise TypeErr

		fun typecheck pat =
			case pat of
				Wildcard => Anything
			  | Variable v => Anything
			  | UnitP => UnitT
			  | ConstP c => IntT 
			  | TupleP ps => TupleT(map typecheck ps)  
			  | ConstructorP (n,p) => 
				Datatype (find_type (n,(typecheck p)))
	in
		(typecheck pattern)
	end

							

fun typecheck_patterns(typedefs,patterns) =
	let
		fun generic (t,Anything) = t
		  | generic (Anything, t) = t
		  | generic ((TupleT ts1),(TupleT ts2)) = TupleT (map generic (ListPair.zipEq(ts1,ts2)))
		  | generic (a,b) = if a=b then a else raise TypeErr
	in
		((SOME (foldl generic Anything (map (typecheck_pattern typedefs) patterns))) handle _ => NONE)

	end								
		
