tree grammar ExpTreeParser;
options {
    language=Python; 
    tokenVocab=Exp;
}
@header{
    from common.nodes import *
} 

exp returns [node]:(theNode=plus|theNode=minus|theNode=div|theNode=mult|theNode=leaf){
$node=$theNode.node
};

plus returns [node]:^(OP_PLUS lhs=exp rhs=exp){
            $node = AddOperator($lhs.node,$rhs.node)
};

minus returns [node]: ^(OP_MINUS lhs=exp rhs=exp){
            $node = SubstractOperator($lhs.node,$rhs.node)
};

mult returns [node]: ^(OP_MULT lhs=exp rhs=exp){
            $node = MultiplyOperator($lhs.node,$rhs.node)
};

div returns [node]: ^(OP_DIV lhs=exp rhs=exp){
            $node = DivideOperator($lhs.node,$rhs.node)
};

leaf returns [node]: OPERAND{
            node = Operand($OPERAND.getText())
};
