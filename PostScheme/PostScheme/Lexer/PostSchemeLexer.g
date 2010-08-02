lexer grammar PostSchemeLexer;


options {
    language=CSharp2;    
}

@namespace { PostScheme }

OPEN_PAREN:   '(';
CLOSE_PAREN:   ')';
DOT: '\.';
COMMA: ',';
NEWLINE:'\r'? '\n';
WS  :   (' '|'\t')+ { Skip(); } ;
IDENTIFIER: ~(OPEN_PAREN | CLOSE_PAREN | DOT | COMMA)+;


