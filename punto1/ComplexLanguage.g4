grammar ComplexLanguage;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # int
    |   complex                     # comp
    |   '(' expr ')'                # parens
    ;

complex: INT op=('+'|'-') IMG        # complejo
       | IMG op=('+'|'-') IMG       # sumaCom
       | IMG                        # img
       ;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
INT :   [0-9]+          // match integers
    |   [0-9]+'.'[0-9]+
    |   '-'[0-9]+
    |   '-'[0-9]+'.'[0-9]+; 
IMG: [0-9]+'i' 
   | '-'[0-9]+'i'
   | [0-9]+'.'[0-9]+'i'
   | '-'[0-9]+'.'[0-9]+'i';
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
