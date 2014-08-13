data Node = Leaf Double
     	    | Plus Node Node 
            | Minus Node Node 
            | Div Node Node 
            | Mul Node Node
	    deriving (Show)

eval (Leaf n) = n
eval (Plus lhs rhs) = (eval lhs) + (eval rhs)
eval (Minus lhs rhs) = (eval lhs) - (eval rhs)
eval (Div lhs rhs) = (eval lhs) / (eval rhs)
eval (Mul lhs rhs) = (eval lhs) * (eval rhs)

printTree _ (Leaf n)  = show n
printTree f (Plus lhs rhs)  = f "+" lhs rhs
printTree f (Minus lhs rhs)  = f "-" lhs rhs
printTree f (Div lhs rhs)  = f "*" lhs rhs
printTree f (Mul lhs rhs) = f "/" lhs rhs

inorder = printTree inorderp 
preorder = printTree preorderp 
postorder = printTree postorderp 

inorderp sign lhs rhs = 
	"(" ++ (inorder lhs) ++ " " ++ sign ++ " " ++ (inorder rhs) ++ ")" 

preorderp sign lhs rhs = 
	"(" ++ sign ++ " " ++ (preorder lhs) ++ " " ++ (preorder rhs) ++ ")" 

postorderp sign lhs rhs = 
	"(" ++ (postorder lhs) ++ " " ++ (postorder rhs) ++ " " ++ sign ++ ")" 

tree = (Mul (Plus (Leaf 1) (Mul (Leaf 2) (Leaf 3)))
	    (Div (Leaf 8) (Minus (Leaf 3) (Leaf 2))))
