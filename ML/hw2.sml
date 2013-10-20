(* all except is a common function used by all_except_option and remove_card*)
fun all_except ([], _) = NONE
  | all_except (head::tail, predicate) = 
    if predicate(head) 
    then SOME tail 
    else 
	case all_except(tail, predicate) of
	    SOME new_tail => SOME(head::new_tail)
	  | NONE => NONE 

(* https://en.wikipedia.org/wiki/Currying *)
fun curry f arg1 arg2 = f(arg1,arg2)

fun map (_, []) = []
  | map (func, x::xs) = func(x)::map(func, xs)
 
fun all_except_option (element, elements) = all_except(elements, curry same_string element)

fun get_substitutions1 ([], _)=[]
  | get_substitutions1(candidates::remaining_candidates, name)  = 
    case all_except_option(name, candidates) of
	SOME matches => matches @ get_substitutions1(remaining_candidates, name)
      | NONE => get_substitutions1(remaining_candidates, name)

fun get_substitutions2 (names_db, name)  = 
    let
	fun substitutions_for([],accumulator) = accumulator
	  | substitutions_for(candidates::remaining_candidates, accumulator) =
	    case all_except_option(name, candidates) of
		SOME matches => substitutions_for(remaining_candidates, accumulator @ matches)
	      | NONE => substitutions_for(remaining_candidates, accumulator)
    in
	substitutions_for(names_db, [])
    end


fun similar_names (names_db, {first=fname, middle=mname, last=lname}) =
    let
	fun replace_fname(new_fname) = {first=new_fname, middle=mname, last=lname}
    in
	({first=fname, middle=mname, last=lname})::map(replace_fname, 
						       get_substitutions2(names_db, fname))
    end

fun card_color ((Diamonds|Hearts), _) = Red
  | card_color ((Clubs|Spades), _) = Black  
	    
fun card_value (_, (Num num)) = num 
  | card_value (_, Ace) = 11
  | card_value (_) = 10

fun remove_card(cards, card, ex) = 
    case all_except(cards, curry op= card) of
	SOME cards' => cards'
      | NONE => raise ex 

fun all_same_color ([]) = true
  | all_same_color (card::[]) = true
  | all_same_color (card1::card2::cards) = 
    card_color(card1)=card_color(card2) andalso all_same_color(card2::cards)

fun sum_cards (cards) =
    let 
	fun sum_cards_([], sum) = sum
	  | sum_cards_(card::cards, sum)  = sum_cards_(cards, sum + card_value(card)) 
    in
	sum_cards_(cards, 0)
    end

fun calc_score(preliminary_score, same_color) =
    (if preliminary_score > 0 
     then (preliminary_score * 3) 
     else ~preliminary_score) div (if same_color then 2 else 1)

fun score (cards, goal) = 
    calc_score(sum_cards(cards) - goal, all_same_color(cards))

fun officiate (cards, moves, goal) =
    let 
	fun play ([],_,held) = score(held, goal)
	  | play (_,[],held) = score(held, goal)
	  | play (card::cards, Draw::moves, held) = 
	    let 
		val new_held = card::held
		val sum = sum_cards(new_held)
	    in
		if sum>goal then score(new_held, goal) else play(cards, moves, new_held)
	    end
	  | play (cards, (Discard card)::moves, held) = 
	    play(cards, moves, remove_card(held, card, IllegalMove))
    in
	play(cards, moves, [])
    end

(* ______________________________________ Challenge ______________________________________ *)

fun add_to_all (lst, value) = map(curry op+ value, lst)

fun sums_for_cards(cards) =
    let
	fun sums_for ([], sums) = sums
	  | sums_for ((_,Ace)::cards, sums)  = 
	    sums_for (cards, add_to_all(sums, 11)) @ sums_for (cards, add_to_all(sums, 1))
	  | sums_for (card::cards, sums)  = 
	    sums_for (cards, add_to_all(sums, card_value(card)))
    in 
	sums_for(cards,[0])
    end

(* Assumes non -ve input only. So default min is 0 *)
fun min (e::[]) = e
  | min (e::rest) =
    let
	val m = min(rest)
    in
	if e<m then e else m
    end

fun score_challenge (cards, goal) = 
    let
	val same_color = all_same_color(cards)
	fun compute_score(sum) =
	    calc_score(sum - goal, same_color)	    
    in
	min(map(compute_score, sums_for_cards(cards)))
    end

fun officiate_challenge (cards, moves, goal) =
    let 
	fun play ([],_,held) = score_challenge(held, goal)
	  | play (_,[],held) = score_challenge(held, goal)
	  | play (card::cards, Draw::moves, held) = 
	    let 
		val new_held = card::held
		val sum = min(sums_for_cards(new_held))
	    in
		if sum>goal then score_challenge(new_held, goal) else play(cards, moves, new_held)
	    end
	  | play (cards, (Discard card)::moves, held) = 
	    play(cards, moves, remove_card(held, card, IllegalMove))
    in
	play(cards, moves, [])
    end
 

(* This function is key to careful_player implementation. It makes all possible move combination 
Ex: for cards [c1,c2,c2] it returns
    [], [draw c1], [draw c1,c2], [draw c1,c2,c3], [draw and discard c1, draw c2,c3] and so on....
Sample output :
 [[], [Draw], [Draw,Discard (Hearts,Ace)], [Draw,Draw], [Draw,Discard (Hearts,Ace),Draw], 
  [Draw,Draw,Discard (Spades,Ace)], [Draw,Draw,Draw]...]
*)
fun moves_combinations(cards) =
   let 
       fun combs (lst, prev, [])=lst 
	 | combs (lst, prev, c::cs) = 
	   let
	       val cur = map(fn l => l@[Draw], prev) @ map(fn l => l@[Draw, Discard c], prev)
	   in
	       combs(lst @ cur, cur, cs)
	   end
   in
       combs([[]],[[]],cards)
end


fun careful_player (cards, goal) = 
    let
	(* returns hand for a move sequence or 
          NONE if value(hand)+10>=goal at any point while evaluating moves 
          This function is similar to 'officiate', but it only simulates evaluation 
          and returns the final hand instead of final score
         *)
	fun hand_for ([],_,hand) = SOME hand
	  | hand_for (Draw::ms, c::cs, hand) = 
	    if sum_cards(hand)+10 < goal then hand_for(ms,cs, c::hand) else NONE
	  | hand_for ((Discard c)::ms, cs, hand) = 
	    hand_for(ms,cs, remove_card(hand, c, IllegalMove))
		    
	(* Find (valid) move sequence with minimum score *)
        fun filter ([], best, _) = best
	  | filter (moves::rest, best_moves, best_score) =
	    case hand_for(moves, cards, []) of
		SOME hand => 
		let 
		    val cur_score = score(hand, goal)
		in
		    if best_score > cur_score
		    then filter(rest, moves, cur_score)
		    else filter(rest, best_moves, best_score)
		end  		    
	      | NONE => filter(rest, best_moves, best_score)
    in
	filter(moves_combinations(cards), [], score([], goal))
    end 

			       

	
