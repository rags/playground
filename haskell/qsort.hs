qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++ qsort (filter (>= x) xs)

--tests
--qsort [4,6,1,9,-1,0,-5,0]