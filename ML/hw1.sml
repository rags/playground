fun is_older((year1,mon1,day1):(int * int * int), (year2,mon2,day2):(int * int * int)) =
    year1 < year2 orelse (year1=year2 andalso (mon1<mon2 orelse (mon1=mon2 andalso day1<day2)))

(*Following 2 funs are not used. They are Version 0. I have left them to demonstrate my
  first solution used recursing as taught in the class and then later enhanced.
---------------------------------------------------------------------------------------
 *)
(* First cut unused*)
fun number_in_month_v0(dates:(int * int * int) list,month:int) = 
    if null dates
    then 0
    else number_in_month_v0(tl dates,month) + (if (#2 (hd dates))=month then 1 else 0)


(* First cut unused*)
fun number_in_months_v0(dates:(int * int * int) list,months:int list) =
    if null months
    then 0
    else number_in_month_v0(dates, hd months) + number_in_months_v0(dates, tl months)
(* ----------------------------------------  *)

fun number_in_month(dates:(int * int * int) list, month:int) = 
    foldr (fn (date,cnt) => cnt + (if (#2 date)=month then 1 else 0)) 0 dates

fun number_in_months(dates:(int * int * int) list, months:int list) =
    foldr (fn (month,cnt) => cnt + number_in_month(dates, month)) 0 months

fun dates_in_month(dates:(int * int * int) list, month:int) = 
    foldr (fn (date, ret_list) => if (#2 date)=month then date::ret_list else ret_list) [] dates

fun dates_in_months(dates:(int * int * int) list, months:int list) =
    foldr (fn (month,ret_list) => dates_in_month(dates, month) @ ret_list) [] months

    
(* Polymorphic to support both int and string lists*)
fun get_nth(str_list, n) =
    if n=1
    then hd str_list
    else get_nth(tl str_list,n-1)

fun date_to_string((year,mon,day):(int * int * int)) =
    get_nth(["January", "February", "March", "April",
	     "May", "June", "July", "August", "September", 
	     "October", "November", "December"], mon) ^
    " " ^ Int.toString(day) ^
    ", " ^ Int.toString(year);

fun number_before_reaching_sum(sum:int,lst:int list)=
    let 
	fun number_before_reaching_sum_(sum_so_far:int, n:int, (x::xs):int list)=
	    if sum_so_far + x >= sum
	    then n
	    else number_before_reaching_sum_(sum_so_far+x, n+1, xs)
    in
	number_before_reaching_sum_(0, 0, lst)
    end

val days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

fun what_month(days:int)=
    number_before_reaching_sum(days, days_in_months) + 1

fun month_range(from:int, to:int) =
    if from>to
    then []
    else what_month(from)::month_range(from+1,to)

fun oldest(dates:(int * int * int) list)=
    foldr (fn (cur_date, oldest) => if (isSome(oldest) andalso is_older(valOf oldest, cur_date)) 
				    then oldest else (SOME cur_date)) NONE dates


fun dedup(input:int list)=
    rev (foldl (fn (cur, ret_list) => if (List.exists (fn e=>e=cur) ret_list) 
				      then ret_list 
				      else cur::ret_list) 
	       [] input)

fun number_in_months_challenge(dates:(int * int * int) list, months:int list) =
    number_in_months (dates, dedup(months))

fun dates_in_months_challenge(dates:(int * int * int) list, months:int list) =
    dates_in_months (dates, dedup(months))


fun last_day_of_month(mon:int, year:int) = 
    if mon=2 andalso ((year mod 4 = 0 andalso year mod 100 <> 0) orelse year mod 400 = 0)
    then
	29
    else get_nth(days_in_months,mon)

fun reasonable_date((year,mon,day):(int * int * int)) =
    year > 0 andalso mon > 0 andalso mon<=12 andalso day>0 andalso day <= last_day_of_month(mon,year)

