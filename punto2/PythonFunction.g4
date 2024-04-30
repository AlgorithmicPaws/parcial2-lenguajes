grammar PythonFunction;

prog:   stat+ ;

stat: function_declaration_filter NEWLINE # creacion_function_fillter
    |function_declaration_map NEWLINE # creacion_function_fillter
    | iterable_declaration NEWLINE  # print_stat
    | ID '=' expr NEWLINE         # assign
    | IDENTIFIER '=' filter NEWLINE    #assign_filter 
    | IDENTIFIER '=' map NEWLINE    #assign_map            
    ;
function_declaration_map: 'def' IDENTIFIER '('IDENTIFIER'):' NEWLINE INDENT 'return' operation # def_map
;

function_declaration_filter: 'def' IDENTIFIER '('IDENTIFIER'):' NEWLINE INDENT 'return' condition # def
;

filter: 'filter' '(' IDENTIFIER ',' IDENTIFIER ')'     # execute_filter
        ;

map: 'map' '(' IDENTIFIER ',' IDENTIFIER ')'     # execute_map
        ;

operation:IDENTIFIER op=('*'|'/'|'+'|'-') expr                                    # left_operation
        |expr op=('*'|'/'|'+'|'-') IDENTIFIER                                    # right_operation
        ;

condition: expr op=('=='|'>'|'<'|'!='|'>='|'<=') expr       # always_condition
        |IDENTIFIER op=('=='|'>'|'<'|'!='|'>='|'<=') expr   # parameter_condition
        |expr op=('=='|'>'|'<'|'!='|'>='|'<=') IDENTIFIER   # condition_parameter
        ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   trigFunc                    # TrigFunction
    |   '|' expr '|'		        # Abs
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
                    | set_expression # set
                    ;

list_expression : '[' INT (',' INT)* ']' # accion_list
                | '[]'                           # empty_list
                ;  

tuple_expression : '(' INT (',' INT)* ')' # accion_tuple
                |'()'                             # empty_tuple
                ;

set_expression : '{' INT (',' INT)* '}'  # accion_set
                |'{}'                            # empty_set
                ;



INDENT : '    ';
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE : '\r'? '\n';
MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
IGUAL :   '==' ;
NOIGUAL :   '!=' ;
MAYOR :   '>' ;
MENOR :   '<' ;
MAYORIGUAL :   '>=' ;
MENORIGUAL :   '<=' ;
TAN :   'tan' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
HEX :   '0x' [a-fA-F0-9]+ ; //lo devuelve como num decimal
WS  :   [ \t]+ -> skip ; // toss out whitespace
