lastButOne :: [Maybe a] ->  Maybe a 
lastButOne [] = Nothing
lastButOne (x:xs) = lastButOne xs
lastButOne [x] = Nothing
lastButOne (x:_:[]) = x

