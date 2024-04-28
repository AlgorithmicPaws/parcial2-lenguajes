grammar PythonFunction;

prog:   stat+ ;

stat: iterable_declaration NEWLINE  # print_stat
    | ID '=' expr NEWLINE         # assign
    ;
filter: 'filter' '(' condition ',' IDENTIFIER ')';

condition: expr op=('=='|'>'|'<'|'!='|'>='|'<=') expr;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   trigFunc                    # TrigFunction
    |   '|' expr '|'		    # Abs
    |   INT                         # int
    |   ID                          # id
    |   HEX			    # hex
    |   '(' expr ')'                # parens
    ;

trigFunc : 'cos' expr               # CosFunc
         | 'sen' expr               # SenFunc
         | 'tan' expr		    # TanFunc
         ;

iterable_declaration : IDENTIFIER '=' iterable_expression  # creacion_iterable
                    ;           


iterable_expression : list_expression  # list
                    | tuple_expression # tuple
                    | string_expression # string
                    | set_expression # set
                    ;

list_expression : '[' LITERAL (',' LITERAL)* ']' # accion_list
                | '[]'                           # empty_list
                ;  

tuple_expression : '(' LITERAL (',' LITERAL)* ')' # accion_tuple
                |'()'                             # empty_tuple
                ;

string_expression : STRING_LITERAL               # accion_string
                ;

set_expression : '{' LITERAL (',' LITERAL)* '}'  # accion_set
                |'{}'                            # empty_set
                ;




IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING_LITERAL : ('"' ~["]* '"' | '\'' ~[']* '\'');
LITERAL : [0-9]+ ;
NEWLINE : '\r'? '\n';
MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
TAN :   'tan' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
HEX :   '0x' [a-fA-F0-9]+ ; //lo devuelve como num decimal
WS  :   [ \t]+ -> skip ; // toss out whitespace
INDENT : '    ';