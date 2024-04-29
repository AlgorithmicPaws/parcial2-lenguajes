grammar FourierTransform; // rename to distinguish from Expr.g4

prog:   stat+ ;

stat:   func NEWLINE                # printExpr
    |   NEWLINE                     # blank
    ;

func:   '{' dec '|' dec # funcion
    |   trigFunc # trigonometricas
    |   'dirac(''t'')' # delta
    |   'SUM(''dirac(''t''-' 'k' '*' pul ')' #sumatoria
    ;

dec:    res ',' cond # declaracion
   ;
   
res:    '1 -''(''|t|''/'pul')' # triangular
   |    INT   # int
   ;
   
cond:   ('t'|'|t|') op=('<'|'>'|'<='|'>=') pul # condicion
    ;
    
trigFunc : 'cos(' frec 't'')'               # CosFunc
         | 'sin(' frec 't'')'                # SinFunc
         ;    
    
pul: INT # ints
   | PULS # longP
   ;

frec: INT # integer
    | FRE # frecuency
    ;

MN  :   '<' ; // assigns token name to '*' used above in grammar
MNI :   '<=' ;
MY  :   '>' ;
MYI :   '>=' ;
FRE :   'w';  
INT :   [0-9]+ 
    |   '-'[0-9]+;         // match integers
PULS:   'T/2'
    |   'T'
    ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
