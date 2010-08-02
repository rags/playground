grammar Exp;

options {
    language=Python;
    output=AST;
	ASTLabelType=CommonTree;
}

OPERAND: '0'..'9'+;

LEFT_PAREN: '(';
RIGHT_PAREN: ')';
OP_PLUS: '+';
OP_MINUS: '-';
OP_MULT: '*';
OP_DIV: '/';

WS	:	(' '|'\t'|'\n'|'\r')+ {self.skip()} ;

low_prededence_op: OP_PLUS | OP_MINUS;
high_prededence_op: OP_MULT | OP_DIV;

low_precedence_exp: high_precedence_exp (low_prededence_op^ high_precedence_exp)*;
high_precedence_exp: atom (high_prededence_op^ atom)*;
atom: OPERAND| LEFT_PAREN! low_precedence_exp RIGHT_PAREN!;
