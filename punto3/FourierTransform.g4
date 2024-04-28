grammar FourierTransform; // rename to distinguish from Expr.g4

prog:   stat+ ;

stat:   func NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

func:   '{' dec '|' dec # funcion
    |   trigFunc # trigonometricas
    |   'dirac(''t'')' # delta
    |   'SUM(''dirac(''t''-' 'k' '*' (INT|PULS) ')' #sumatoria
    ;

dec:    res ',' cond # declaracion
   ;
   
res:    '1 -''(''|t|''/'(INT|PULS) # triangular
   |    INT   # int
   |    '-1'  # blanked 
   ;
   
cond:   ('t'|'|t|') op=('<'|'>'|'<='|'>=') (INT|PULS) # condicion
    ;

trigFunc : 'cos(' INT 't'')'               # CosFunc
         | 'sin(' INT 't'')'                # SinFunc
         ;

MN  :   '<' ; // assigns token name to '*' used above in grammar
MNI :   '<=' ;
MY  :   '>' ;
MYI :   '>=' ;
INT :   [0-9]+ ;         // match integers
PULS:   'T'
    |   'T/2'
    ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
