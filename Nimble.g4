/**
 A grammar for the Nimble language

 Author: Greg Phillips

 version: 2022-02-04
*/
 
grammar Nimble ;

script : funcDef* main EOF;

funcDef: 'func' ID '('
             (parameterDef (',' parameterDef)*)?
         ')' ('->' TYPE)? '{' body '}';

parameterDef: ID ':' TYPE;

main: body;

body : varBlock block;

varBlock: varDec* ;

block : statement* ;

varDec: 'var' ID ':' TYPE ('=' expr)? ;

statement :
      ID '=' expr                       # assignment
    | 'while' expr '{' block '}'        # while
    | 'if' expr '{' block '}'
      ('else' '{' block '}')?           # if
    | 'print' expr                      # print
    | 'return' expr?                    # return
    | funcCall                          # funcCallStmt
    ;

expr:
     '(' expr ')'                       # parens
    | op=('!'|'-') expr                 # neg
    | expr op=('*'|'/') expr            # mulDiv
    | expr op=('+'|'-') expr            # addSub
    | expr op=('<' | '<=' | '==') expr  # compare
    | funcCall                          # funcCallExpr
    | ID                                # variable
    | STRING                            # stringLiteral
    | INT                               # intLiteral
    | BOOL                              # boolLiteral
    ;

funcCall: ID '('(expr (',' expr)* )?')';

STRING : '"' ( SINGLE_CHAR | ESCAPED_CHAR )*? '"' ;
fragment SINGLE_CHAR : ( ' ' .. '[' | ']' .. '~');
fragment ESCAPED_CHAR : '\\' [abfnrtv'"\\?] ;

INT : [0-9]+ ;

TYPE:    'Int' | 'Bool' | 'String';
BOOL:    'true' | 'false';

ID : [_a-zA-Z][_a-zA-Z0-9]* ; 

WS : [ \t\r\n]+ -> skip ;

COMMENT : '//' ~[\r\n]* -> skip ;
