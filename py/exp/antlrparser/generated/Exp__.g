lexer grammar Exp;
options {
  language=Python;

}

// $ANTLR src "Exp.g" 9
OPERAND: '0'..'9'+;

// $ANTLR src "Exp.g" 11
LEFT_PAREN: '(';
// $ANTLR src "Exp.g" 12
RIGHT_PAREN: ')';
// $ANTLR src "Exp.g" 13
OP_PLUS: '+';
// $ANTLR src "Exp.g" 14
OP_MINUS: '-';
// $ANTLR src "Exp.g" 15
OP_MULT: '*';
// $ANTLR src "Exp.g" 16
OP_DIV: '/';

// $ANTLR src "Exp.g" 18
WS	:	(' '|'\t'|'\n'|'\r')+ {self.skip()} ;

