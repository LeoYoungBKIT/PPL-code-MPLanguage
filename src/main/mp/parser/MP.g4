//MSSV:1612541
//Ho va ten: Tran Truong Tuan Phat
//Lop: MT16TN

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declaration+ EOF;
declaration: varDecl | funcDecl | proDecl;
varDecl: VAR listDecls+;
listDecls: IDENTIFIER (COMMA IDENTIFIER)* COLON types SEMI;
funcDecl: FUNCTION IDENTIFIER LB listParams? RB COLON types SEMI varDecl? compoundstmt;
listParams: params (SEMI params)*;
params: IDENTIFIER (COMMA IDENTIFIER)* COLON types;
proDecl: PROCEDURE IDENTIFIER LB listParams? RB SEMI varDecl? compoundstmt;

fragment A: ('a' | 'A');
fragment B: ('b' | 'B');
fragment C: ('c' | 'C');
fragment D: ('d' | 'D');
fragment E: ('e' | 'E');
fragment F: ('f' | 'F');
fragment G: ('g' | 'G');
fragment H: ('h' | 'H');
fragment I: ('i' | 'I');
fragment J: ('j' | 'J');
fragment K: ('k' | 'K');
fragment L: ('l' | 'L');
fragment M: ('m' | 'M');
fragment N: ('n' | 'N');
fragment O: ('o' | 'O');
fragment P: ('p' | 'P');
fragment Q: ('q' | 'Q');
fragment R: ('r' | 'R');
fragment S: ('s' | 'S');
fragment T: ('t' | 'T');
fragment U: ('u' | 'U');
fragment V: ('v' | 'V');
fragment W: ('w' | 'W');
fragment X: ('x' | 'X');
fragment Y: ('y' | 'Y');
fragment Z: ('z' | 'Z');


LCMT: '//'~[\n]* -> skip;
BCMT1: '{' .*? '}' -> skip;
BCMT2: '(*' .*? '*)' -> skip;


BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
WHILE: W H I L E;
TO: T O;
DOWNTO: D O W N T O;
WITH: W I T H;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
VAR: V A R;
OF: O F;
BEGIN: B E G I N;
END: E N D;
RETURN: R E T U R N;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
ARRAY: A R R A Y;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;
ADD: '+';
SUB: '-';
MUL: '*';
DIV_F: '/';
EQUAL: '=';
NOTEQUAL: '<>';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';
ASSIGN: ':=';
LSB: '[';
RSB: ']';
COLON: ':';
LB: '(';
RB: ')';
SEMI: ';';
DDOT: '..';
COMMA: ',';


literal: INTLIT | REALIT | BOOLIT | STRLIT;
fragment DIGIT: [0-9];
INTLIT: DIGIT+;
fragment EXPONENT:[eE] '-'? DIGIT+;
REALIT: DIGIT+ ('.' DIGIT*)? EXPONENT? | '.' DIGIT+ EXPONENT?;
BOOLIT: TRUE | FALSE;
TRUE: T R U E;
FALSE: F A L S E;

fragment BSP: '\\b';
fragment FF: '\\f';
fragment CR: '\\r';
fragment NEWLINE: '\\n';
fragment TAB: '\\t';
fragment SQUOTE: '\\\'';
fragment DQUOTE: '\\"';
fragment BSL:'\\''\\';

fragment LEGAL_ESCAPE: BSP | FF | CR | NEWLINE | TAB | SQUOTE | DQUOTE | BSL;

UNCLOSE_STRING: '"' (~[\n\r\\'"] | LEGAL_ESCAPE)*{ raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: UNCLOSE_STRING ('\\' ~[nrbft'"] | '\''){ raise IllegalEscape(self.text[1:])};

STRLIT: UNCLOSE_STRING '"'{ self.text = self.text[1:-1]};


types: primtype | compoundtype;
primtype: BOOLEAN | INTEGER | REAL | STRING;
compoundtype: arrtype;
arrtype: ARRAY LSB lower DDOT upper RSB OF primtype;
lower: SUB? INTLIT;
upper: SUB? INTLIT;

operand: literal | IDENTIFIER | funcall;
exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1 | operand;
exp1: exp2 EQUAL exp2 | exp2 NOTEQUAL exp2 | exp2 LESSTHAN exp2 | exp2 GREATERTHAN exp2 | exp2 LESSEQUAL exp2 | exp2 GREATEREQUAL exp2 | exp2;
exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;
exp3: exp3 DIV_F exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;
exp4: SUB exp4 | NOT exp4 | exp5;
exp5: exp5 LSB exp RSB | exp6;
exp6: LB exp RB | operand;
arrelement: exp5 LSB exp RSB;
funcall: IDENTIFIER LB (exp (COMMA exp)*)? RB;


stmt: assignstmt | ifstmt | whilestmt | forstmt | breakstmt | continuestmt | returnstmt | compoundstmt | withstmt | callstmt;
assignstmt: lhs (ASSIGN lhs)* ASSIGN exp SEMI;
lhs: (IDENTIFIER | arrelement);
ifstmt: IF exp THEN stmt (ELSE stmt)?;
whilestmt: WHILE exp DO stmt;
forstmt: FOR IDENTIFIER ASSIGN exp (TO | DOWNTO) exp DO stmt;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN exp? SEMI;
compoundstmt: BEGIN stmt* END;
withstmt: WITH listDecls+ DO stmt;
callstmt: IDENTIFIER LB (exp (COMMA exp)*)? RB SEMI;


IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: .{ raise ErrorToken(self.text)};
