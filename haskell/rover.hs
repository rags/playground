data Rover = Rover Int Int Direction deriving (Show)
data Direction = North|South|East|West deriving (Show)

left (Rover x y North) = Rover x y West
left (Rover x y West) = Rover  x y South
left (Rover x y South) = Rover x y East
left (Rover x y East) = Rover  x y North

right (Rover x y North) = Rover x y East  
right (Rover x y East) = Rover  x y South
right (Rover x y South) = Rover x y West 
right (Rover x y West) = Rover  x y North

move (Rover x y North) = Rover (x+1) y East 
move (Rover x y East) = Rover  x (y+1) South 
move (Rover x y South) = Rover x (y-1) West 
move (Rover x y West) = Rover  (x+1) y North 


r = right (move (left (move (left (Rover 1 2 North)))))


