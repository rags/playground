sumprod1 l = (sum (filter odd l), product (filter even l))

sumprod2 [] = (0,1)
sumprod2 (x:xs) = 
	 let (sum,prod) = sumprod xs 
	     in 
	     ((if (even x) then sum else sum+x), if (odd x) then prod else prod*x)

sumprod l =
	 acc_sum_prod l 0 1
	 where
	 acc_sum_prod [] sum prod = (sum,prod)
	 acc_sum_prod (x:xs) sum prod = 
	 	 (acc_sum_prod xs
		 (if (odd x) then sum+x else sum)
 	 	 (if (even x) then (prod*x) else prod))



	 