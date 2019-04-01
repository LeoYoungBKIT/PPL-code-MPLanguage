import unittest
from TestUtils import TestAST
from AST import *

#simple_program: 10 tests: 301 -> 310 (tests about variable_declaration, procedure_declaration, function_declaration and some keywords)
#_statement: 30 tests
########## assignment_statement: 311-> 315 (5 tests)
########## if_statement: 316 -> 320 (5 tests)
########## while_statement: 321 -> 323 (3 tests)
########## for_statement: 324 -> 327 (4 tests)
########## with_statement: 328 -> 332 (5 tests)
########## compound_statement: 333 -> 334 (2 tests)
########## call_statement: 335 -> 338 (4 tests)
########## other_statement: 339 -> 340 (2 tests)
#_expression: 20
########## andthen_orelse_expression: 341 -> 343 (3 tests)
########## relational_expression: 344 ->347 (4 tests)
########## associative_expression: 348 -> 360 (13 tests)
#_multideclaration: 361 -> 365 (5 tests)
#comment: 366 -> 370 (5 tests)
#notice_scenario: 371 -> 380 (10 tests)
#random_program: 381 -> 400 (20 tests)

class ASTGenSuite(unittest.TestCase):
    def test_simpleprogram_301(self):
        input = """
            procedure main(a:integer; b,c: real;d:string;e:boolean);
            var x:integer;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'e'),BoolType())],[VarDecl(Id(r'x'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))


    def test_simpleprogram_302(self):
        input = """
            function main(a:integer; b,c: real;d:string;e:boolean): integer;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'e'),BoolType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))


    def test_simpleprogram_303(self):
        input = """
            procedure main(a:integer; b: array[1 .. 3] of integer);
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,IntType()))],[],[],VoidType())]))

        self.assertTrue(TestAST.test(input,expect,303))


    def test_simpleprogram_304(self):
        input = """
            function main(a:integer; b: array[1 .. 3] of integer): integer;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),ArrayType(1,3,IntType()))],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))


    def test_simpleprogram_305(self):
        input = """
            procedure main(a:integer; b,c: real;d:string;e:boolean;f:array[1 .. 3] of integer);
            var x,y,z: integer;
                    t: real;
                  m,n: string;
                    p: array[1 .. 4] of real;
            begin

            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),ArrayType(1,3,IntType()))],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'm'),StringType()),VarDecl(Id(r'n'),StringType()),VarDecl(Id(r'p'),ArrayType(1,4,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))


    def test_simpleprogram_306(self):
        input = """
            pRoCeDUre main(a:inTegEr; b:StriNG);
            vAr x: array[1 .. 7] of BoOLean;
                y: array[-1 .. 7] of real;
                z: array[1 .. -7] of string;
                p: array[-1 .. -7] of Real;
            beGiN

            enD
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType())],[VarDecl(Id(r'x'),ArrayType(1,7,BoolType())),VarDecl(Id(r'y'),ArrayType(-1,7,FloatType())),VarDecl(Id(r'z'),ArrayType(1,-7,StringType())),VarDecl(Id(r'p'),ArrayType(-1,-7,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))


    def test_simpleprogram_307(self):
        input = """
            FunCtIon a(a:inTegEr; b:StriNG; c:Array[1 .. 3] of real): array[1 .. -2] of real;
            begin

            end
            """
        expect = str(Program([FuncDecl(Id(r'a'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),ArrayType(1,3,FloatType()))],[],[],ArrayType(1,-2,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,307))


    def test_simpleprogram_308(self):
        input = """
            FunCtIon a(a:inTegEr; b:StriNG; c:Array[1 .. 3] of real): array[1 .. -2] of real;
            var x,y,z: integer;
                    t: real;
                  m,n: string;
                    p: array[1 .. 4] of real;
            begin

            end
            """
        expect = str(Program([FuncDecl(Id(r'a'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),StringType()),VarDecl(Id(r'c'),ArrayType(1,3,FloatType()))],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'm'),StringType()),VarDecl(Id(r'n'),StringType()),VarDecl(Id(r'p'),ArrayType(1,4,FloatType()))],[],ArrayType(1,-2,FloatType()))]))

        self.assertTrue(TestAST.test(input,expect,308))


    def test_simpleprogram_309(self):
        input = """
            procedure main();
            begin
            end
            function add(x,y:integer): integer;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[],VoidType()),FuncDecl(Id(r'add'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))


    def test_simpleprogram_310(self):
        input = """
            var x,y,z: integer;
                    t: real;
                  m,n: string;
                    p: array[1 .. 4] of boolean;
            procedure main();
            begin
            end
            function add(x,y:integer): integer;
            begin
            end
            """
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'm'),StringType()),VarDecl(Id(r'n'),StringType()),VarDecl(Id(r'p'),ArrayType(1,4,BoolType())),FuncDecl(Id(r'main'),[],[],[],VoidType()),FuncDecl(Id(r'add'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))


    def test_assignment_statement_311(self):
        '''Simple assigment statement test'''
        input = """
            procedure main();
            begin
                a:=1+3*2;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',IntLiteral(1),BinaryOp(r'*',IntLiteral(3),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,311))


    def test_assignment_statement_312(self):
        '''assigment statement with stranger expression test '''
        input = """
            procedure main();
            begin
                a:=1<3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),BinaryOp(r'<',IntLiteral(1),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,312))


    def test_assignment_statement_313(self):
        '''Multi assign in assignment statement test'''
        input = """
            procedure main();
            begin
                a:=b:=c:=d+e;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'c'),BinaryOp(r'+',Id(r'd'),Id(r'e'))),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))


    def test_assignment_statement_314(self):
        '''Multi assign and complex expression in assignment statement test'''
        input = """
            procedure main();
            begin
                a:=b:=c[4]*3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'b'),BinaryOp(r'*',ArrayCell(Id(r'c'),IntLiteral(4)),IntLiteral(3))),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))


    def test_assignment_statement_315(self):
        '''Multi assign and function call in assignment statement test'''
        input = """
            procedure main();
            begin
                a:=b:=foo(1,2,3);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'b'),CallExpr(Id(r'foo'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(Id(r'a'),Id(r'b'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))


    def test_if_statement_316(self):
        input = """
            procedure main();
            begin
                if foo(1,2,3)>b[3] then write("I have done assignment 2 PPL"); else write("I have to try more") ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',CallExpr(Id(r'foo'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayCell(Id(r'b'),IntLiteral(3))),[CallStmt(Id(r'write'),[StringLiteral(r'I have done assignment 2 PPL')])],[CallStmt(Id(r'write'),[StringLiteral(r'I have to try more')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))


    def test_if_statement_317(self):
        input = """
            procedure main();
            begin
                if (a = TRUE and then not 5) then begin end else begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'andthen',BinaryOp(r'=',Id(r'a'),BooleanLiteral(True)),UnaryOp(r'not',IntLiteral(5))),[],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))


    def test_if_statement_318(self):
        input = """
            procedure main();
            begin
                if (a = false or else foo(3)) then a:=true ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'orelse',BinaryOp(r'=',Id(r'a'),BooleanLiteral(False)),CallExpr(Id(r'foo'),[IntLiteral(3)])),[Assign(Id(r'a'),BooleanLiteral(True))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))


    def test_if_statement_319(self):
        input = """
            procedure main();
            begin
                if (a = false or else foo(3)) then if a>b then f:=3; else f:=2; else f:="error" ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'orelse',BinaryOp(r'=',Id(r'a'),BooleanLiteral(False)),CallExpr(Id(r'foo'),[IntLiteral(3)])),[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'f'),IntLiteral(3))],[Assign(Id(r'f'),IntLiteral(2))])],[Assign(Id(r'f'),StringLiteral(r'error'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))


    def test_if_statement_320(self):
        input = """
            procedure main();
            begin
                if a>1 then return 0;
                else
                    if a<1 then break;
                    else continue;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Return(IntLiteral(0))],[If(BinaryOp(r'<',Id(r'a'),IntLiteral(1)),[Break()],[Continue()])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))


    def test_while_statement_321(self):
        '''Simple while statement test'''
        input = """
            procedure main();
            var i,a,b: integer;
            begin
                i:=a:=0;
                while i<100 do
                    write("I have done Assignment 2 PPL");
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(0)),Assign(Id(r'i'),Id(r'a')),While(BinaryOp(r'<',Id(r'i'),IntLiteral(100)),[CallStmt(Id(r'write'),[StringLiteral(r'I have done Assignment 2 PPL')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))


    def test_while_statement_322(self):
        '''while nest in while test'''
        input = """
            procedure main();
            var i,a,b: integer;
            begin
                i:=a:=0;
                while i<100 do while j<10 do a:=i+j;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(0)),Assign(Id(r'i'),Id(r'a')),While(BinaryOp(r'<',Id(r'i'),IntLiteral(100)),[While(BinaryOp(r'<',Id(r'j'),IntLiteral(10)),[Assign(Id(r'a'),BinaryOp(r'+',Id(r'i'),Id(r'j')))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))


    def test_while_statement_323(self):
        '''compound statement in while statement '''
        input = """
            procedure main();
            var i,a,b: integer;
            begin
                i:=a:=0;
                while i<100 do
                    begin
                        i:=i+1;
                        b:=i*i;
                        a:=a+b;
                    end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(0)),Assign(Id(r'i'),Id(r'a')),While(BinaryOp(r'<',Id(r'i'),IntLiteral(100)),[Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),IntLiteral(1))),Assign(Id(r'b'),BinaryOp(r'*',Id(r'i'),Id(r'i'))),Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),Id(r'b')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))


    def test_for_statement_324(self):
        '''Simple for statement test'''
        input = """
            procedure main();
            begin
                for a:=1 to 10 do write("My name is Tuan Phat and you can call me Leo Young, my English name");
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'write'),[StringLiteral(r'My name is Tuan Phat and you can call me Leo Young, my English name')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))


    def test_for_statement_325(self):
        '''downto in for statement '''
        input = """
            procedure main();
            begin
                for a:=10 downto 1 do begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),IntLiteral(10),IntLiteral(1),False,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))


    def test_for_statement_326(self):
        '''expression in for statement test'''
        input = """
            procedure main();
            begin
                for a:=foo(2,3,4) TO -10 do begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'a'),CallExpr(Id(r'foo'),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]),UnaryOp(r'-',IntLiteral(10)),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))


    def test_for_statement_327(self):
        '''for nest in for statement test'''
        input = """
            procedure main();
            begin
                fOr i:=5*4 div 2 mod 2 dOWnTo 1 div 1 div 1 do for j:=0 to 9 do swap(a[i],a[j]);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'i'),BinaryOp(r'mod',BinaryOp(r'div',BinaryOp(r'*',IntLiteral(5),IntLiteral(4)),IntLiteral(2)),IntLiteral(2)),BinaryOp(r'div',BinaryOp(r'div',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),False,[For(Id(r'j'),IntLiteral(0),IntLiteral(9),True,[CallStmt(Id(r'swap'),[ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))


    def test_with_statement_328(self):
        '''Simple with statement test'''
        input = """
            procedure main();
            begin
                with a,b:integer; do print("a plus b equal: ",a+b);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'print'),[StringLiteral(r'a plus b equal: '),BinaryOp(r'+',Id(r'a'),Id(r'b'))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))


    def test_with_statement_329(self):
        '''List declaration in with statement test'''
        input = """
            procedure main();
            begin
                with a,b:integer; c: string; d,e:boolean; f:real; do begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'd'),BoolType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),FloatType())],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))


    def test_with_statement_330(self):
        '''More Complex list declaration in with statement test'''
        input = """
            procedure main();
            begin
                witH a,b:integer; c,d: array[-1 .. -3] of real; do begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(-1,-3,FloatType())),VarDecl(Id(r'd'),ArrayType(-1,-3,FloatType()))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))


    def test_with_statement_331(self):
        '''compound statement in with statement test'''
        input = """
            procedure main();
            begin
                wiTh a,b,c:integer; do
                    begin
                        a:=b;
                        b:=c;
                        c:=a;
                    end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),Id(r'b')),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'c'),Id(r'a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))


    def test_with_statement_332(self):
        '''With nest in with statement test'''
        input = """
            procedure main();
            begin
                With a,b,c:integer; Do
                    with d,e: string; do
                        with f: real; do
                            begin end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[With([VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'e'),StringType())],[With([VarDecl(Id(r'f'),FloatType())],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))


    def test_compound_statement_333(self):
        '''Compound in compound statement test'''
        input = """
            procedure main(a:integer; b,c: real;d:string;e:boolean;f:array[1 .. 3] of integer);
            var x,y,z: integer;
                    t: real;
                  m,n: string;
                    p: array[1 .. 4] of real;
            begin
                begin
                    beGiN
                    End
                end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),StringType()),VarDecl(Id(r'e'),BoolType()),VarDecl(Id(r'f'),ArrayType(1,3,IntType()))],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType()),VarDecl(Id(r't'),FloatType()),VarDecl(Id(r'm'),StringType()),VarDecl(Id(r'n'),StringType()),VarDecl(Id(r'p'),ArrayType(1,4,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))


    def test_compound_statement_334(self):
        '''Complex statement nest in compound statement test '''
        input = """
            function main(x,y:integer):integer;
            var a,b:string;
            begin
                begin
                    if m=n then read(files); else close(files);
                    for i:=1 to 10 do begin end
                    begin
                    end
                    begin end
                end
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[If(BinaryOp(r'=',Id(r'm'),Id(r'n')),[CallStmt(Id(r'read'),[Id(r'files')])],[CallStmt(Id(r'close'),[Id(r'files')])]),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,334))


    def test_call_statement_335(self):
        '''Genaral call statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:string;
            begin
                open(files,"r");
                write();
                check("successful",1,2,foo(3,a[4]),a[2]);
                close(open());
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[CallStmt(Id(r'open'),[Id(r'files'),StringLiteral(r'r')]),CallStmt(Id(r'write'),[]),CallStmt(Id(r'check'),[StringLiteral(r'successful'),IntLiteral(1),IntLiteral(2),CallExpr(Id(r'foo'),[IntLiteral(3),ArrayCell(Id(r'a'),IntLiteral(4))]),ArrayCell(Id(r'a'),IntLiteral(2))]),CallStmt(Id(r'close'),[CallExpr(Id(r'open'),[])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,335))


    def test_call_statement_336(self):
        '''Complex(expression + compound_type) call statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:string;
            begin
                call(foo(),x+y,a[a[a[a()]]]);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[CallStmt(Id(r'call'),[CallExpr(Id(r'foo'),[]),BinaryOp(r'+',Id(r'x'),Id(r'y')),ArrayCell(Id(r'a'),ArrayCell(Id(r'a'),ArrayCell(Id(r'a'),CallExpr(Id(r'a'),[]))))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,336))


    def test_call_statement_337(self):
        '''More complex call statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:integer;
            begin
                call(this,(1+a)[2][3]);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'call'),[Id(r'this'),ArrayCell(ArrayCell(BinaryOp(r'+',IntLiteral(1),Id(r'a')),IntLiteral(2)),IntLiteral(3))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,337))


    def test_call_statement_338(self):
        '''Call in call statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:string;
            begin
                call(call(call()));
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[CallStmt(Id(r'call'),[CallExpr(Id(r'call'),[CallExpr(Id(r'call'),[])])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,338))


    def test_other_statement_339(self):
        '''Genaral other statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:string;
            begin
                coNtinue;
                breaK;
                return;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[Continue(),Break(),Return(None)],IntType())]))
        self.assertTrue(TestAST.test(input,expect,339))


    def test_other_statement_340(self):
        '''Return statement test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:integer;
            begin
                return;
                return 1 div 1 div 1 mod 1 + 1;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Return(None),Return(BinaryOp(r'+',BinaryOp(r'mod',BinaryOp(r'div',BinaryOp(r'div',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),IntLiteral(1)),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,340))


    def test_andthen_orelse_expression_341(self):
        '''andthen not test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:integer;
            begin
                a:= f(0,1,2) and then not 5;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),BinaryOp(r'andthen',CallExpr(Id(r'f'),[IntLiteral(0),IntLiteral(1),IntLiteral(2)]),UnaryOp(r'not',IntLiteral(5))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,341))


    def test_andthen_orelse_expression_342(self):
        '''orelse not test'''
        input = """
            function main(x,y:integer):integer;
            var a,b:integer;
            begin
                b:=a[3] or else not 6;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[Assign(Id(r'b'),BinaryOp(r'orelse',ArrayCell(Id(r'a'),IntLiteral(3)),UnaryOp(r'not',IntLiteral(6))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,342))


    def test_andthen_orelse_expression_343(self):
        '''andthen orelse nested'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=b:=c[3] or else not 1 and then 3 or else 2;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'b'),BinaryOp(r'orelse',BinaryOp(r'andthen',BinaryOp(r'orelse',ArrayCell(Id(r'c'),IntLiteral(3)),UnaryOp(r'not',IntLiteral(1))),IntLiteral(3)),IntLiteral(2))),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,343))


    def test_relational_expression_344(self):
        '''Relational operator and associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=b:=c=2;
                a:=b<1;
                b:=c>5;
                a:=b:=c<>0;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'b'),BinaryOp(r'=',Id(r'c'),IntLiteral(2))),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'a'),BinaryOp(r'<',Id(r'b'),IntLiteral(1))),Assign(Id(r'b'),BinaryOp(r'>',Id(r'c'),IntLiteral(5))),Assign(Id(r'b'),BinaryOp(r'<>',Id(r'c'),IntLiteral(0))),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))


    def test_relational_expression_345(self):
        '''More Complex relational operator and associavity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=b:=c<=1;
                a:=b>=-1;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'b'),BinaryOp(r'<=',Id(r'c'),IntLiteral(1))),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'a'),BinaryOp(r'>=',Id(r'b'),UnaryOp(r'-',IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))


    def test_relational_expression_346(self):
        '''All relational operator and associavity test '''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=c[1]=2;
                a:=f()<1;
                b:=foo(a,b,c)>5;
                a:=b:=f(f(f()))<>0;
                c:=b[b[b[2]]]<=1;
                a:=f(a[1],h)>=-1;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'=',ArrayCell(Id(r'c'),IntLiteral(1)),IntLiteral(2))),Assign(Id(r'a'),BinaryOp(r'<',CallExpr(Id(r'f'),[]),IntLiteral(1))),Assign(Id(r'b'),BinaryOp(r'>',CallExpr(Id(r'foo'),[Id(r'a'),Id(r'b'),Id(r'c')]),IntLiteral(5))),Assign(Id(r'b'),BinaryOp(r'<>',CallExpr(Id(r'f'),[CallExpr(Id(r'f'),[CallExpr(Id(r'f'),[])])]),IntLiteral(0))),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'c'),BinaryOp(r'<=',ArrayCell(Id(r'b'),ArrayCell(Id(r'b'),ArrayCell(Id(r'b'),IntLiteral(2)))),IntLiteral(1))),Assign(Id(r'a'),BinaryOp(r'>=',CallExpr(Id(r'f'),[ArrayCell(Id(r'a'),IntLiteral(1)),Id(r'h')]),UnaryOp(r'-',IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,346))


    def test_relational_expression_347(self):
        ''''No relational operator and associavity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=b:=c;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,347))


    def test_associative_expression_348(self):
        '''Some basic operators test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=1+2-3*c mod 2 div 3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(1),IntLiteral(2)),BinaryOp(r'div',BinaryOp(r'mod',BinaryOp(r'*',IntLiteral(3),Id(r'c')),IntLiteral(2)),IntLiteral(3))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))


    def test_associative_expression_349(self):
        '''More operators test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=1*3+2 div 3 - 3 mod 5 or c and b;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'or',BinaryOp(r'-',BinaryOp(r'+',BinaryOp(r'*',IntLiteral(1),IntLiteral(3)),BinaryOp(r'div',IntLiteral(2),IntLiteral(3))),BinaryOp(r'mod',IntLiteral(3),IntLiteral(5))),BinaryOp(r'and',Id(r'c'),Id(r'b'))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,349))


    def test_associative_expression_350(self):
        '''Operators and parenthesis test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=1*(3+2 div 3) - 3 ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'*',IntLiteral(1),BinaryOp(r'+',IntLiteral(3),BinaryOp(r'div',IntLiteral(2),IntLiteral(3)))),IntLiteral(3)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,350))


    def test_associative_expression_351(self):
        '''mul-add-unary-indexparenthesis associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=1*2-a[b+c mod 2];
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'*',IntLiteral(1),IntLiteral(2)),ArrayCell(Id(r'a'),BinaryOp(r'+',Id(r'b'),BinaryOp(r'mod',Id(r'c'),IntLiteral(2))))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,351))


    def test_associative_expression_352(self):
        '''mul-add-unary-parenthesis-indexparenthesis associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=1*2-(a+b+c)[b+c mod 2];
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'*',IntLiteral(1),IntLiteral(2)),ArrayCell(BinaryOp(r'+',BinaryOp(r'+',Id(r'a'),Id(r'b')),Id(r'c')),BinaryOp(r'+',Id(r'b'),BinaryOp(r'mod',Id(r'c'),IntLiteral(2))))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,352))


    def test_associative_expression_353(self):
        '''mul-add-unary associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=x*y + -3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'*',Id(r'x'),Id(r'y')),UnaryOp(r'-',IntLiteral(3))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,353))


    def test_associative_expression_354(self):
        '''mul-add-unary-parenthesis associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:=x*(y + -3);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'*',Id(r'x'),BinaryOp(r'+',Id(r'y'),UnaryOp(r'-',IntLiteral(3)))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))


    def test_associative_expression_355(self):
        '''logic operator and associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= not c or a and b;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'or',UnaryOp(r'not',Id(r'c')),BinaryOp(r'and',Id(r'a'),Id(r'b'))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,355))


    def test_associative_expression_356(self):
        '''logic operator and parenthesis associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= not c or (a and b);
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'or',UnaryOp(r'not',Id(r'c')),BinaryOp(r'and',Id(r'a'),Id(r'b'))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,356))


    def test_associative_expression_357(self):
        '''logic operator and other parenthesis associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= not (c or a) and b;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'and',UnaryOp(r'not',BinaryOp(r'or',Id(r'c'),Id(r'a'))),Id(r'b')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,357))


    def test_associative_expression_358(self):
        '''sub or unary test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= -b--b---b-b;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'-',BinaryOp(r'-',BinaryOp(r'-',UnaryOp(r'-',Id(r'b')),UnaryOp(r'-',Id(r'b'))),UnaryOp(r'-',UnaryOp(r'-',Id(r'b')))),Id(r'b')))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))


    def test_associative_expression_359(self):
        '''Most of all operators associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= a[2]>3*(b+c) and then (-a div 2 or else not (a or c) and b<>0) ;
            end

            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'>',ArrayCell(Id(r'a'),IntLiteral(2)),BinaryOp(r'*',IntLiteral(3),BinaryOp(r'+',Id(r'b'),Id(r'c')))),BinaryOp(r'orelse',BinaryOp(r'div',UnaryOp(r'-',Id(r'a')),IntLiteral(2)),BinaryOp(r'<>',BinaryOp(r'and',UnaryOp(r'not',BinaryOp(r'or',Id(r'a'),Id(r'c'))),Id(r'b')),IntLiteral(0)))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,359))


    def test_associative_expression_360(self):
        '''Most of all operators associvity test'''
        input = """
            function main(x,y:integer):integer;
            var a,b,c:integer;
            begin
                a:= a*b[2] and a() and then a+2 and then a>=0 and not a ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'andthen',BinaryOp(r'and',BinaryOp(r'*',Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(2))),CallExpr(Id(r'a'),[])),BinaryOp(r'+',Id(r'a'),IntLiteral(2))),BinaryOp(r'>=',Id(r'a'),BinaryOp(r'and',IntLiteral(0),UnaryOp(r'not',Id(r'a'))))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,360))


    def test_multideclaration_361(self):
        input = """
            var a,b: integer;
            function main(x,y:integer):integer;
            var c: array[1 .. 3] of boolean;
            begin
                b:=1;
                for i:=1 to 10 do
                    begin
                        while b=1 do
                            begin
                                if a>0 then c[1]:=tRue; else c[1]:=False;
                                if a>1 then c[2]:=tRue; else c[2]:=False;
                                if a>2 then c[3]:=tRue; else c[3]:=False;
                                b:=0;
                            end
                    end
            end

            """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),FuncDecl(Id(r'main'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'c'),ArrayType(1,3,BoolType()))],[Assign(Id(r'b'),IntLiteral(1)),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[While(BinaryOp(r'=',Id(r'b'),IntLiteral(1)),[If(BinaryOp(r'>',Id(r'a'),IntLiteral(0)),[Assign(ArrayCell(Id(r'c'),IntLiteral(1)),BooleanLiteral(True))],[Assign(ArrayCell(Id(r'c'),IntLiteral(1)),BooleanLiteral(False))]),If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(ArrayCell(Id(r'c'),IntLiteral(2)),BooleanLiteral(True))],[Assign(ArrayCell(Id(r'c'),IntLiteral(2)),BooleanLiteral(False))]),If(BinaryOp(r'>',Id(r'a'),IntLiteral(2)),[Assign(ArrayCell(Id(r'c'),IntLiteral(3)),BooleanLiteral(True))],[Assign(ArrayCell(Id(r'c'),IntLiteral(3)),BooleanLiteral(False))]),Assign(Id(r'b'),IntLiteral(0))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,361))


    def test_multideclaration_362(self):
        input = """
            function add(x,y:integer):real ;
            BEGIN(*Ham cong hai so *)
                return x+y;
            END

            procedure main();
            begin
                write("Nhap 2 so can cong la: ");
                read(x,y);
                write("Ket qua cua phep cong la: ");
                print(add(x,y));
            end
            """
        expect = str(Program([FuncDecl(Id(r'add'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Return(BinaryOp(r'+',Id(r'x'),Id(r'y')))],FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Nhap 2 so can cong la: ')]),CallStmt(Id(r'read'),[Id(r'x'),Id(r'y')]),CallStmt(Id(r'write'),[StringLiteral(r'Ket qua cua phep cong la: ')]),CallStmt(Id(r'print'),[CallExpr(Id(r'add'),[Id(r'x'),Id(r'y')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))


    def test_multideclaration_363(self):
        input = """
            var x,y: integer;

            function addition(x,y:integer):real ;
            BEGIN(*Ham cong hai so *)
                return x+y;
            END

            function subtract(x,y:integer):real ;
            BEGIN(*Ham tru hai so *)
                return x-y;
            END

            function multiply(x,y:integer):real ;
            BEGIN(*Ham nhan hai so *)
                return x*y;
            END

            function division(x,y:integer):real ;
            BEGIN(*Ham chia hai so *)
                return x div y;
            END

            procedure main();
            begin
                write("Nhap 2 so can cong la: ");
                read(x,y);

                writeln("Ket qua cua phep cong la: ");
                print(addition(x,y));

                writeln("Ket qua cua phep tru la: ");
                print(subtract(x,y));

                writeln("Ket qua cua phep nhan la: ");
                print(multiply(x,y));

                writeln("Ket qua cua phep chia la: ");
                print(division(x,y));

            end
            """
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'addition'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Return(BinaryOp(r'+',Id(r'x'),Id(r'y')))],FloatType()),FuncDecl(Id(r'subtract'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Return(BinaryOp(r'-',Id(r'x'),Id(r'y')))],FloatType()),FuncDecl(Id(r'multiply'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Return(BinaryOp(r'*',Id(r'x'),Id(r'y')))],FloatType()),FuncDecl(Id(r'division'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Return(BinaryOp(r'div',Id(r'x'),Id(r'y')))],FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Nhap 2 so can cong la: ')]),CallStmt(Id(r'read'),[Id(r'x'),Id(r'y')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ket qua cua phep cong la: ')]),CallStmt(Id(r'print'),[CallExpr(Id(r'addition'),[Id(r'x'),Id(r'y')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ket qua cua phep tru la: ')]),CallStmt(Id(r'print'),[CallExpr(Id(r'subtract'),[Id(r'x'),Id(r'y')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ket qua cua phep nhan la: ')]),CallStmt(Id(r'print'),[CallExpr(Id(r'multiply'),[Id(r'x'),Id(r'y')])]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ket qua cua phep chia la: ')]),CallStmt(Id(r'print'),[CallExpr(Id(r'division'),[Id(r'x'),Id(r'y')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))


    def test_multideclaration_364(self):
        input = """
            procedure swap(a,b:integer);
            var t: integer;
            begin
                t:=b;
                b:=a;
                a:=t;
            end

            function max(x: array[1 .. 100] of integer):inTegEr;
            var num: integer;
            begin
                num:=x[1];
                for i:=1 to length(x) do
                    if x[i]>num then num:=x[i];

                return num;
            end

            procedure main();
            begin
            end

            """
        expect = str(Program([FuncDecl(Id(r'swap'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r't'),IntType())],[Assign(Id(r't'),Id(r'b')),Assign(Id(r'b'),Id(r'a')),Assign(Id(r'a'),Id(r't'))],VoidType()),FuncDecl(Id(r'max'),[VarDecl(Id(r'x'),ArrayType(1,100,IntType()))],[VarDecl(Id(r'num'),IntType())],[Assign(Id(r'num'),ArrayCell(Id(r'x'),IntLiteral(1))),For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'length'),[Id(r'x')]),True,[If(BinaryOp(r'>',ArrayCell(Id(r'x'),Id(r'i')),Id(r'num')),[Assign(Id(r'num'),ArrayCell(Id(r'x'),Id(r'i')))],[])]),Return(Id(r'num'))],IntType()),FuncDecl(Id(r'main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))


    def test_multideclaration_365(self):
        input = """
            var a, b, c: real;

            var x, y, z: Boolean;
                g, h, y: Integer;

            function abc(): Real;
            var x, y, z: Integer;

           begin
                read();
                // comment
                INthis := readStdin();
                with i: integer; do
                    begin
                        for ID := 4 downto -3 do hi := 6;
                        if i > 3 then return;
                        end

                return 0;
            end

            var q : integer;

            function f(): Boolean;
            begin
            (*
                begin
                end
            *)
            end

            """
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x'),BoolType()),VarDecl(Id(r'y'),BoolType()),VarDecl(Id(r'z'),BoolType()),VarDecl(Id(r'g'),IntType()),VarDecl(Id(r'h'),IntType()),VarDecl(Id(r'y'),IntType()),FuncDecl(Id(r'abc'),[],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType()),VarDecl(Id(r'z'),IntType())],[CallStmt(Id(r'read'),[]),Assign(Id(r'INthis'),CallExpr(Id(r'readStdin'),[])),With([VarDecl(Id(r'i'),IntType())],[For(Id(r'ID'),IntLiteral(4),UnaryOp(r'-',IntLiteral(3)),False,[Assign(Id(r'hi'),IntLiteral(6))]),If(BinaryOp(r'>',Id(r'i'),IntLiteral(3)),[Return(None)],[])]),Return(IntLiteral(0))],FloatType()),VarDecl(Id(r'q'),IntType()),FuncDecl(Id(r'f'),[],[],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,365))


    def test_comment_366(self):
        input = """
         procedure foo();
                var a: boolean;
                begin
                  //  a := TRUE and then 1 <= (1<>0) ;
                end
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[VarDecl(Id(r'a'),BoolType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))


    def test_comment_367(self):
        input = """
            procedure foo();
            begin
                a := b+c {*4^2 or *pow(4,2) ?} +d;
            end
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',Id(r'b'),Id(r'c')),Id(r'd')))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))


    def test_comment_368(self):
        input = """
            pRoCeDUre main();
             var a,b,c:real;
             begin
                write("Hello Phat");
                (*
                   a:=b;
                   b:=c;
                   c:=a;
                *)
             end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType())],[CallStmt(Id(r'write'),[StringLiteral(r'Hello Phat')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))


    def test_comment_369(self):
        input = """
             procedure foo();(*ten chuong trinh*)
                begin(*chuong trinh bat dau tu day*)
                    a := 1+2*3 div 4+5*6+7 ;(*thuc thi chuong trinh*)
             end(*chuong trinh ket thuc o day*)
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'+',IntLiteral(1),BinaryOp(r'div',BinaryOp(r'*',IntLiteral(2),IntLiteral(3)),IntLiteral(4))),BinaryOp(r'*',IntLiteral(5),IntLiteral(6))),IntLiteral(7)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))


    def test_comment_370(self):
        input = """
            {comment} function foo(c: string;a:array[1 ..{comment} 4] of {comment} string){comment}:{comment}boolean {comment};{comment}
                   var x,{comment}y:{comment} integer ;
                   BEGIN{comment}
                    foo(a,b,{comment}c{comment});
                    c := a[12{comment}] ;
                   END
            """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'c'),StringType()),VarDecl(Id(r'a'),ArrayType(1,4,StringType()))],[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[CallStmt(Id(r'foo'),[Id(r'a'),Id(r'b'),Id(r'c')]),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,370))


    def test_notice_scenario_371(self):
        input = """
            procedure main();
            var a,b:integer;
            begin
                if (a = 1) or (a = 2) AND (b = 3) then
                print();
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[If(BinaryOp(r'or',BinaryOp(r'=',Id(r'a'),IntLiteral(1)),BinaryOp(r'AND',BinaryOp(r'=',Id(r'a'),IntLiteral(2)),BinaryOp(r'=',Id(r'b'),IntLiteral(3)))),[CallStmt(Id(r'print'),[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))


    def test_notice_scenario_372(self):
        input = """
            PrOcEdUrE _1(A,__b,c_2:INTEGER; x,y,z:array[1 .. 3] of BOOLEAN) ;
            var x_, _y_, z : real; m,n: INTEGER;
            begin
            end
            """
        expect = str(Program([FuncDecl(Id(r'_1'),[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'__b'),IntType()),VarDecl(Id(r'c_2'),IntType()),VarDecl(Id(r'x'),ArrayType(1,3,BoolType())),VarDecl(Id(r'y'),ArrayType(1,3,BoolType())),VarDecl(Id(r'z'),ArrayType(1,3,BoolType()))],[VarDecl(Id(r'x_'),FloatType()),VarDecl(Id(r'_y_'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))


    def test_notice_scenario_373(self):
        input = """
            procedure _();
            vAr __ : STRING;
            begin
                foo := 1 * -2e09 div 3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'_'),[],[VarDecl(Id(r'__'),StringType())],[Assign(Id(r'foo'),BinaryOp(r'div',BinaryOp(r'*',IntLiteral(1),UnaryOp(r'-',FloatLiteral(2000000000.0))),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))


    def test_notice_scenario_374(self):
        input = """
            function foo (x:boolean):boolean;
            begin
            if a = 1 then
                begin
                    x := y := .1e2;
                    foo(True AND then false);
                end
            end

            """
        expect = str(Program([FuncDecl(Id(r'foo'),[VarDecl(Id(r'x'),BoolType())],[],[If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r'y'),FloatLiteral(10.0)),Assign(Id(r'x'),Id(r'y')),CallStmt(Id(r'foo'),[BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(False))])],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,374))


    def test_notice_scenario_375(self):
        input = """
            procedure foo();
            begin
            	a[1][2][3] := -.5e3;
            end

            """
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(ArrayCell(ArrayCell(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),UnaryOp(r'-',FloatLiteral(500.0)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))


    def test_notice_scenario_376(self):
        input = """
            procedure main();
            begin
                FOR x := -   1 TO (1+1)[1+1] do
                begin
                    PrintLn("Hello Guys");
                end
            end

            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[For(Id(r'x'),UnaryOp(r'-',IntLiteral(1)),ArrayCell(BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),BinaryOp(r'+',IntLiteral(1),IntLiteral(1))),True,[CallStmt(Id(r'PrintLn'),[StringLiteral(r'Hello Guys')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))


    def test_notice_scenario_377(self):
        input = """
            function main():rEaL;
            var _, __ : REAL; _1     : STRING;
            begin
                a := b := X := y := (Z+1)[0.0*3] := 1+1-2/3;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'_'),FloatType()),VarDecl(Id(r'__'),FloatType()),VarDecl(Id(r'_1'),StringType())],[Assign(ArrayCell(BinaryOp(r'+',Id(r'Z'),IntLiteral(1)),BinaryOp(r'*',FloatLiteral(0.0),IntLiteral(3))),BinaryOp(r'-',BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),BinaryOp(r'/',IntLiteral(2),IntLiteral(3)))),Assign(Id(r'y'),ArrayCell(BinaryOp(r'+',Id(r'Z'),IntLiteral(1)),BinaryOp(r'*',FloatLiteral(0.0),IntLiteral(3)))),Assign(Id(r'X'),Id(r'y')),Assign(Id(r'b'),Id(r'X')),Assign(Id(r'a'),Id(r'b'))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,377))


    def test_notice_scenario_378(self):
        input = """
            procedure main();
            begin
                e := a/b*c DIV 9e3Mod 2and FALSE ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'e'),BinaryOp(r'and',BinaryOp(r'Mod',BinaryOp(r'DIV',BinaryOp(r'*',BinaryOp(r'/',Id(r'a'),Id(r'b')),Id(r'c')),FloatLiteral(9000.0)),IntLiteral(2)),BooleanLiteral(False)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))


    def test_notice_scenario_379(self):
        input = """
            procedure main();
            begin
                e := ((1. = 2.) <> (3. < 4.)) <= ((5. > 6.) >= (7. = 8.));
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[],[Assign(Id(r'e'),BinaryOp(r'<=',BinaryOp(r'<>',BinaryOp(r'=',FloatLiteral(1.0),FloatLiteral(2.0)),BinaryOp(r'<',FloatLiteral(3.0),FloatLiteral(4.0))),BinaryOp(r'>=',BinaryOp(r'>',FloatLiteral(5.0),FloatLiteral(6.0)),BinaryOp(r'=',FloatLiteral(7.0),FloatLiteral(8.0)))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))


    def test_notice_scenario_380(self):
        input = """
            procedure main();
            var
                a: real;

            begin
                a := TRUE and then FALSE or     else True or      else (1 and       then 2) ;
            end
            """
        expect = str(Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),FloatType())],[Assign(Id(r'a'),BinaryOp(r'orelse',BinaryOp(r'orelse',BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BinaryOp(r'andthen',IntLiteral(1),IntLiteral(2))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))


    def test_random_program_381(self):
        '''Quick Sort test from Internet'''
        input = """
            Procedure QSort(numbers : Array [1 .. 100] of Integer; left : Integer; right : Integer);
            Var pivot, l_ptr, r_ptr : Integer;

            Begin
                l_ptr := left;
                r_ptr := right;
                pivot := numbers[left];

                While (left < right) do
                Begin
                        While ((numbers[right] >= pivot) AND (left < right)) do
                            right := right - 1;

                    If (left <> right) Then
                        Begin
                            numbers[left] := numbers[right];
                            left := left + 1;
                        End

                    While ((numbers[left] <= pivot) AND (left < right)) do
                        left := left + 1;

                    If (left <> right) Then
                        Begin
                            numbers[right] := numbers[left];
                            right := right - 1;
                        End
                End

                numbers[left] := pivot;
                pivot := left;
                left := l_ptr;
                right := r_ptr;

                If (left < pivot) Then
                    QSort(numbers, left, pivot-1);

                If (right > pivot) Then
                    QSort(numbers, pivot+1, right);
            End

            Procedure QuickSort(numbers : Array [1 .. 100] of Integer; size : Integer);
            Begin
                QSort(numbers, 0, size-1);
            End

            """
        expect = str(Program([FuncDecl(Id(r'QSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'left'),IntType()),VarDecl(Id(r'right'),IntType())],[VarDecl(Id(r'pivot'),IntType()),VarDecl(Id(r'l_ptr'),IntType()),VarDecl(Id(r'r_ptr'),IntType())],[Assign(Id(r'l_ptr'),Id(r'left')),Assign(Id(r'r_ptr'),Id(r'right')),Assign(Id(r'pivot'),ArrayCell(Id(r'numbers'),Id(r'left'))),While(BinaryOp(r'<',Id(r'left'),Id(r'right')),[While(BinaryOp(r'AND',BinaryOp(r'>=',ArrayCell(Id(r'numbers'),Id(r'right')),Id(r'pivot')),BinaryOp(r'<',Id(r'left'),Id(r'right'))),[Assign(Id(r'right'),BinaryOp(r'-',Id(r'right'),IntLiteral(1)))]),If(BinaryOp(r'<>',Id(r'left'),Id(r'right')),[Assign(ArrayCell(Id(r'numbers'),Id(r'left')),ArrayCell(Id(r'numbers'),Id(r'right'))),Assign(Id(r'left'),BinaryOp(r'+',Id(r'left'),IntLiteral(1)))],[]),While(BinaryOp(r'AND',BinaryOp(r'<=',ArrayCell(Id(r'numbers'),Id(r'left')),Id(r'pivot')),BinaryOp(r'<',Id(r'left'),Id(r'right'))),[Assign(Id(r'left'),BinaryOp(r'+',Id(r'left'),IntLiteral(1)))]),If(BinaryOp(r'<>',Id(r'left'),Id(r'right')),[Assign(ArrayCell(Id(r'numbers'),Id(r'right')),ArrayCell(Id(r'numbers'),Id(r'left'))),Assign(Id(r'right'),BinaryOp(r'-',Id(r'right'),IntLiteral(1)))],[])]),Assign(ArrayCell(Id(r'numbers'),Id(r'left')),Id(r'pivot')),Assign(Id(r'pivot'),Id(r'left')),Assign(Id(r'left'),Id(r'l_ptr')),Assign(Id(r'right'),Id(r'r_ptr')),If(BinaryOp(r'<',Id(r'left'),Id(r'pivot')),[CallStmt(Id(r'QSort'),[Id(r'numbers'),Id(r'left'),BinaryOp(r'-',Id(r'pivot'),IntLiteral(1))])],[]),If(BinaryOp(r'>',Id(r'right'),Id(r'pivot')),[CallStmt(Id(r'QSort'),[Id(r'numbers'),BinaryOp(r'+',Id(r'pivot'),IntLiteral(1)),Id(r'right')])],[])],VoidType()),FuncDecl(Id(r'QuickSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[],[CallStmt(Id(r'QSort'),[Id(r'numbers'),IntLiteral(0),BinaryOp(r'-',Id(r'size'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))


    def test_random_program_382(self):
        '''Stack ADT source from Internet'''
        input = """
         Var
            myStack : Array[1 .. 100] of Integer;
            topPointer : Integer;


        Procedure InitStack();
        Begin
            topPointer := 0;
        End
        //We now implemement the IsEmpty() and IsFull() functions.

        Function IsEmpty() : Boolean;
        Begin
            IsEmpty := False;
            If (topPointer = 0) Then
                IsEmpty := true;
        End

        Function IsFull() : Boolean;
        Begin
            IsFull := False;
            If ((topPointer + 1) = STACK_SIZE) Then
                IsFull := True;
        End
        //Here are the implementations of the Pop() and Push() functions and making use of the functions that we have just implemented.

        Function Pop() : Integer;

        Begin
            Pop := nil;

            If not IsEmpty Then
                Begin
                    Pop := myStack[topPointer];
                    topPointer := topPointer - 1;
                End
            End

        Procedure Push(item : Integer);
        Begin
            If not IsFull Then
                Begin
                    myStack[topPointer+1] := item;
                    topPointer := topPointer + 1;
                End
        End

        //Finally, we implement the utility function GetSize(). Although one can access the current size of the stack using the global variable topPointer, it is of good practice to make use of functions instead of global variables.

        Function GetSize() : Integer;
        Begin
            GetSize := topPointer;
        End

            """
        expect = str(Program([VarDecl(Id(r'myStack'),ArrayType(1,100,IntType())),VarDecl(Id(r'topPointer'),IntType()),FuncDecl(Id(r'InitStack'),[],[],[Assign(Id(r'topPointer'),IntLiteral(0))],VoidType()),FuncDecl(Id(r'IsEmpty'),[],[],[Assign(Id(r'IsEmpty'),BooleanLiteral(False)),If(BinaryOp(r'=',Id(r'topPointer'),IntLiteral(0)),[Assign(Id(r'IsEmpty'),BooleanLiteral(True))],[])],BoolType()),FuncDecl(Id(r'IsFull'),[],[],[Assign(Id(r'IsFull'),BooleanLiteral(False)),If(BinaryOp(r'=',BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1)),Id(r'STACK_SIZE')),[Assign(Id(r'IsFull'),BooleanLiteral(True))],[])],BoolType()),FuncDecl(Id(r'Pop'),[],[],[Assign(Id(r'Pop'),Id(r'nil')),If(UnaryOp(r'not',Id(r'IsEmpty')),[Assign(Id(r'Pop'),ArrayCell(Id(r'myStack'),Id(r'topPointer'))),Assign(Id(r'topPointer'),BinaryOp(r'-',Id(r'topPointer'),IntLiteral(1)))],[])],IntType()),FuncDecl(Id(r'Push'),[VarDecl(Id(r'item'),IntType())],[],[If(UnaryOp(r'not',Id(r'IsFull')),[Assign(ArrayCell(Id(r'myStack'),BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1))),Id(r'item')),Assign(Id(r'topPointer'),BinaryOp(r'+',Id(r'topPointer'),IntLiteral(1)))],[])],VoidType()),FuncDecl(Id(r'GetSize'),[],[],[Assign(Id(r'GetSize'),Id(r'topPointer'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,382))


    def test_random_program_383(self):
        '''Recursive Fibonacci from Internet'''
        input = """
         var
            i: integer;
            function fibonacci(n: integer): integer;

        begin
            if n=1 then fibonacci := 0;

            else if n=2 then fibonacci := 1;

                 else fibonacci := fibonacci(n-1) + fibonacci(n-2);
            end

         procedure main();
         begin
            for i:= 1 to 10 do

            write(fibonacci (i), "  ");
         end


            """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'fibonacci'),[VarDecl(Id(r'n'),IntType())],[],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'fibonacci'),IntLiteral(0))],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(2)),[Assign(Id(r'fibonacci'),IntLiteral(1))],[Assign(Id(r'fibonacci'),BinaryOp(r'+',CallExpr(Id(r'fibonacci'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1))]),CallExpr(Id(r'fibonacci'),[BinaryOp(r'-',Id(r'n'),IntLiteral(2))])))])])],IntType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'write'),[CallExpr(Id(r'fibonacci'),[Id(r'i')]),StringLiteral(r'  ')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))


    def test_random_program_384(self):
        '''BubbleSort from Internet'''
        input = """
            Procedure BubbleSort(numbers : Array[1 .. 100] of Integer; size : Integer);
            Var
            	i, j, temp : Integer;

            Begin
            	For i := size-1 DownTo 1 do
            		For j := 2 to i do
            			If (numbers[j-1] > numbers[j]) Then
            			Begin
            				temp := numbers[j-1];
            				numbers[j-1] := numbers[j];
            				numbers[j] := temp;
            			End

            End
            """
        expect = str(Program([FuncDecl(Id(r'BubbleSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),IntLiteral(1),False,[For(Id(r'j'),IntLiteral(2),Id(r'i'),True,[If(BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'temp'))],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))


    def test_random_program_385(self):
        '''insertionSort from Internet'''
        input = """
            Procedure InsertionSort(numbers : Array[1 .. 100] of Integer; size : Integer);
            Var
            	i, j, index : Integer;


            Begin
            	For i := 2 to size-1 do
            	Begin
            		index := numbers[i];
            		j := i;
            		While ((j > 1) AND (numbers[j-1] > index)) do
            		Begin
            			numbers[j] := numbers[j-1];
            			j := j - 1;
            		End
            		numbers[j] := index;
            	End
            End
            """
        expect = str(Program([FuncDecl(Id(r'InsertionSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'index'),IntType())],[For(Id(r'i'),IntLiteral(2),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),True,[Assign(Id(r'index'),ArrayCell(Id(r'numbers'),Id(r'i'))),Assign(Id(r'j'),Id(r'i')),While(BinaryOp(r'AND',BinaryOp(r'>',Id(r'j'),IntLiteral(1)),BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),Id(r'index'))),[Assign(ArrayCell(Id(r'numbers'),Id(r'j')),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(Id(r'j'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))]),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'index'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))


    def test_random_program_386(self):
        '''Prime Number test from Internet'''
        input = """
            var
               i, j:integer;

            procedure main();
            begin
               for i := 2 to 50 do

               begin
                  for j := 2 to i do
                     if (i mod j)=0  then
                        break; {* if factor found, not prime *}

                  if(j = i) then
                     writeln(i , " is prime" );
               end
            end

            """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),FuncDecl(Id(r'main'),[],[],[For(Id(r'i'),IntLiteral(2),IntLiteral(50),True,[For(Id(r'j'),IntLiteral(2),Id(r'i'),True,[If(BinaryOp(r'=',BinaryOp(r'mod',Id(r'i'),Id(r'j')),IntLiteral(0)),[Break()],[])]),If(BinaryOp(r'=',Id(r'j'),Id(r'i')),[CallStmt(Id(r'writeln'),[Id(r'i'),StringLiteral(r' is prime')])],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386))


    def test_random_program_387(self):
        '''Program from Internet'''
        input = """
        (* Demonstrates  some String actions *)
          (* that involve  names of people *)
          VAR FirstName,  LastName, FullName: STRING;
          Count,  NameCount, Gap: INTEGER;
          PROCEDURE main();
          BEGIN
          Space := "  ";
          Hyphen := "-";
          Greeting :=  "Hello there ";
          Write("Enter the  number of names: ");
          ReadLn(NameCount);
          WriteLn();
          WHILE NameCount  >0 DO BEGIN
          Write("Enter a  name, last name first: ");
          Read(FullName);
          Gap :=  POS(Space, FullName); { NOTE }
          IF Gap > 0  THEN BEGIN
          LastName :=  Copy(FullName, 1, Gap);
          Delete(FullName,  1, Gap); { NOTE }
          FirstName :=  FullName;
          IF Length(LastName) <= 4 THEN
          WriteLn("That is  a short last name");
          IF Pos(Hyphen,  LastName) <> 0 THEN
          WriteLn("That is  a hyphenated name");
          IF FirstName =  "Bill" THEN { etc., etc. }
          WriteLn("Bill is  a good name ");
          FullName :=  FirstName + Space + LastName;
          WriteLn(Greeting,  FullName);
          WriteLn();
          END { IF }
          NameCount :=  NameCount - 1;
          END { WHILE }
          END { NameParse  }
            """
        expect = str(Program([VarDecl(Id(r'FirstName'),StringType()),VarDecl(Id(r'LastName'),StringType()),VarDecl(Id(r'FullName'),StringType()),VarDecl(Id(r'Count'),IntType()),VarDecl(Id(r'NameCount'),IntType()),VarDecl(Id(r'Gap'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Space'),StringLiteral(r'  ')),Assign(Id(r'Hyphen'),StringLiteral(r'-')),Assign(Id(r'Greeting'),StringLiteral(r'Hello there ')),CallStmt(Id(r'Write'),[StringLiteral(r'Enter the  number of names: ')]),CallStmt(Id(r'ReadLn'),[Id(r'NameCount')]),CallStmt(Id(r'WriteLn'),[]),While(BinaryOp(r'>',Id(r'NameCount'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'Enter a  name, last name first: ')]),CallStmt(Id(r'Read'),[Id(r'FullName')]),Assign(Id(r'Gap'),CallExpr(Id(r'POS'),[Id(r'Space'),Id(r'FullName')])),If(BinaryOp(r'>',Id(r'Gap'),IntLiteral(0)),[Assign(Id(r'LastName'),CallExpr(Id(r'Copy'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')])),CallStmt(Id(r'Delete'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')]),Assign(Id(r'FirstName'),Id(r'FullName')),If(BinaryOp(r'<=',CallExpr(Id(r'Length'),[Id(r'LastName')]),IntLiteral(4)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a short last name')])],[]),If(BinaryOp(r'<>',CallExpr(Id(r'Pos'),[Id(r'Hyphen'),Id(r'LastName')]),IntLiteral(0)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a hyphenated name')])],[]),If(BinaryOp(r'=',Id(r'FirstName'),StringLiteral(r'Bill')),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Bill is  a good name ')])],[]),Assign(Id(r'FullName'),BinaryOp(r'+',BinaryOp(r'+',Id(r'FirstName'),Id(r'Space')),Id(r'LastName'))),CallStmt(Id(r'WriteLn'),[Id(r'Greeting'),Id(r'FullName')]),CallStmt(Id(r'WriteLn'),[])],[]),Assign(Id(r'NameCount'),BinaryOp(r'-',Id(r'NameCount'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))


    def test_random_program_388(self):
        '''Program from Internet'''
        input = """
        (* Demonstrates  some String actions *)
          (* that involve  names of people *)
          VAR FirstName,  LastName, FullName: STRING;
          Count,  NameCount, Gap: INTEGER;

          PROCEDURE main();
          BEGIN
              Space := "  ";
              Hyphen := "-";
              Greeting :=  "Hello there ";
              Write("Enter the  number of names: ");
              ReadLn(NameCount);
              WriteLn();
              WHILE NameCount  >0 DO
              BEGIN
                  Write("Enter a  name, last name first: ");
                  Read(FullName);
                  Gap :=  POS(Space, FullName); { NOTE }

                  IF Gap > 0  THEN
                  BEGIN
                      LastName :=  Copy(FullName, 1, Gap);
                      Delete(FullName,  1, Gap); { NOTE }
                      FirstName :=  FullName;
                      IF Length(LastName) <= 4 THEN
                      WriteLn("That is  a short last name");
                      IF Pos(Hyphen,  LastName) <> 0 THEN
                      WriteLn("That is  a hyphenated name");
                      IF FirstName =  "Bill" THEN { etc., etc. }
                      WriteLn("Bill is  a good name ");
                      FullName :=  FirstName + Space + LastName;
                      WriteLn(Greeting,  FullName);
                      WriteLn();
                  END { IF }

              NameCount :=  NameCount - 1;
              END { WHILE }
          END { NameParse  }
            """
        expect = str(Program([VarDecl(Id(r'FirstName'),StringType()),VarDecl(Id(r'LastName'),StringType()),VarDecl(Id(r'FullName'),StringType()),VarDecl(Id(r'Count'),IntType()),VarDecl(Id(r'NameCount'),IntType()),VarDecl(Id(r'Gap'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Space'),StringLiteral(r'  ')),Assign(Id(r'Hyphen'),StringLiteral(r'-')),Assign(Id(r'Greeting'),StringLiteral(r'Hello there ')),CallStmt(Id(r'Write'),[StringLiteral(r'Enter the  number of names: ')]),CallStmt(Id(r'ReadLn'),[Id(r'NameCount')]),CallStmt(Id(r'WriteLn'),[]),While(BinaryOp(r'>',Id(r'NameCount'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'Enter a  name, last name first: ')]),CallStmt(Id(r'Read'),[Id(r'FullName')]),Assign(Id(r'Gap'),CallExpr(Id(r'POS'),[Id(r'Space'),Id(r'FullName')])),If(BinaryOp(r'>',Id(r'Gap'),IntLiteral(0)),[Assign(Id(r'LastName'),CallExpr(Id(r'Copy'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')])),CallStmt(Id(r'Delete'),[Id(r'FullName'),IntLiteral(1),Id(r'Gap')]),Assign(Id(r'FirstName'),Id(r'FullName')),If(BinaryOp(r'<=',CallExpr(Id(r'Length'),[Id(r'LastName')]),IntLiteral(4)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a short last name')])],[]),If(BinaryOp(r'<>',CallExpr(Id(r'Pos'),[Id(r'Hyphen'),Id(r'LastName')]),IntLiteral(0)),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'That is  a hyphenated name')])],[]),If(BinaryOp(r'=',Id(r'FirstName'),StringLiteral(r'Bill')),[CallStmt(Id(r'WriteLn'),[StringLiteral(r'Bill is  a good name ')])],[]),Assign(Id(r'FullName'),BinaryOp(r'+',BinaryOp(r'+',Id(r'FirstName'),Id(r'Space')),Id(r'LastName'))),CallStmt(Id(r'WriteLn'),[Id(r'Greeting'),Id(r'FullName')]),CallStmt(Id(r'WriteLn'),[])],[]),Assign(Id(r'NameCount'),BinaryOp(r'-',Id(r'NameCount'),IntLiteral(1)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))


    def test_random_program_389(self):
        '''Program from Internet'''
        input = """
        (* Problem of  Interest on a loan *)
          (* Computes: the  Balloon Payment total interest *)
          VAR
          Amount,  Duration, Payment, Interest,
          Balance, Time,  IntSum: INTEGER;
          Rate: REAL;
          PROCEDURE main();
          BEGIN
          (* Input  necessary information *)
              Write("Enter  amount of loan: ");
              Read(Amount);
              Write("Enter  payment amount: ");
              Read(Payment);
              Write("Enter the  duration in months: ");
              Read(Duration);
              WriteLn("Enter  annual interest rate ");
              Write("as a  decimal percent: ");
              Read(Rate);
              Rate :=  Rate/1200; (* Convert to monthly *)
              (* Compute the  Ballon Payment *)
              Balance :=  Amount;
              IntSum := 0;
              Time := 1;
              WHILE Time <  Duration DO BEGIN
                  Interest :=  TRUNC(Balance * Rate);
                  Balance :=  Balance + Interest;
                  Balance :=  Balance - Payment;
                  IntSum := IntSum  + Interest;
                  Time := Time +  1;
                  (* Begin trace  ************************)
                  Write(Time);
                  Write(" Balance  = ");
                  WriteLn(Balance);
                  (* End trace  **************************)
              END (* WHILE *)
              (* Output all  required Results *)
              Write("Balloon  Balance is: ");
              WriteLn(Balance);
              Write("Total  interest is : ");
              WriteLn(IntSum);
          END (* Loan *)
            """
        expect = str(Program([VarDecl(Id(r'Amount'),IntType()),VarDecl(Id(r'Duration'),IntType()),VarDecl(Id(r'Payment'),IntType()),VarDecl(Id(r'Interest'),IntType()),VarDecl(Id(r'Balance'),IntType()),VarDecl(Id(r'Time'),IntType()),VarDecl(Id(r'IntSum'),IntType()),VarDecl(Id(r'Rate'),FloatType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Write'),[StringLiteral(r'Enter  amount of loan: ')]),CallStmt(Id(r'Read'),[Id(r'Amount')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter  payment amount: ')]),CallStmt(Id(r'Read'),[Id(r'Payment')]),CallStmt(Id(r'Write'),[StringLiteral(r'Enter the  duration in months: ')]),CallStmt(Id(r'Read'),[Id(r'Duration')]),CallStmt(Id(r'WriteLn'),[StringLiteral(r'Enter  annual interest rate ')]),CallStmt(Id(r'Write'),[StringLiteral(r'as a  decimal percent: ')]),CallStmt(Id(r'Read'),[Id(r'Rate')]),Assign(Id(r'Rate'),BinaryOp(r'/',Id(r'Rate'),IntLiteral(1200))),Assign(Id(r'Balance'),Id(r'Amount')),Assign(Id(r'IntSum'),IntLiteral(0)),Assign(Id(r'Time'),IntLiteral(1)),While(BinaryOp(r'<',Id(r'Time'),Id(r'Duration')),[Assign(Id(r'Interest'),CallExpr(Id(r'TRUNC'),[BinaryOp(r'*',Id(r'Balance'),Id(r'Rate'))])),Assign(Id(r'Balance'),BinaryOp(r'+',Id(r'Balance'),Id(r'Interest'))),Assign(Id(r'Balance'),BinaryOp(r'-',Id(r'Balance'),Id(r'Payment'))),Assign(Id(r'IntSum'),BinaryOp(r'+',Id(r'IntSum'),Id(r'Interest'))),Assign(Id(r'Time'),BinaryOp(r'+',Id(r'Time'),IntLiteral(1))),CallStmt(Id(r'Write'),[Id(r'Time')]),CallStmt(Id(r'Write'),[StringLiteral(r' Balance  = ')]),CallStmt(Id(r'WriteLn'),[Id(r'Balance')])]),CallStmt(Id(r'Write'),[StringLiteral(r'Balloon  Balance is: ')]),CallStmt(Id(r'WriteLn'),[Id(r'Balance')]),CallStmt(Id(r'Write'),[StringLiteral(r'Total  interest is : ')]),CallStmt(Id(r'WriteLn'),[Id(r'IntSum')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))


    def test_random_program_390(self):
        '''Recursive factorial from Internet'''
        input = """
            Function Factorial(n : Integer) : Integer;
            Var
            	Result : Integer;

            Begin
            	If n = 1 Then
            		Factorial := 1;
            	Else
            		Factorial := n*Factorial(n-1);
            End
            """
        expect = str(Program([FuncDecl(Id(r'Factorial'),[VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'Result'),IntType())],[If(BinaryOp(r'=',Id(r'n'),IntLiteral(1)),[Assign(Id(r'Factorial'),IntLiteral(1))],[Assign(Id(r'Factorial'),BinaryOp(r'*',Id(r'n'),CallExpr(Id(r'Factorial'),[BinaryOp(r'-',Id(r'n'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,390))


    def test_random_program_391(self):
        '''Quadratic equation from internet'''
        input = """
            procedure ptb2() ;
                VAR a,b,c,x1,x2,d:REAL;
                BEGIN
                     clrscr();
                     while(true) do begin
                          write("Nhap cac he so a, b, c: ");
                          readln(a,b,c);
                          if(a<>0) then break;
                     end
                     d:=sqr(b)-4*a*c;
                     IF d<0 THEN write("Phuong trinh vo nghiem!");
                     ELSE BEGIN
                          x1:=(-b-sqrt(d))/(2*a);
                          x2:=(-b+sqrt(d))/(2*a);
                          IF d=0 THEN writeln("Phuong trinh co nghiem kep x = ",x1);
                          ELSE writeln("Phuong trinh co 2 nghiem phan biet: ",x1,x2);
                     END
                     readln();
                END
            """
        expect = str(Program([FuncDecl(Id(r'ptb2'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'x1'),FloatType()),VarDecl(Id(r'x2'),FloatType()),VarDecl(Id(r'd'),FloatType())],[CallStmt(Id(r'clrscr'),[]),While(BooleanLiteral(True),[CallStmt(Id(r'write'),[StringLiteral(r'Nhap cac he so a, b, c: ')]),CallStmt(Id(r'readln'),[Id(r'a'),Id(r'b'),Id(r'c')]),If(BinaryOp(r'<>',Id(r'a'),IntLiteral(0)),[Break()],[])]),Assign(Id(r'd'),BinaryOp(r'-',CallExpr(Id(r'sqr'),[Id(r'b')]),BinaryOp(r'*',BinaryOp(r'*',IntLiteral(4),Id(r'a')),Id(r'c')))),If(BinaryOp(r'<',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'write'),[StringLiteral(r'Phuong trinh vo nghiem!')])],[Assign(Id(r'x1'),BinaryOp(r'/',BinaryOp(r'-',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),Assign(Id(r'x2'),BinaryOp(r'/',BinaryOp(r'+',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),If(BinaryOp(r'=',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co nghiem kep x = '),Id(r'x1')])],[CallStmt(Id(r'writeln'),[StringLiteral(r'Phuong trinh co 2 nghiem phan biet: '),Id(r'x1'),Id(r'x2')])])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))


    def test_random_program_392(self):
        '''GCD algorithm using division from Internet'''
        input = """
            function greatestCommonDivisor(a, b: integer): Integer;
            var
                temp: Integer;
            begin
              while b <> 0 do
              begin
                temp := b;
                b := a mod b;
                a := temp;
               end
              result := a;
            end
            """
        expect = str(Program([FuncDecl(Id(r'greatestCommonDivisor'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'temp'),IntType())],[While(BinaryOp(r'<>',Id(r'b'),IntLiteral(0)),[Assign(Id(r'temp'),Id(r'b')),Assign(Id(r'b'),BinaryOp(r'mod',Id(r'a'),Id(r'b'))),Assign(Id(r'a'),Id(r'temp'))]),Assign(Id(r'result'),Id(r'a'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,392))


    def test_random_program_393(self):
        '''GCD using Euclids Subtraction Method from Internet'''
        input = """
            function greatestCommonDivisor_euclidsSubtractionMethod(a, b: Integer): Integer;
            begin
              // only works with positive integers
              if (a < 0) then a := -a;
              if (b < 0) then b := -b;
              // don't enter loop, since subtracting zero won't break condition
              if (a = 0) then exit(b);
              if (b = 0) then exit(a);
              while not (a = b) do
              begin
                if (a > b) then
                 a := a - b;
                else
                 b := b - a;
              end
              result := a;
            end

            """
        expect = str(Program([FuncDecl(Id(r'greatestCommonDivisor_euclidsSubtractionMethod'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[If(BinaryOp(r'<',Id(r'a'),IntLiteral(0)),[Assign(Id(r'a'),UnaryOp(r'-',Id(r'a')))],[]),If(BinaryOp(r'<',Id(r'b'),IntLiteral(0)),[Assign(Id(r'b'),UnaryOp(r'-',Id(r'b')))],[]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(0)),[CallStmt(Id(r'exit'),[Id(r'b')])],[]),If(BinaryOp(r'=',Id(r'b'),IntLiteral(0)),[CallStmt(Id(r'exit'),[Id(r'a')])],[]),While(UnaryOp(r'not',BinaryOp(r'=',Id(r'a'),Id(r'b'))),[If(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),BinaryOp(r'-',Id(r'a'),Id(r'b')))],[Assign(Id(r'b'),BinaryOp(r'-',Id(r'b'),Id(r'a')))])]),Assign(Id(r'result'),Id(r'a'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,393))


    def test_random_program_394(self):
        '''Longest Common Subsequence (LCS) Algorithm from Internet'''
        input = """
            function lcs(a, b: string): string;
              var
                x, y: string;
                lenga, lengb: integer;
              begin
                lenga := length(a);
                lengb := length(b);
                lcs := " ";
                if (lenga >  0) and (lengb >  0) then
                  if a[lenga] =  b[lengb] then
                    lcs := lcs(copy(a, 1, lenga-1), copy(b, 1, lengb-1)) + a[lenga];
                  else
                  begin
                    x := lcs(a, copy(b, 1, lengb-1));
                    y := lcs(copy(a, 1, lenga-1), b);
                    if length(x) > length(y) then
                      lcs := x;
                    else
                      lcs := y;
                  end
              end

            procedure main();
            var
              s1, s2: string;
            begin
              s1 := "thisisatest";
              s2 := "testing123testing";
              writeln (lcs(s1, s2));
              s1 := "1234";
              s2 := "1224533324";
              writeln (lcs(s1, s2));
            end
            """
        expect = str(Program([FuncDecl(Id(r'lcs'),[VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())],[VarDecl(Id(r'x'),StringType()),VarDecl(Id(r'y'),StringType()),VarDecl(Id(r'lenga'),IntType()),VarDecl(Id(r'lengb'),IntType())],[Assign(Id(r'lenga'),CallExpr(Id(r'length'),[Id(r'a')])),Assign(Id(r'lengb'),CallExpr(Id(r'length'),[Id(r'b')])),Assign(Id(r'lcs'),StringLiteral(r' ')),If(BinaryOp(r'and',BinaryOp(r'>',Id(r'lenga'),IntLiteral(0)),BinaryOp(r'>',Id(r'lengb'),IntLiteral(0))),[If(BinaryOp(r'=',ArrayCell(Id(r'a'),Id(r'lenga')),ArrayCell(Id(r'b'),Id(r'lengb'))),[Assign(Id(r'lcs'),BinaryOp(r'+',CallExpr(Id(r'lcs'),[CallExpr(Id(r'copy'),[Id(r'a'),IntLiteral(1),BinaryOp(r'-',Id(r'lenga'),IntLiteral(1))]),CallExpr(Id(r'copy'),[Id(r'b'),IntLiteral(1),BinaryOp(r'-',Id(r'lengb'),IntLiteral(1))])]),ArrayCell(Id(r'a'),Id(r'lenga'))))],[Assign(Id(r'x'),CallExpr(Id(r'lcs'),[Id(r'a'),CallExpr(Id(r'copy'),[Id(r'b'),IntLiteral(1),BinaryOp(r'-',Id(r'lengb'),IntLiteral(1))])])),Assign(Id(r'y'),CallExpr(Id(r'lcs'),[CallExpr(Id(r'copy'),[Id(r'a'),IntLiteral(1),BinaryOp(r'-',Id(r'lenga'),IntLiteral(1))]),Id(r'b')])),If(BinaryOp(r'>',CallExpr(Id(r'length'),[Id(r'x')]),CallExpr(Id(r'length'),[Id(r'y')])),[Assign(Id(r'lcs'),Id(r'x'))],[Assign(Id(r'lcs'),Id(r'y'))])])],[])],StringType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r's1'),StringType()),VarDecl(Id(r's2'),StringType())],[Assign(Id(r's1'),StringLiteral(r'thisisatest')),Assign(Id(r's2'),StringLiteral(r'testing123testing')),CallStmt(Id(r'writeln'),[CallExpr(Id(r'lcs'),[Id(r's1'),Id(r's2')])]),Assign(Id(r's1'),StringLiteral(r'1234')),Assign(Id(r's2'),StringLiteral(r'1224533324')),CallStmt(Id(r'writeln'),[CallExpr(Id(r'lcs'),[Id(r's1'),Id(r's2')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))


    def test_random_program_395(self):
        '''Rabin-Karp Algorithm from Internet'''
        input = """
            function search ( pat: string;   Text: string) : integer;
            var
              hpat, htext,Bm, j, m,  n: integer;
              found : Boolean;
            begin
              found := False;
              result := 0;
              m := length(pat);
              if m = 0 then
              begin
                result := 1;
                found := true;
              end

               Bm := 1;
               hpat := 0;
               htext := 0;
               n := length (Text);
               if n >= m then
                 {*** preprocessing ***}
                 for j := 1 to m do
                 begin
                   Bm := Bm * b;
                   hpat := hpat * b + ord (pat[j]);
                   htext := htext * b + ord (Text[j]);
                 end

               j := m;
               {*** search ***}
               while not found do
               begin
                 if (hpat = htext) and (pat = Copy (Text, j - m + 1, m)) then
                 begin
                   result := j - m;
                   found := true;
                 end
                 if j < n then
                 begin
                   j := j + 1;
                   htext := htext * b - ord (Text[j - m]) * Bm + ord (Text[j]);
                 end
                 else
                   found := true;
               end
             end

            procedure main();
             begin
               writeln(Search("abcde", "0123456abcde"));
               writeln(Search("abcde", "012345678abcde"));
               writeln(Search("abcde", "0123456785785758"));
               readln();
            end
            """
        expect = str(Program([FuncDecl(Id(r'search'),[VarDecl(Id(r'pat'),StringType()),VarDecl(Id(r'Text'),StringType())],[VarDecl(Id(r'hpat'),IntType()),VarDecl(Id(r'htext'),IntType()),VarDecl(Id(r'Bm'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'found'),BoolType())],[Assign(Id(r'found'),BooleanLiteral(False)),Assign(Id(r'result'),IntLiteral(0)),Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'pat')])),If(BinaryOp(r'=',Id(r'm'),IntLiteral(0)),[Assign(Id(r'result'),IntLiteral(1)),Assign(Id(r'found'),BooleanLiteral(True))],[]),Assign(Id(r'Bm'),IntLiteral(1)),Assign(Id(r'hpat'),IntLiteral(0)),Assign(Id(r'htext'),IntLiteral(0)),Assign(Id(r'n'),CallExpr(Id(r'length'),[Id(r'Text')])),If(BinaryOp(r'>=',Id(r'n'),Id(r'm')),[For(Id(r'j'),IntLiteral(1),Id(r'm'),True,[Assign(Id(r'Bm'),BinaryOp(r'*',Id(r'Bm'),Id(r'b'))),Assign(Id(r'hpat'),BinaryOp(r'+',BinaryOp(r'*',Id(r'hpat'),Id(r'b')),CallExpr(Id(r'ord'),[ArrayCell(Id(r'pat'),Id(r'j'))]))),Assign(Id(r'htext'),BinaryOp(r'+',BinaryOp(r'*',Id(r'htext'),Id(r'b')),CallExpr(Id(r'ord'),[ArrayCell(Id(r'Text'),Id(r'j'))])))])],[]),Assign(Id(r'j'),Id(r'm')),While(UnaryOp(r'not',Id(r'found')),[If(BinaryOp(r'and',BinaryOp(r'=',Id(r'hpat'),Id(r'htext')),BinaryOp(r'=',Id(r'pat'),CallExpr(Id(r'Copy'),[Id(r'Text'),BinaryOp(r'+',BinaryOp(r'-',Id(r'j'),Id(r'm')),IntLiteral(1)),Id(r'm')]))),[Assign(Id(r'result'),BinaryOp(r'-',Id(r'j'),Id(r'm'))),Assign(Id(r'found'),BooleanLiteral(True))],[]),If(BinaryOp(r'<',Id(r'j'),Id(r'n')),[Assign(Id(r'j'),BinaryOp(r'+',Id(r'j'),IntLiteral(1))),Assign(Id(r'htext'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'*',Id(r'htext'),Id(r'b')),BinaryOp(r'*',CallExpr(Id(r'ord'),[ArrayCell(Id(r'Text'),BinaryOp(r'-',Id(r'j'),Id(r'm')))]),Id(r'Bm'))),CallExpr(Id(r'ord'),[ArrayCell(Id(r'Text'),Id(r'j'))])))],[Assign(Id(r'found'),BooleanLiteral(True))])])],IntType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[CallExpr(Id(r'Search'),[StringLiteral(r'abcde'),StringLiteral(r'0123456abcde')])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'Search'),[StringLiteral(r'abcde'),StringLiteral(r'012345678abcde')])]),CallStmt(Id(r'writeln'),[CallExpr(Id(r'Search'),[StringLiteral(r'abcde'),StringLiteral(r'0123456785785758')])]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))


    def test_random_program_396(self):
        '''Boyer-Moore Algorithm (BM Algorithm) from Internet'''
        input = """
            var

                bad_character_shift : array[0 .. 255] of Integer;
                good_suffix_shift : array[1 .. 100] of Integer;
                suff : array[1 .. 100] of Integer;

            //prepare bad character shift table
            procedure pre_bad_character_shift(pattern: String);
            var
                i: Integer;
                m: Integer;
            begin
                m := length(pattern);
                for i := 0 to 255 do
                    bad_character_shift[i] := m;

                for i := 1 to m - 1 do
                    bad_character_shift[pattern[i]] := m - i;

            end

            //prepare suff table
            procedure pre_suff(pattern: String);
            var
            i, j: Integer;
            m: Integer;
            begin
                m := length(pattern);

                suff[m] := m;
                for i := m - 1 downto 1 do
                begin
                    for j := 0 to i do
                        if pattern[i-j] <> pattern[m-j] then
                            break;
                    suff[i] := j;
                end

            end



          //prepare good_suffix_shift table
            procedure pre_good_suffix_shift(pattern: String);
            var
                i,j: Integer;
                m: Integer;
            begin

                m := length(pattern);

                pre_suff(pattern);

                for i := 1 to m do
                good_suffix_shift[i] := m;

                for i := m downto 1 do
                    if suff[i] = i then
                        for j := 0 to m - i do
                            if good_suffix_shift[j] = m then
                                good_suffix_shift[j] := m - i;

                for i := 1 to m do
                    good_suffix_shift[m - suff[i]] := m - i;
            end

            //Boyer-Moore algorithm
            procedure BM_alg(text: String; pattern: String);
            var
                i, j : Integer;
                found : Boolean;
                m : Integer;
                n : Integer;
            begin

                m := length(pattern);
                n := length(text);

                pre_bad_character_shift(pattern);
                pre_good_suffix_shift(pattern);

                j := 0;
                while (j <= n - m) do
                    begin
                        found := true;
                        for i := m downto 1 do
                        if pattern[i] <> text[i + j] then
                        begin
                            found := false;
                            break;
                        end
                        if found = true then
                            begin
                                write(IntToStr(j) + " ");
                                j := j + good_suffix_shift[1];
                            end
                        else
                            j := j + max(good_suffix_shift[i], bad_character_shift[text[i + j]] - m + i);
                    end

            end

            procedure main();
            var
                pattern : String;
                text : String;
            begin

                writeln("Podaj tekst");
                readln(text);

                writeln("Podaj wzorzec");
                readln(pattern);

                BM_alg(text, pattern);

                readln();

            end

            """
        expect = str(Program([VarDecl(Id(r'bad_character_shift'),ArrayType(0,255,IntType())),VarDecl(Id(r'good_suffix_shift'),ArrayType(1,100,IntType())),VarDecl(Id(r'suff'),ArrayType(1,100,IntType())),FuncDecl(Id(r'pre_bad_character_shift'),[VarDecl(Id(r'pattern'),StringType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'm'),IntType())],[Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'pattern')])),For(Id(r'i'),IntLiteral(0),IntLiteral(255),True,[Assign(ArrayCell(Id(r'bad_character_shift'),Id(r'i')),Id(r'm'))]),For(Id(r'i'),IntLiteral(1),BinaryOp(r'-',Id(r'm'),IntLiteral(1)),True,[Assign(ArrayCell(Id(r'bad_character_shift'),ArrayCell(Id(r'pattern'),Id(r'i'))),BinaryOp(r'-',Id(r'm'),Id(r'i')))])],VoidType()),FuncDecl(Id(r'pre_suff'),[VarDecl(Id(r'pattern'),StringType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'm'),IntType())],[Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'pattern')])),Assign(ArrayCell(Id(r'suff'),Id(r'm')),Id(r'm')),For(Id(r'i'),BinaryOp(r'-',Id(r'm'),IntLiteral(1)),IntLiteral(1),False,[For(Id(r'j'),IntLiteral(0),Id(r'i'),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'pattern'),BinaryOp(r'-',Id(r'i'),Id(r'j'))),ArrayCell(Id(r'pattern'),BinaryOp(r'-',Id(r'm'),Id(r'j')))),[Break()],[])]),Assign(ArrayCell(Id(r'suff'),Id(r'i')),Id(r'j'))])],VoidType()),FuncDecl(Id(r'pre_good_suffix_shift'),[VarDecl(Id(r'pattern'),StringType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'm'),IntType())],[Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'pattern')])),CallStmt(Id(r'pre_suff'),[Id(r'pattern')]),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[Assign(ArrayCell(Id(r'good_suffix_shift'),Id(r'i')),Id(r'm'))]),For(Id(r'i'),Id(r'm'),IntLiteral(1),False,[If(BinaryOp(r'=',ArrayCell(Id(r'suff'),Id(r'i')),Id(r'i')),[For(Id(r'j'),IntLiteral(0),BinaryOp(r'-',Id(r'm'),Id(r'i')),True,[If(BinaryOp(r'=',ArrayCell(Id(r'good_suffix_shift'),Id(r'j')),Id(r'm')),[Assign(ArrayCell(Id(r'good_suffix_shift'),Id(r'j')),BinaryOp(r'-',Id(r'm'),Id(r'i')))],[])])],[])]),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[Assign(ArrayCell(Id(r'good_suffix_shift'),BinaryOp(r'-',Id(r'm'),ArrayCell(Id(r'suff'),Id(r'i')))),BinaryOp(r'-',Id(r'm'),Id(r'i')))])],VoidType()),FuncDecl(Id(r'BM_alg'),[VarDecl(Id(r'text'),StringType()),VarDecl(Id(r'pattern'),StringType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'found'),BoolType()),VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'pattern')])),Assign(Id(r'n'),CallExpr(Id(r'length'),[Id(r'text')])),CallStmt(Id(r'pre_bad_character_shift'),[Id(r'pattern')]),CallStmt(Id(r'pre_good_suffix_shift'),[Id(r'pattern')]),Assign(Id(r'j'),IntLiteral(0)),While(BinaryOp(r'<=',Id(r'j'),BinaryOp(r'-',Id(r'n'),Id(r'm'))),[Assign(Id(r'found'),BooleanLiteral(True)),For(Id(r'i'),Id(r'm'),IntLiteral(1),False,[If(BinaryOp(r'<>',ArrayCell(Id(r'pattern'),Id(r'i')),ArrayCell(Id(r'text'),BinaryOp(r'+',Id(r'i'),Id(r'j')))),[Assign(Id(r'found'),BooleanLiteral(False)),Break()],[])]),If(BinaryOp(r'=',Id(r'found'),BooleanLiteral(True)),[CallStmt(Id(r'write'),[BinaryOp(r'+',CallExpr(Id(r'IntToStr'),[Id(r'j')]),StringLiteral(r' '))]),Assign(Id(r'j'),BinaryOp(r'+',Id(r'j'),ArrayCell(Id(r'good_suffix_shift'),IntLiteral(1))))],[Assign(Id(r'j'),BinaryOp(r'+',Id(r'j'),CallExpr(Id(r'max'),[ArrayCell(Id(r'good_suffix_shift'),Id(r'i')),BinaryOp(r'+',BinaryOp(r'-',ArrayCell(Id(r'bad_character_shift'),ArrayCell(Id(r'text'),BinaryOp(r'+',Id(r'i'),Id(r'j')))),Id(r'm')),Id(r'i'))])))])])],VoidType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'pattern'),StringType()),VarDecl(Id(r'text'),StringType())],[CallStmt(Id(r'writeln'),[StringLiteral(r'Podaj tekst')]),CallStmt(Id(r'readln'),[Id(r'text')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Podaj wzorzec')]),CallStmt(Id(r'readln'),[Id(r'pattern')]),CallStmt(Id(r'BM_alg'),[Id(r'text'),Id(r'pattern')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))


    def test_random_program_397(self):
        '''Knuth–Morris–Pratt (KMP) Algorithm from Internet'''
        input = """
            var
                m,n,i,j,t:Integer;
                wzorzec:String;
                tekst:String;
                P: array[1 .. 100] of Integer;

            procedure main();
            begin
                writeln("Podaj tekst");
                readln(tekst);
                writeln("Podaj wzorzec");
                readln(wzorzec);
                n:=length(tekst);
                m:=length(wzorzec);
                SetLength(P,m+1);


                P[0]:=0; P[1]:=0; t:=0;
                for j:=2 to m do
                    begin
                        while (t>0) and (wzorzec[t+1]<>wzorzec[j]) do t:=P[t];
                        if wzorzec[t+1]=wzorzec[j] then t:=t+1;
                        P[j]:=t;
                    end

                //Algorithm KMP
                writeln("Indeksy poczatkow wzorca w tekscie");
                i:=1; j:=0;
                while i<=n-m+1 do
                    begin
                        j:=P[j];
                        while ((j<m)and(wzorzec[j+1]=tekst[i+j])) do j:=j+1;
                        if j=m then writeln((IntToStr(i)));
                        i:=i+max(1,j-P[j]);
                    end
                readln();
            end
            """
        expect = str(Program([VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r't'),IntType()),VarDecl(Id(r'wzorzec'),StringType()),VarDecl(Id(r'tekst'),StringType()),VarDecl(Id(r'P'),ArrayType(1,100,IntType())),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Podaj tekst')]),CallStmt(Id(r'readln'),[Id(r'tekst')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Podaj wzorzec')]),CallStmt(Id(r'readln'),[Id(r'wzorzec')]),Assign(Id(r'n'),CallExpr(Id(r'length'),[Id(r'tekst')])),Assign(Id(r'm'),CallExpr(Id(r'length'),[Id(r'wzorzec')])),CallStmt(Id(r'SetLength'),[Id(r'P'),BinaryOp(r'+',Id(r'm'),IntLiteral(1))]),Assign(ArrayCell(Id(r'P'),IntLiteral(0)),IntLiteral(0)),Assign(ArrayCell(Id(r'P'),IntLiteral(1)),IntLiteral(0)),Assign(Id(r't'),IntLiteral(0)),For(Id(r'j'),IntLiteral(2),Id(r'm'),True,[While(BinaryOp(r'and',BinaryOp(r'>',Id(r't'),IntLiteral(0)),BinaryOp(r'<>',ArrayCell(Id(r'wzorzec'),BinaryOp(r'+',Id(r't'),IntLiteral(1))),ArrayCell(Id(r'wzorzec'),Id(r'j')))),[Assign(Id(r't'),ArrayCell(Id(r'P'),Id(r't')))]),If(BinaryOp(r'=',ArrayCell(Id(r'wzorzec'),BinaryOp(r'+',Id(r't'),IntLiteral(1))),ArrayCell(Id(r'wzorzec'),Id(r'j'))),[Assign(Id(r't'),BinaryOp(r'+',Id(r't'),IntLiteral(1)))],[]),Assign(ArrayCell(Id(r'P'),Id(r'j')),Id(r't'))]),CallStmt(Id(r'writeln'),[StringLiteral(r'Indeksy poczatkow wzorca w tekscie')]),Assign(Id(r'i'),IntLiteral(1)),Assign(Id(r'j'),IntLiteral(0)),While(BinaryOp(r'<=',Id(r'i'),BinaryOp(r'+',BinaryOp(r'-',Id(r'n'),Id(r'm')),IntLiteral(1))),[Assign(Id(r'j'),ArrayCell(Id(r'P'),Id(r'j'))),While(BinaryOp(r'and',BinaryOp(r'<',Id(r'j'),Id(r'm')),BinaryOp(r'=',ArrayCell(Id(r'wzorzec'),BinaryOp(r'+',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'tekst'),BinaryOp(r'+',Id(r'i'),Id(r'j'))))),[Assign(Id(r'j'),BinaryOp(r'+',Id(r'j'),IntLiteral(1)))]),If(BinaryOp(r'=',Id(r'j'),Id(r'm')),[CallStmt(Id(r'writeln'),[CallExpr(Id(r'IntToStr'),[Id(r'i')])])],[]),Assign(Id(r'i'),BinaryOp(r'+',Id(r'i'),CallExpr(Id(r'max'),[IntLiteral(1),BinaryOp(r'-',Id(r'j'),ArrayCell(Id(r'P'),Id(r'j')))])))]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))


    def test_random_program_398(self):
        '''Kruskal Algorithm from Internet '''
        input = """

            var     f:string;
                    u,v,c:array[1 .. 100] of integer;
                    root:array[1 .. 100] of integer;
                    n,m:integer;

            procedure docfile();
            var     i: inTegEr;
            begin
                    assign(f,fi); reset(f);
                    readln(f,n,m);
                    for i:=1 to m do
                            readln(f,u[i],v[i],c[i]);
                    close(f);
            end

            procedure swap(a,b:integer);
            var     z:integer;
            begin
                    z:=a;
                    a:=b;
                    b:=z;
            end

            function findroot(x:integer):integer;
            begin
                    if root[x]<>x then
                            root[x]:=findroot(root[x]);
                    exit(root[x]);
            end

            procedure union(x,y:integer);
            begin
                    root[x]:=y;
            end

            procedure kruskal();
            var     i,ur,uv:integer;
                    t:integer;
            begin
                    for i:=1 to n do root[i]:=i;
                    t:=0;
                    for i:=1 to m do
                            begin
                                    ur:=findroot(u[i]);
                                    uv:=findroot(v[i]);
                                    if ur<>uv then
                                            begin
                                                    union(ur,uv);
                                                    t:=t+c[i];
                                            end
                            end
                    writeln(t);
            end

            procedure main();
            begin
                    docfile();
                    Quicksort(1,m);
                    kruskal();
            end
            """
        expect = str(Program([VarDecl(Id(r'f'),StringType()),VarDecl(Id(r'u'),ArrayType(1,100,IntType())),VarDecl(Id(r'v'),ArrayType(1,100,IntType())),VarDecl(Id(r'c'),ArrayType(1,100,IntType())),VarDecl(Id(r'root'),ArrayType(1,100,IntType())),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'm'),IntType()),FuncDecl(Id(r'docfile'),[],[VarDecl(Id(r'i'),IntType())],[CallStmt(Id(r'assign'),[Id(r'f'),Id(r'fi')]),CallStmt(Id(r'reset'),[Id(r'f')]),CallStmt(Id(r'readln'),[Id(r'f'),Id(r'n'),Id(r'm')]),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[CallStmt(Id(r'readln'),[Id(r'f'),ArrayCell(Id(r'u'),Id(r'i')),ArrayCell(Id(r'v'),Id(r'i')),ArrayCell(Id(r'c'),Id(r'i'))])]),CallStmt(Id(r'close'),[Id(r'f')])],VoidType()),FuncDecl(Id(r'swap'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'z'),IntType())],[Assign(Id(r'z'),Id(r'a')),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'b'),Id(r'z'))],VoidType()),FuncDecl(Id(r'findroot'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'<>',ArrayCell(Id(r'root'),Id(r'x')),Id(r'x')),[Assign(ArrayCell(Id(r'root'),Id(r'x')),CallExpr(Id(r'findroot'),[ArrayCell(Id(r'root'),Id(r'x'))]))],[]),CallStmt(Id(r'exit'),[ArrayCell(Id(r'root'),Id(r'x'))])],IntType()),FuncDecl(Id(r'union'),[VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[],[Assign(ArrayCell(Id(r'root'),Id(r'x')),Id(r'y'))],VoidType()),FuncDecl(Id(r'kruskal'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'ur'),IntType()),VarDecl(Id(r'uv'),IntType()),VarDecl(Id(r't'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[Assign(ArrayCell(Id(r'root'),Id(r'i')),Id(r'i'))]),Assign(Id(r't'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[Assign(Id(r'ur'),CallExpr(Id(r'findroot'),[ArrayCell(Id(r'u'),Id(r'i'))])),Assign(Id(r'uv'),CallExpr(Id(r'findroot'),[ArrayCell(Id(r'v'),Id(r'i'))])),If(BinaryOp(r'<>',Id(r'ur'),Id(r'uv')),[CallStmt(Id(r'union'),[Id(r'ur'),Id(r'uv')]),Assign(Id(r't'),BinaryOp(r'+',Id(r't'),ArrayCell(Id(r'c'),Id(r'i'))))],[])]),CallStmt(Id(r'writeln'),[Id(r't')])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'docfile'),[]),CallStmt(Id(r'Quicksort'),[IntLiteral(1),Id(r'm')]),CallStmt(Id(r'kruskal'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))


    def test_random_program_399(self):
        '''Prim Algorithm from Internet '''
        input = """
        var
            f:string;
            adj,adc:array[0 .. 200] of integer;
            tmp,tmpc,head,u,v,C,heap,pos,d:array[0 .. 101] of integer;
            dd:array[0 .. 101] of boolean;
            n,m,k,s,t,nheap:integer;

        procedure swaps(u,v:integer);
        var     k,i,j:integer;
        begin
                k:=0;
                for i:=u to v do
                        begin
                                inc(k);
                                tmp[k]:=adj[i];
                                tmpc[k]:=adc[i];
                        end
                for i:=u to v do
                        begin
                                adj[i]:=tmp[k];
                                adc[i]:=tmpc[k];
                                dec(K);
                        end
        end

        procedure swap(a,b:integer);
        var     z:integer;
        begin
                z:=a;
                a:=b;
                b:=z;
        end

        procedure upheap(i:integer);
        begin
                if (i div 2=0) or (d[heap[i]]>d[heap[i div 2]]) then exit();
                swap(heap[i],heap[i div 2]);
                swap(pos[heap[i]],pos[heap[i div 2]]);
                upheap(i div 2);
        end


        procedure downheap(i:integer);
        var     j:integer;
        begin
                j:=i*2;
                if j>nHeap then exit();
                if (j<nHeap) and (d[heap[j]]>d[heap[j+1]]) then inc(j);
                if d[heap[i]]<=d[heap[j]] then exit();
                swap(heap[i],heap[j]);
                swap(pos[heap[i]],pos[heap[j]]);
                downheap(j);
        end

        procedure push(x:integer);
        begin
                inc(nHeap);
                heap[nHeap]:=x;
                upheap(Nheap);
        end

        function pop():integer;
        begin
                pop:=Heap[1];
                heap[1]:=heap[nheap];
                dec(nheap);
                downheap(1);
        end

        Procedure update(i:integer);
        Begin
                if (i=1) or (d[heap[i]]>d[heap[i div 2]]) then exit();
                swap(heap[i],heap[i div 2]);
                swap(pos[heap[i]],pos[heap[i div 2]]);
                update(i div 2);
        End

        procedure docfile();
        var     i,j:integer;
        begin
                assign(f,fi); reset(f);
                read(f,n,m);
                fillchar(head,sizeof(head),0);
                for i:=1 to m do
                        begin
                                read(f,u[i],v[i],c[i]);
                                inc(head[u[i]]);
                                inc(head[v[i]]);
                        end
                for i:=1 to n+1 do
                        head[i]:=head[i-1]+head[i];
                for i:=1 to m do
                        begin
                                adj[head[u[i]]]:=v[i];
                                adc[head[u[i]]]:=c[i];
                                dec(head[u[i]]);

                                adj[head[v[i]]]:=u[i];
                                adc[head[v[i]]]:=c[i];
                                dec(head[v[i]]);
                        end
                close(f);
                for i:=1 to n do
                    swaps(head[i]+1,head[i+1]);
        end


        procedure prim();
        var     i,j,u,v,res:integer;
        begin
                for i:=1 to n do
                        begin
                                heap[i]:=i;
                                pos[i]:=i;
                                d[i]:=maxc;
                        end
                d[1]:=0;
                fillchar(dd,sizeof(dd),false);
                nHeap:=n;
                Update(1);
                while nheap<>0 do
                        u:=pop;
                        dd[u]:=true;
                        for v:=head[u]+1 to head[u+1] do
                                if (not dd[adj[v]]) and (d[adj[v]]>adc[v]) then
                                        begin
                                                d[adj[v]]:=adc[v];
                                                upheap(pos[adj[v]]);
                                        end

                res:=0;
                for i:=1 to n do
                        res:=res+d[i];
                writeln(res);
        end

        procedure main();
        begin
                docfile();
                prim();
        end

            """
        expect = str(Program([VarDecl(Id(r'f'),StringType()),VarDecl(Id(r'adj'),ArrayType(0,200,IntType())),VarDecl(Id(r'adc'),ArrayType(0,200,IntType())),VarDecl(Id(r'tmp'),ArrayType(0,101,IntType())),VarDecl(Id(r'tmpc'),ArrayType(0,101,IntType())),VarDecl(Id(r'head'),ArrayType(0,101,IntType())),VarDecl(Id(r'u'),ArrayType(0,101,IntType())),VarDecl(Id(r'v'),ArrayType(0,101,IntType())),VarDecl(Id(r'C'),ArrayType(0,101,IntType())),VarDecl(Id(r'heap'),ArrayType(0,101,IntType())),VarDecl(Id(r'pos'),ArrayType(0,101,IntType())),VarDecl(Id(r'd'),ArrayType(0,101,IntType())),VarDecl(Id(r'dd'),ArrayType(0,101,BoolType())),VarDecl(Id(r'n'),IntType()),VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'k'),IntType()),VarDecl(Id(r's'),IntType()),VarDecl(Id(r't'),IntType()),VarDecl(Id(r'nheap'),IntType()),FuncDecl(Id(r'swaps'),[VarDecl(Id(r'u'),IntType()),VarDecl(Id(r'v'),IntType())],[VarDecl(Id(r'k'),IntType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[Assign(Id(r'k'),IntLiteral(0)),For(Id(r'i'),Id(r'u'),Id(r'v'),True,[CallStmt(Id(r'inc'),[Id(r'k')]),Assign(ArrayCell(Id(r'tmp'),Id(r'k')),ArrayCell(Id(r'adj'),Id(r'i'))),Assign(ArrayCell(Id(r'tmpc'),Id(r'k')),ArrayCell(Id(r'adc'),Id(r'i')))]),For(Id(r'i'),Id(r'u'),Id(r'v'),True,[Assign(ArrayCell(Id(r'adj'),Id(r'i')),ArrayCell(Id(r'tmp'),Id(r'k'))),Assign(ArrayCell(Id(r'adc'),Id(r'i')),ArrayCell(Id(r'tmpc'),Id(r'k'))),CallStmt(Id(r'dec'),[Id(r'K')])])],VoidType()),FuncDecl(Id(r'swap'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'z'),IntType())],[Assign(Id(r'z'),Id(r'a')),Assign(Id(r'a'),Id(r'b')),Assign(Id(r'b'),Id(r'z'))],VoidType()),FuncDecl(Id(r'upheap'),[VarDecl(Id(r'i'),IntType())],[],[If(BinaryOp(r'or',BinaryOp(r'=',BinaryOp(r'div',Id(r'i'),IntLiteral(2)),IntLiteral(0)),BinaryOp(r'>',ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2)))))),[CallStmt(Id(r'exit'),[])],[]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'heap'),Id(r'i')),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2)))]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2))))]),CallStmt(Id(r'upheap'),[BinaryOp(r'div',Id(r'i'),IntLiteral(2))])],VoidType()),FuncDecl(Id(r'downheap'),[VarDecl(Id(r'i'),IntType())],[VarDecl(Id(r'j'),IntType())],[Assign(Id(r'j'),BinaryOp(r'*',Id(r'i'),IntLiteral(2))),If(BinaryOp(r'>',Id(r'j'),Id(r'nHeap')),[CallStmt(Id(r'exit'),[])],[]),If(BinaryOp(r'and',BinaryOp(r'<',Id(r'j'),Id(r'nHeap')),BinaryOp(r'>',ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),Id(r'j'))),ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),BinaryOp(r'+',Id(r'j'),IntLiteral(1)))))),[CallStmt(Id(r'inc'),[Id(r'j')])],[]),If(BinaryOp(r'<=',ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),Id(r'j')))),[CallStmt(Id(r'exit'),[])],[]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'heap'),Id(r'i')),ArrayCell(Id(r'heap'),Id(r'j'))]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),Id(r'j')))]),CallStmt(Id(r'downheap'),[Id(r'j')])],VoidType()),FuncDecl(Id(r'push'),[VarDecl(Id(r'x'),IntType())],[],[CallStmt(Id(r'inc'),[Id(r'nHeap')]),Assign(ArrayCell(Id(r'heap'),Id(r'nHeap')),Id(r'x')),CallStmt(Id(r'upheap'),[Id(r'Nheap')])],VoidType()),FuncDecl(Id(r'pop'),[],[],[Assign(Id(r'pop'),ArrayCell(Id(r'Heap'),IntLiteral(1))),Assign(ArrayCell(Id(r'heap'),IntLiteral(1)),ArrayCell(Id(r'heap'),Id(r'nheap'))),CallStmt(Id(r'dec'),[Id(r'nheap')]),CallStmt(Id(r'downheap'),[IntLiteral(1)])],IntType()),FuncDecl(Id(r'update'),[VarDecl(Id(r'i'),IntType())],[],[If(BinaryOp(r'or',BinaryOp(r'=',Id(r'i'),IntLiteral(1)),BinaryOp(r'>',ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'd'),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2)))))),[CallStmt(Id(r'exit'),[])],[]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'heap'),Id(r'i')),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2)))]),CallStmt(Id(r'swap'),[ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),Id(r'i'))),ArrayCell(Id(r'pos'),ArrayCell(Id(r'heap'),BinaryOp(r'div',Id(r'i'),IntLiteral(2))))]),CallStmt(Id(r'update'),[BinaryOp(r'div',Id(r'i'),IntLiteral(2))])],VoidType()),FuncDecl(Id(r'docfile'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType())],[CallStmt(Id(r'assign'),[Id(r'f'),Id(r'fi')]),CallStmt(Id(r'reset'),[Id(r'f')]),CallStmt(Id(r'read'),[Id(r'f'),Id(r'n'),Id(r'm')]),CallStmt(Id(r'fillchar'),[Id(r'head'),CallExpr(Id(r'sizeof'),[Id(r'head')]),IntLiteral(0)]),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[CallStmt(Id(r'read'),[Id(r'f'),ArrayCell(Id(r'u'),Id(r'i')),ArrayCell(Id(r'v'),Id(r'i')),ArrayCell(Id(r'c'),Id(r'i'))]),CallStmt(Id(r'inc'),[ArrayCell(Id(r'head'),ArrayCell(Id(r'u'),Id(r'i')))]),CallStmt(Id(r'inc'),[ArrayCell(Id(r'head'),ArrayCell(Id(r'v'),Id(r'i')))])]),For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'n'),IntLiteral(1)),True,[Assign(ArrayCell(Id(r'head'),Id(r'i')),BinaryOp(r'+',ArrayCell(Id(r'head'),BinaryOp(r'-',Id(r'i'),IntLiteral(1))),ArrayCell(Id(r'head'),Id(r'i'))))]),For(Id(r'i'),IntLiteral(1),Id(r'm'),True,[Assign(ArrayCell(Id(r'adj'),ArrayCell(Id(r'head'),ArrayCell(Id(r'u'),Id(r'i')))),ArrayCell(Id(r'v'),Id(r'i'))),Assign(ArrayCell(Id(r'adc'),ArrayCell(Id(r'head'),ArrayCell(Id(r'u'),Id(r'i')))),ArrayCell(Id(r'c'),Id(r'i'))),CallStmt(Id(r'dec'),[ArrayCell(Id(r'head'),ArrayCell(Id(r'u'),Id(r'i')))]),Assign(ArrayCell(Id(r'adj'),ArrayCell(Id(r'head'),ArrayCell(Id(r'v'),Id(r'i')))),ArrayCell(Id(r'u'),Id(r'i'))),Assign(ArrayCell(Id(r'adc'),ArrayCell(Id(r'head'),ArrayCell(Id(r'v'),Id(r'i')))),ArrayCell(Id(r'c'),Id(r'i'))),CallStmt(Id(r'dec'),[ArrayCell(Id(r'head'),ArrayCell(Id(r'v'),Id(r'i')))])]),CallStmt(Id(r'close'),[Id(r'f')]),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[CallStmt(Id(r'swaps'),[BinaryOp(r'+',ArrayCell(Id(r'head'),Id(r'i')),IntLiteral(1)),ArrayCell(Id(r'head'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)))])])],VoidType()),FuncDecl(Id(r'prim'),[],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'u'),IntType()),VarDecl(Id(r'v'),IntType()),VarDecl(Id(r'res'),IntType())],[For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[Assign(ArrayCell(Id(r'heap'),Id(r'i')),Id(r'i')),Assign(ArrayCell(Id(r'pos'),Id(r'i')),Id(r'i')),Assign(ArrayCell(Id(r'd'),Id(r'i')),Id(r'maxc'))]),Assign(ArrayCell(Id(r'd'),IntLiteral(1)),IntLiteral(0)),CallStmt(Id(r'fillchar'),[Id(r'dd'),CallExpr(Id(r'sizeof'),[Id(r'dd')]),BooleanLiteral(False)]),Assign(Id(r'nHeap'),Id(r'n')),CallStmt(Id(r'Update'),[IntLiteral(1)]),While(BinaryOp(r'<>',Id(r'nheap'),IntLiteral(0)),[Assign(Id(r'u'),Id(r'pop'))]),Assign(ArrayCell(Id(r'dd'),Id(r'u')),BooleanLiteral(True)),For(Id(r'v'),BinaryOp(r'+',ArrayCell(Id(r'head'),Id(r'u')),IntLiteral(1)),ArrayCell(Id(r'head'),BinaryOp(r'+',Id(r'u'),IntLiteral(1))),True,[If(BinaryOp(r'and',UnaryOp(r'not',ArrayCell(Id(r'dd'),ArrayCell(Id(r'adj'),Id(r'v')))),BinaryOp(r'>',ArrayCell(Id(r'd'),ArrayCell(Id(r'adj'),Id(r'v'))),ArrayCell(Id(r'adc'),Id(r'v')))),[Assign(ArrayCell(Id(r'd'),ArrayCell(Id(r'adj'),Id(r'v'))),ArrayCell(Id(r'adc'),Id(r'v'))),CallStmt(Id(r'upheap'),[ArrayCell(Id(r'pos'),ArrayCell(Id(r'adj'),Id(r'v')))])],[])]),Assign(Id(r'res'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[Assign(Id(r'res'),BinaryOp(r'+',Id(r'res'),ArrayCell(Id(r'd'),Id(r'i'))))]),CallStmt(Id(r'writeln'),[Id(r'res')])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'docfile'),[]),CallStmt(Id(r'prim'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))


    def test_random_program_400(self):
        '''Monte Carlo Program from Internet'''
        input = """
            var S,V,x,intguess,varguess,stddev,squarerootlerun,errfifty,errninety,errninetyfive:real;
                i,seed,answer:integer;

            function Rand (Seed: integer): real;
            {Generate pseudo random number between 0 and 1}

            begin
                Modulus := 65536;
                Multiplier := 25173;
                Increment := 13849;
                Seed := ((Multiplier * Seed) + Increment)  mod Modulus;
                Rand := Seed / Modulus;
            end

            function randomfunction():real;
            var a,b,c,d:real;
            begin
                a:=rand(seed);b:=rand(seed);c:=rand(seed);d:=rand(seed);
                randomfunction:=abs(a*d-b*c);
            end

            procedure main();
            begin
                Seed := 21877;
                while (answer<>0) do
                    S:=0;V:=0;
                    for i:=1 to lengthofrun do
                        begin
                              x:=randomfunction;
                              S:=S+x;
                              V:=V+sqr(x);
                         end

                    intguess:=S div lengthofrun;
                    varguess:=V div lengthofrun-sqr(intguess);
                    stddev:= sqrt(varguess);
                    squarerootlerun:=sqrt(lengthofrun);
                    errfifty:= 0.6745*stddev div squarerootlerun;
                    errninety:= 1.645*stddev div squarerootlerun;
                    errninetyfive:= 1.960*stddev div squarerootlerun;
                    writeln("average for this run = ",intguess);
                    writeln("estimated standard deviation = ",stddev);
                    writeln("with probability 50 percent and your error is less than ",errfifty);
                    writeln("with probability 90 percent and your error is less than ",errninety);
                    writeln("with probability 95 percent and your error is less than ",errninetyfive);
                    writeln("another run 1 with new seed and 2 without");
                    readln(answer);
                    if (answer=1) then
                        begin
                            writeln("enter a new seed and which should be an integer");
                            readln(seed);
                        end
            end

            """
        expect = str(Program([VarDecl(Id(r'S'),FloatType()),VarDecl(Id(r'V'),FloatType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'intguess'),FloatType()),VarDecl(Id(r'varguess'),FloatType()),VarDecl(Id(r'stddev'),FloatType()),VarDecl(Id(r'squarerootlerun'),FloatType()),VarDecl(Id(r'errfifty'),FloatType()),VarDecl(Id(r'errninety'),FloatType()),VarDecl(Id(r'errninetyfive'),FloatType()),VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'seed'),IntType()),VarDecl(Id(r'answer'),IntType()),FuncDecl(Id(r'Rand'),[VarDecl(Id(r'Seed'),IntType())],[],[Assign(Id(r'Modulus'),IntLiteral(65536)),Assign(Id(r'Multiplier'),IntLiteral(25173)),Assign(Id(r'Increment'),IntLiteral(13849)),Assign(Id(r'Seed'),BinaryOp(r'mod',BinaryOp(r'+',BinaryOp(r'*',Id(r'Multiplier'),Id(r'Seed')),Id(r'Increment')),Id(r'Modulus'))),Assign(Id(r'Rand'),BinaryOp(r'/',Id(r'Seed'),Id(r'Modulus')))],FloatType()),FuncDecl(Id(r'randomfunction'),[],[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'b'),FloatType()),VarDecl(Id(r'c'),FloatType()),VarDecl(Id(r'd'),FloatType())],[Assign(Id(r'a'),CallExpr(Id(r'rand'),[Id(r'seed')])),Assign(Id(r'b'),CallExpr(Id(r'rand'),[Id(r'seed')])),Assign(Id(r'c'),CallExpr(Id(r'rand'),[Id(r'seed')])),Assign(Id(r'd'),CallExpr(Id(r'rand'),[Id(r'seed')])),Assign(Id(r'randomfunction'),CallExpr(Id(r'abs'),[BinaryOp(r'-',BinaryOp(r'*',Id(r'a'),Id(r'd')),BinaryOp(r'*',Id(r'b'),Id(r'c')))]))],FloatType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'Seed'),IntLiteral(21877)),While(BinaryOp(r'<>',Id(r'answer'),IntLiteral(0)),[Assign(Id(r'S'),IntLiteral(0))]),Assign(Id(r'V'),IntLiteral(0)),For(Id(r'i'),IntLiteral(1),Id(r'lengthofrun'),True,[Assign(Id(r'x'),Id(r'randomfunction')),Assign(Id(r'S'),BinaryOp(r'+',Id(r'S'),Id(r'x'))),Assign(Id(r'V'),BinaryOp(r'+',Id(r'V'),CallExpr(Id(r'sqr'),[Id(r'x')])))]),Assign(Id(r'intguess'),BinaryOp(r'div',Id(r'S'),Id(r'lengthofrun'))),Assign(Id(r'varguess'),BinaryOp(r'-',BinaryOp(r'div',Id(r'V'),Id(r'lengthofrun')),CallExpr(Id(r'sqr'),[Id(r'intguess')]))),Assign(Id(r'stddev'),CallExpr(Id(r'sqrt'),[Id(r'varguess')])),Assign(Id(r'squarerootlerun'),CallExpr(Id(r'sqrt'),[Id(r'lengthofrun')])),Assign(Id(r'errfifty'),BinaryOp(r'div',BinaryOp(r'*',FloatLiteral(0.6745),Id(r'stddev')),Id(r'squarerootlerun'))),Assign(Id(r'errninety'),BinaryOp(r'div',BinaryOp(r'*',FloatLiteral(1.645),Id(r'stddev')),Id(r'squarerootlerun'))),Assign(Id(r'errninetyfive'),BinaryOp(r'div',BinaryOp(r'*',FloatLiteral(1.96),Id(r'stddev')),Id(r'squarerootlerun'))),CallStmt(Id(r'writeln'),[StringLiteral(r'average for this run = '),Id(r'intguess')]),CallStmt(Id(r'writeln'),[StringLiteral(r'estimated standard deviation = '),Id(r'stddev')]),CallStmt(Id(r'writeln'),[StringLiteral(r'with probability 50 percent and your error is less than '),Id(r'errfifty')]),CallStmt(Id(r'writeln'),[StringLiteral(r'with probability 90 percent and your error is less than '),Id(r'errninety')]),CallStmt(Id(r'writeln'),[StringLiteral(r'with probability 95 percent and your error is less than '),Id(r'errninetyfive')]),CallStmt(Id(r'writeln'),[StringLiteral(r'another run 1 with new seed and 2 without')]),CallStmt(Id(r'readln'),[Id(r'answer')]),If(BinaryOp(r'=',Id(r'answer'),IntLiteral(1)),[CallStmt(Id(r'writeln'),[StringLiteral(r'enter a new seed and which should be an integer')]),CallStmt(Id(r'readln'),[Id(r'seed')])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,400))
