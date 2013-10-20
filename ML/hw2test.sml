(* Homework2 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)

val test1 = all_except_option("string", ["string"]) = SOME []
 
val test2 = get_substitutions1([["foo"],["there"]], "foo") = []
val test21 = get_substitutions1([["Fred","Fredrick"],
				 ["Elizabeth","Betty"],
				 ["Freddie","Fred","F"]],"Fred") =
	      ["Fredrick","Freddie","F"]


val test3 = get_substitutions2([["foo"],["there"]], "foo") = []
val test31 = get_substitutions1([["Fred","Fredrick"],
				 ["Elizabeth","Betty"],
				 ["Freddie","Fred","F"]],"Fred") =
	     ["Fredrick","Freddie","F"]

val test4 = similar_names([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]], {first="Fred", middle="W", last="Smith"}) =
	    [{first="Fred", last="Smith", middle="W"}, {first="Fredrick", last="Smith", middle="W"},
	     {first="Freddie", last="Smith", middle="W"}, {first="F", last="Smith", middle="W"}]

val test5 = card_color((Clubs, Num 2)) = Black
val test51 = (card_color((Hearts, Ace)), 
	      card_color((Spades, Ace)),
	      card_color(Diamonds, Ace)) = (Red, Black, Red)

val test6 = card_value((Clubs, Num 2)) = 2
val test61 = (card_value((Clubs, Ace)), 
	     card_value(Clubs, Num 10), 
	     card_value((Clubs, King))) = (11, 10, 10)

val test7 = remove_card([(Hearts, Ace)], (Hearts, Ace), IllegalMove) = []



val test8 = all_same_color([(Hearts, Ace), (Hearts, Ace)]) = true
val test81 = all_same_color([(Hearts, Ace), (Diamonds, Ace), (Hearts, Num 2)]) = true
val test82 = all_same_color([(Hearts, Ace), (Hearts, Ace), (Clubs, Ace)]) = false

val test9 = sum_cards([(Clubs, Num 2),(Clubs, Num 2)]) = 4
val test91 = sum_cards([(Clubs, Num 2), (Clubs, Ace), (Hearts, Jack)]) = 23


val test10 = score([(Hearts, Num 2),(Clubs, Num 4)],10) = 4
val test101 = score([(Hearts, Num 2),(Clubs, Num 10)],10) = 6
val test102 = score([(Hearts, Num 2),(Diamonds, Num 4)],10) = 2
val test103 = score([(Hearts, Num 2),(Diamonds, Num 10)],10) = 3



val test11 = officiate([(Hearts, Num 2),(Clubs, Num 4)],[Draw], 15) = 6

val test12 = officiate([(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)],
                       [Draw,Draw,Draw,Draw,Draw],
                       42)
             = 3

val test13 = ((officiate([(Clubs,Jack),(Spades,Num(8))],
                         [Draw,Discard(Hearts,Jack)],
                         42);
               false) 
              handle IllegalMove => true)
             
             
val test3a_1 = 
    let
    	val c1 = (Hearts,Ace)
	val c2 = (Spades,Ace)
    in [
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],99)=0,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],89)=0,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],53)=4,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],52)=3,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],51)=2,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],50)=1,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],49)=0,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],48)=3,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],47)=6,
	score_challenge([c1,c2,c2,c2,c2,c2,c2,c2,c2],46)=7
    ]
    end;



val test3a_2 = 
    let
	val cards= [(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Hearts,Ace)]
	val moves1 =[Draw,Draw,Draw,Draw,Draw]

    in [
 	officiate_challenge(cards, moves1, 44) = 0,
 	officiate_challenge(cards, moves1, 43) = 3,
 	officiate_challenge(cards, moves1, 42) = 6,
 	officiate_challenge(cards, moves1, 41) = 7,
 	officiate_challenge(cards, moves1, 40) = 6
    ]
    end;


		
val test3b = 
let
    val cards1 = [(Spades,Num 7),(Hearts,King),(Clubs,Ace),
		  (Diamonds,Num 2)]
    val cards2 = [(Spades,Num 8),(Hearts,King),(Clubs,Ace),
		  (Diamonds,Num 2)]
    val cards3 = [(Spades,Ace),(Hearts,Queen),(Spades,Num 7)]
in
    [
      officiate(cards1, careful_player(cards1, 18), 18) = 0,
      officiate(cards1, careful_player(cards1,  8),  8) = 4,
      officiate(cards2, careful_player(cards2,  8),  8) = 4,
      officiate(cards2, careful_player(cards2, 18), 18) = 3,
      officiate(cards2, careful_player(cards2, 20), 20) = 0,
      officiate(cards2, careful_player(cards2, 21), 21) = 0,
      officiate(cards3, careful_player(cards3, 21), 21) = 4

    ]
end;



