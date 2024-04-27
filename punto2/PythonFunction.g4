grammar PythonFunction;

prog:   stat+ ;

stat:  function_declaration NEWLINE (iterable_declaration)* 'map' '('  function_name (',' iterable_name)* ')'
    ;

function_declaration : 'def' function_name '(' parameter_list ')' ':' NEWLINE function_body;

function_name : IDENTIFIER;

parameter_list : parameter (',' parameter)*;

parameter : IDENTIFIER;

function_body : statement_block;

statement_block : INDENT statements;

statements : statement (NEWLINE statement)*;

statement : expression_statement ;

expression_statement : expression;


expression :  LITERAL 
        | expression '+' expression 
        | expression '-' expression
        | expression '*' expression 
        | expression '/' expression;

iterable_declaration : iterable_name '=' iterable_expression;


iterable_name : IDENTIFIER;

iterable_expression : list_expression 
                    | tuple_expression 
                    | string_expression 
                    | set_expression;

list_expression : '[' expression_list? ']';

tuple_expression : '(' expression_list? ')';

string_expression : STRING_LITERAL;

set_expression : '{' expression_list? '}';

expression_list : LITERAL (',' LITERAL)*;


IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING_LITERAL : '"' ~["]* '"';
LITERAL : [0-9]+ ;
NEWLINE : '\r'? '\n';
INDENT : '    ';