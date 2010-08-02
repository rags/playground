parser grammar PostSchemeParser;
options {
    language=CSharp2;    
    tokenVocab = PostSchemeLexer;
}

@namespace { PostScheme }

statement: OPEN_PAREN IDENTIFIER CLOSE_PAREN;
