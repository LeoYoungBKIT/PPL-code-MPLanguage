import unittest
from TestUtils import TestChecker
from AST import *

# Redeclared Variable: 9
# Redeclared Function: 3
# Redeclared Procedure: 3
# Redeclared Parameter: 3
# Undeclared Identifier: 5
# Undeclared Function: 5
# Undeclared Procedure: 3
# Type Mismatch In Statement: 23
## for: 4
## while: 4
## if: 4
## assign: 3
## return: 4
## procedure call: 4
# Type Mismatch In Expression: 10
# Function not return: 5
# Break/Continue not in loop: 5
# No Entry Point: 3
# Unreachable statement: 5
# Unreachable function/procedure: 5
# Test Random: 13

class CheckerSuite(unittest.TestCase):
# Redeclared Variable: 9
    def test_redeclared_variable_1(self):
        """ Test "Redeclared Variable" error: redeclaration in global vardecl """
        input = """
        var a, b, c, a: integer;

        procedure main();
        begin
            return;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_2(self):
        """ Test "Redeclared Variable" error: redeclaration in global vardecl """
        input = """
        var a, b, c: integer;
                x,y: string;
                a,z: array[1 .. 5] of Real;

        procedure main();
        begin
            return;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_3(self):
        """ Test "Redeclared Variable" error: redeclaration in local vardecl of function """
        input = """
        var a, b, c:integer;

        procedure main();
        var a:integer;
            b,a:real;
        begin
            return;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_4(self):
        """ Test "Redeclared Variable" error: redeclaration in local vardecl of function """
        input = """
        var a, b, c:integer;

        procedure main();
        var a,x,z,a:integer;
            b,m,n:real;
        begin
            return;
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_5(self):
        """ Test "Redeclared Variable" error: redeclaration in "with" block scope """
        input = """
        var a,b,c:integer;

        procedure main();
        begin
            with x,y,z:integer;
                x:array [1 .. 2] of integer;
            do begin end

            return;
        end
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable_6(self):
        """ Test "Redeclared Variable" error: redeclaration of param in local vardecl of function """
        input = """
        var a,b,c:integer;

        procedure ppl(asgmt3: boolean);
        var asgmt3: integer;
        begin
            return;
        end

        procedure main();
        begin
            ppl(true);
            return;
        end
        """
        expect = "Redeclared Variable: asgmt3"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable_7(self):
        """ Test "Redeclared Variable" error: redeclaration of procedure in global vardecl """
        input = """
        var a,b,c:integer;

        procedure ppl(asgmt3: boolean);
        begin
            return;
        end

        var ppl: array[1 .. 4] of BooLean;

        procedure main();
        begin
            ppl(true);
            return;
        end
        """
        expect = "Redeclared Variable: ppl"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable_8(self):
        """ Test "Redeclared Variable" error: redeclaration of function in global vardecl """
        input = """
        var a,b,c:integer;

        function ppl(asgmt3: boolean):BooLean;
        begin
            return true;
        end

        var ppl: array[1 .. 4] of BooLean;

        procedure main();
        var x:boolean;
        begin
            x:=ppl(true);
            return;
        end
        """
        expect = "Redeclared Variable: ppl"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_variable_9(self):
        """ Test "Redeclared Variable" error: redeclaration of another vardecl in global vardecl """
        input = """
        var a,b,c:integer;

        procedure main();
        begin
            return;
        end

        var a: array[1 .. 4] of BooLean;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

# Redeclared Function: 3
    def test_redeclared_function_1(self):
        """ Test "Redeclared Function" error: redeclaration of another funcdecl in global vardecl """
        input = """
        var a, b, c:integer;

        function ppl(asgmt3: boolean):BooLean;
        begin
            return true;
        end

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(false);
            asgmt2:=ppl(true);
            return false;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            return;
        end
        """
        expect = "Redeclared Function: ppl"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_function_2(self):
        """ Test "Redeclared Function" error: redeclaration of prodecl in global vardecl """
        input = """
        var a, b, c:integer;

        procedure ppl(asgmt3: boolean);
        begin
            return;
        end

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(false);
            ppl(true);
            return true;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            return;
        end
        """
        expect = "Redeclared Function: ppl"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_function_3(self):
        """ Test "Redeclared Function" error: redeclaration of vardecl in global vardecl """
        input = """
        var a, b, ppl:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(true);
            return true;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            return;
        end
        """
        expect = "Redeclared Function: ppl"
        self.assertTrue(TestChecker.test(input,expect,411))

# Redeclared Procedure: 3
    def test_redeclared_procedure_1(self):
        """ Test "Redeclared Procedure" error: redeclaration of another prodecl in global vardecl """
        input = """
        var a, b, c:integer;

        procedure ppl(asgmt3: boolean);
        begin
            asgmt3:=true;
            return;
        end

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        procedure ppl(asgmt2,asgmt3: boolean);
        begin
            ppl2018(false);
            asgmt2:=ppl(true);
            return;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            y:=ppl(true);
            return;
        end
        """
        expect = "Redeclared Procedure: ppl"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclared_procedure_2(self):
        """ Test "Redeclared Procedure" error: redeclaration of fundecl in global vardecl """
        input = """
        var a, b, c:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(false);
            ppl(true);
            return true;
        end

        procedure ppl(asgmt3: boolean);
        begin
            return;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            return;
        end
        """
        expect = "Redeclared Procedure: ppl"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclared_procedure_3(self):
        """ Test "Redeclared Function" error: redeclaration of vardecl in global vardecl """
        input = """
        var a, b, ppl:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        procedure ppl(asgmt2,asgmt3: boolean);
        begin
            ppl2018(true);
            return;
        end

        procedure main();
        var x,y:boolean;
        begin
            ppl(true,true);
            return;
        end
        """
        expect = "Redeclared Procedure: ppl"
        self.assertTrue(TestChecker.test(input,expect,414))

# Redeclared Parameter: 3
    def test_redeclared_parameter_1(self):
        """ Test "Redeclared Parameter" error: simple test """
        input = """
        var a, b, c:integer;

        procedure main(a,x,y,z,a:integer;b:real;c:string);
        begin
            return;
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_redeclared_parameter_2(self):
        """ Test "Redeclared Parameter" error: same name and different type """
        input = """
        var a, b, c:integer;

        procedure main(a,x,y,z:integer; b:real; c:string; a:array[1 .. 4] of BooLean);
        begin
            return;
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_redeclared_parameter_3(self):
        """ Test "Redeclared Parameter" error: Redeclared param in prodecl/fundecl but not "main" procedure """
        input = """
        var a, b, c:integer;

        procedure ppl(asgmt1,asgmt2,asgmt3: boolean;asgmt4,asgmt3:boolean);
        begin
            return;
        end

        procedure main();
        begin
            ppl(true,true,true,true,true);
            return;
        end
        """
        expect = "Redeclared Parameter: asgmt3"
        self.assertTrue(TestChecker.test(input,expect,417))

# Undeclared Identifier: 5
    def test_undeclared_identifier_1(self):
        """ Test "Undeclared Identifier" error: Undeclared Identifier in Expression """
        input = """
        var a, b, c:integer;

        procedure main();
        begin
            a:= asgmt1 + 1;
            return;
        end
        """
        expect = "Undeclared Identifier: asgmt1"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_identifier_2(self):
        """ Test "Undeclared Identifier" error: Undeclared Identifier in "Assign" statement """
        input = """
        var a, b, c:integer;

        procedure main();
        begin
            asgmt1:= a + 1;
            return;
        end
        """
        expect = "Undeclared Identifier: asgmt1"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_identifier_3(self):
        """ Test "Undeclared Identifier" error: Undeclared Identifier in "If" statement """
        input = """
        var a, b, c:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(true);
            asgmt2:=ppl(true,true);
            return true;
        end

        procedure pplwinter18(asgmt1: boolean);
        begin
            if asgmt1 then begin asgmt2 := true; end
            return;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            pplwinter18(true);
            return;
        end
        """
        expect = "Undeclared Identifier: asgmt2"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_identifier_4(self):
        """ Test "Undeclared Identifier" error: Undeclared Identifier in "Return" statement """
        input = """
        var a, b, c:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(true);
            asgmt2:=ppl(true,true);
            return asgmt1;
        end

        procedure pplwinter18(asgmt1,asgmt2: boolean);
        begin
            if asgmt1 then begin asgmt2 := true; end
            return;
        end

        procedure main();
        var x,y:boolean;
        begin
            x:=ppl(true,true);
            pplwinter18(true,true);
            return;
        end
        """
        expect = "Undeclared Identifier: asgmt1"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_identifier_5(self):
        """ Test "Undeclared Identifier" error: Undeclared Identifier in "While" statement """
        input = """
        var a, b, c:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2,asgmt3: boolean):BooLean;
        begin
            ppl2018(true);
            asgmt2:=ppl(true,true);
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: boolean);
        begin
            while asgmt3 do begin asgmt2 := true;  end
            return;
        end

        procedure main();
        var x:boolean;
        begin
            x:=ppl(true,true);
            pplwinter18(true,true);
            return;
        end
        """
        expect = "Undeclared Identifier: asgmt3"
        self.assertTrue(TestChecker.test(input,expect,422))


# Undeclared Function: 5
    def test_undeclared_function_1(self):
        """ Test "Undeclared Function" error: Declare Procedure but use as Function """
        input = """
        var a, b, c:integer;

        procedure ppl2018(asgmt3: boolean);
        begin
            return;
        end

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            ppl2018(true);
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2;  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(1998,"hello ppl 2018");
            k:=ppl2018(true);
            pplwinter18(10,11,true);
            return;
        end
        """
        expect = "Undeclared Function: ppl2018"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_function_2(self):
        """ Test "Undeclared Function" error: Sinple Undeclared Function """
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2 + ppl2018(1,2,3);  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018");
            pplwinter18(10,11,true);
            return;
        end
        """
        expect = "Undeclared Function: ppl2018"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function_3(self):
        """ Test "Undeclared Function" error: Subtitute Undeclared Function """
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2;  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),ppl2018("hello ppl 2018"));
            pplwinter18(10,11,true);
            return;
        end
        """
        expect = "Undeclared Function: ppl2018"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_function_4(self):
        """ Test "Undeclared Function" error: Return Undeclared Function """
        input = """
        var a, b, c:integer;

        function ppl1(asgmt2:integer;asgmt3: string): integer;
        begin
            return ppl2(2,"hai");
        end

        function ppl2(asgmt2:integer;asgmt3: string): integer;
        begin
            return ppl3(3,"ba");
        end

        function ppl3(asgmt2:integer;asgmt3: string): integer;
        begin
            return ppl0(0,"khong") + ppl1(1,"mot") + ppl2(2,"hai");
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl1(1,"mot") + ppl2(2,"hai") + ppl3(3,"ba");
            return;
        end
        """
        expect = "Undeclared Function: ppl0"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_function_5(self):
        """ Test "Undeclared Function" error: More Complex Undeclared Function """
        input = """
        var a, b, c:integer;

        function ppl1(asgmt2:integer;asgmt3: string): integer;
        begin
            return ppl2(2,"hai");
        end

        function ppl2(asgmt2:integer;asgmt3: string): integer;
        begin
            return ppl3(3,"ba");
        end

        function ppl3(asgmt2:integer;asgmt3: string): integer;
        var x:integer;
        begin
            x:= ppl0(0,"khong") + ppl1(1,"mot") + ppl2(2,"hai");
            return x;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl1(1,"mot") + ppl2(2,"hai") + ppl3(3,"ba");
            return;
        end
        """
        expect = "Undeclared Function: ppl0"
        self.assertTrue(TestChecker.test(input,expect,427))

# Undeclared Procedure: 5
    def test_undeclared_procedure_1(self):
        """ Test "Undeclared Procedure" error: Simple Undeclared Procedure """
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            ppl2018(true,10.11,10,"ppl deadline");
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2;  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            pplwinter18(ppl(1998,"Tran Truong Tuan Phat"),ppl(2018,"study ppl"),true);
            return;
        end
        """
        expect = "Undeclared Procedure: ppl2018"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_procedure_2(self):
        """ Test "Undeclared Procedure" error: Declare Function but use as Procedure """
        input = """
        var a, b, c:integer;

        function ppl2018(asgmt3: boolean):integer;
        begin
            return a;
        end

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            ppl2018(true);
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2;  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(1998,"hello ppl 2018");
            pplwinter18(10,11,true);
            return;
        end
        """
        expect = "Undeclared Procedure: ppl2018"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_procedure_3(self):
        """ Test "Undeclared Procedure" error: More Complex Undeclared Procedure """
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2; asgmt4();  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018");
            pplwinter18(10,11,true);
            return;
        end
        """
        expect = "Undeclared Procedure: asgmt4"
        self.assertTrue(TestChecker.test(input,expect,430))

#Type Mismatch In Statement: 23
# type mismatch if: 4
    def test_typemismatch_if_1(self):
        """ Test "Type Mismatch in Statement: If" test id not return BoolType in conditional expression in "if" statement """
        input = """
        var a: real;
            b: boolean;

        procedure main();
        begin
            if a then a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: If(Id(a),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],[])"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_typemismatch_if_2(self):
        """ Test "Type Mismatch in Statement: If" test IntType conditional expression in "if" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            if (1) then a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: If(IntLiteral(1),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],[])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_typemismatch_if_3(self):
        """ Test "Type Mismatch in Statement: If" test StringType conditional expression in "if" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            if "true" then a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: If(StringLiteral(true),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],[])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_typemismatch_if_4(self):
        """ Test "Type Mismatch in Statement: If" test FloatType conditional expression in "if" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            if 1.5 then a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: If(FloatLiteral(1.5),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],[])"
        self.assertTrue(TestChecker.test(input,expect,434))

# type mismatch for: 4
    def test_typemismatch_for_1(self):
        """ Test "Type Mismatch in Statement: For" test expression 1 in "for" statement """
        input = """
        var a,x: integer;
            b: boolean;

        procedure main();
        begin
            for x:=1.0 to 10 do a:=a+10;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(x)FloatLiteral(1.0),IntLiteral(10),True,[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(10)))])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_typemismatch_for_2(self):
        """ Test "Type Mismatch in Statement: For" test Identifier in "for" statement """
        input = """
        var a,x: integer;
            b: boolean;

        procedure main();
        begin
            for b:=1 to 10 do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(b)IntLiteral(1),IntLiteral(10),True,[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_typemismatch_for_3(self):
        """ Test "Type Mismatch in Statement: For" test expression 2 in "for" statement """
        input = """
        var a,x: integer;
            b: boolean;
            y:real;

        procedure main();
        begin
            for x:=1 to y do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(x)IntLiteral(1),Id(y),True,[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_typemismatch_for_4(self):
        """ Test "Type Mismatch in Statement: For" "for" statement nested in "for" statement """
        input = """
        var a,x: integer;
            b: boolean;
            y:real;

        procedure main();
        begin
            for x:=1 to 10 do
                for  a:=1 to y do y:=y+a+x;
            return;
        end
        """
        expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(1),Id(y),True,[AssignStmt(Id(y),BinaryOp(+,BinaryOp(+,Id(y),Id(a)),Id(x)))])"
        self.assertTrue(TestChecker.test(input,expect,438))

# type mismatch while: 4
    def test_typemismatch_while_1(self):
        """ Test "Type Mismatch in Statement: While" test id not return BoolType in conditional expression in "while" statement """
        input = """
        var a: real;
            b: boolean;

        procedure main();
        begin
            while a do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: While(Id(a),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_typemismatch_while_2(self):
        """ Test "Type Mismatch in Statement: While" test IntType conditional expression in "while" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            while (1) do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: While(IntLiteral(1),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_typemismatch_while_3(self):
        """ Test "Type Mismatch in Statement: While" test StringType conditional expression in "while" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            while "true" do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: While(StringLiteral(true),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_typemismatch_while_4(self):
        """ Test "Type Mismatch in Statement: While" test "While" statement nested in "while" statement """
        input = """
        var a: integer;
            b: boolean;

        procedure main();
        begin
            while b do while a do a:=a+1;
            return;
        end
        """
        expect = "Type Mismatch In Statement: While(Id(a),[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,442))

# type mismatch assign: 3
    def test_typemismatch_assign_1(self):
        """ Test "Type Mismatch in Statement: AssignStmt" test random mismatch assgin (Boolean is assgined to integer) """
        input = """
        var a: integer;
            b: boolean;
            c: real;

        procedure main();
        begin
            c:=a;
            a:=b;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_typemismatch_assign_2(self):
        """ Test "Type Mismatch in Statement: AssignStmt" test mismatch assgin (integeris assgined to array) """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;

        procedure main();
        begin
            c:=a;
            d:=a;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_typemismatch_assign_3(self):
        """ Test "Type Mismatch in Statement: AssignStmt" test coerce (pass case (int is assgined to real); error case(real is assigned to int)) """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;

        procedure main();
        begin
            c:=a:=d[1]:=d[2]+d[3];
            a:=c;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,445))

# type mismatch return: 4
    def test_typemismatch_return_1(self):
        """ Test "Type Mismatch in Statement: Return" test mismatch return type and coerce (integer is assgined to float) and else """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;
            e: string;

        function foo(): real;
        begin
            return 1;
        end

        function foo1(): integer;
        begin
            return 1.0;
        end

        procedure main();
        begin
            c := foo() +foo1();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_typemismatch_return_2(self):
        """ Test "Type Mismatch in Statement: Return" test random mismatch return type (string and integer) """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;
            e: string;

        function foo(): real;
        begin
            return "Finish PPL";
        end

        function foo1(): integer;
        begin
            return 1.0;
        end

        procedure main();
        begin
            c := foo() +foo1();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(Finish PPL)))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_typemismatch_return_3(self):
        """ Test "Type Mismatch in Statement: Return" test mismatch return type: array type mismatch index """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;
            e: string;

        function foo():  array[1 .. 4] of integer;
        begin
            return d;
        end

        function foo1(): array[2 .. 3] of integer;
        begin
            return d;
        end

        procedure main();
        var k: array[2 .. 3] of integer;
        begin
            d := foo();
            k := foo1();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_typemismatch_return_4(self):
        """ Test "Type Mismatch in Statement: Return" test mismatch return type: array type mismatch eleType """
        input = """
        var a: integer;
            b: boolean;
            c: real;
            d: array[1 .. 4] of integer;
            e: string;

        function foo():  array[1 .. 4] of integer;
        begin
            return d;
        end

        function foo1(): array[1 .. 4] of boolean;
        begin
            return d;
        end

        procedure main();
        var k: array[1 .. 4] of boolean;
        begin
            d := foo();
            k := foo1();
            return;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,449))

# type mismatch procedure call :3
    def test_typemismatch_procedurecall_1(self):
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2;  end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018");
            pplwinter18();
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(pplwinter18),[])"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_typemismatch_procedurecall_2(self):
        input = """
        var a, b, c:integer;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt1,asgmt2: integer;asgmt4:boolean);
        begin
            while asgmt4 do begin asgmt2 := asgmt1 + asgmt2; end
            return;
        end

        procedure main();
        var k:boolean;
            x:integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018");
            pplwinter18(10,11,true,"123");
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(pplwinter18),[IntLiteral(10),IntLiteral(11),BooleanLiteral(True),StringLiteral(123)])"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_typemismatch_procedurecall_3(self):
        input = """
        var a, b, c:boolean;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt: array[1 .. 4] of boolean);
        begin
            while a do begin b:=c:=true; end
            return;
        end

        procedure main();
        var k: array[1 .. 4] of boolean;
            n: array[1 .. 3] of boolean;
            x: integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018");
            pplwinter18(k);
            pplwinter18(n);
            return;
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(pplwinter18),[Id(n)])"
        self.assertTrue(TestChecker.test(input,expect,452))

#Type Mismatch In Expression: 10
    def test_typemismatch_expression_1(self):
        input = """
        var a, b, c:boolean;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt: array[1 .. 4] of boolean);
        begin
            while a do begin b:=c:=true; end
            return;
        end

        procedure main();
        var k: array[1 .. 4] of boolean;
            n: array[1 .. 3] of integer;
            x: integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018") + n[1];
            x:=x + n["hello asgmt 4"];
            pplwinter18(k);

            return;
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(n),StringLiteral(hello asgmt 4))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_typemismatch_expression_2(self):
        input = """
        var a, b, c:boolean;

        function ppl(asgmt2:integer;asgmt3: string): integer;
        begin
            return asgmt2;
        end

        procedure pplwinter18(asgmt: array[1 .. 4] of boolean);
        begin
            while a do begin b:=c:=true; end
            return;
        end

        procedure main();
        var k: array[1 .. 4] of boolean;
            n: array[1 .. 3] of integer;
            x: integer;
        begin
            x:=ppl(ppl(1998,"Tran Truong Tuan Phat"),"hello ppl 2018") + x[1];
            pplwinter18(k);

            return;
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_typemismatch_expression_3(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a:= 1 or true;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def  test_typemismatch_expression_4(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a:= 1 or else true;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(orelse,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_typemismatch_expression_5(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a:= 1 and 1.0;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,457))


    def test_typemismatch_expression_6(self):
        input = """
        procedure main();
        var a: integer;
        begin
            a:= 1 > true;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_typemismatch_expression_7(self):
        input = """
        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
        begin
            b := a;
            b := a * b;
            b := a / a;
            a := b/a;
            return;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,Id(b),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_typemismatch_expression_8(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            return 1;
        end

        function ppl2(asgmt:real):real;
        begin
            return 1.0;
        end

        function ppl3(asgmt:string):string;
        begin
            return "bye asgmt 3";
        end

        function ppl4(asgmt:array[1 .. 100] of integer):array[1 .. 100] of integer;
        begin
            return asgmt;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 100] of integer;
        begin
            a := ppl1(ppl1(3));
            b := ppl2(ppl1(2));
            d := ppl3(b);
            return;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(ppl3),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_typemismatch_expression_9(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            return 1;
        end

        function ppl2(asgmt:real):real;
        begin
            return 1.0;
        end

        function ppl3(asgmt:string):string;
        begin
            return "bye asgmt 3";
        end

        function ppl4(asgmt:array[1 .. 100] of integer):array[1 .. 100] of integer;
        begin
            return asgmt;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 100] of integer;
        begin
            a := ppl1(d);
            return;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(ppl1),[Id(d)])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_typemismatch_expression_10(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            return 1;
        end

        function ppl2(asgmt:real):real;
        begin
            return 1.0;
        end

        function ppl3(asgmt:string):string;
        begin
            return "bye asgmt 3";
        end

        function ppl4(asgmt:array[1 .. 4] of integer):array[1 .. 4] of integer;
        begin
            return asgmt;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl1(e);
            return;
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(ppl1),[Id(e)])"
        self.assertTrue(TestChecker.test(input,expect,462))

# Function not return: 5
    def test_NOT_RETURN_1(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl1(a);
            return;
        end
        """
        expect = "Function ppl1 Not Return"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_NOT_RETURN_2(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl2(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl1(a);
            return;
        end
        """
        expect = "Function ppl2 Not Return"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_NOT_RETURN_3(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl1(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl1(ppl2(10));
            return;
        end
        """
        expect = "Function ppl2 Not Return"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_NOT_RETURN_4(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl1(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
            return ppl2(asgmt);
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl3(pp11(10),ppl2(11));
            return;
        end
        """
        expect = "Function ppl3 Not Return"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_NOT_RETURN_5(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl1(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
            return asgmt1 + asgmt2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl3(pp11(10),ppl2(11));
            return;
        end
        """
        expect = "Function ppl2 Not Return"
        self.assertTrue(TestChecker.test(input,expect,467))

# Break/Continue: 6
    def test_continue_not_in_loop_1(self):
        input = """
        var a,b,c:integer;
        procedure foo();
        begin
            continue;
        end

        procedure main();
        begin
            foo();
            return;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_continue_not_in_loop_2(self):
        input = """
        var a,b,c:integer;
        procedure foo();
        begin
            continue;
        end

        procedure main();
        begin
            foo();
            continue;
            return;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_continue_not_in_loop_3(self):
        input = """
            var a,b,c:integer;
            procedure foo();
            var asgmt: boolean;
            begin
                while asgmt do
                    begin
                        continue;
                    end
                if asgmt then continue;
            end

            procedure main();
            begin
                foo();
                return;
            end
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_break_not_in_loop_1(self):
        input = """
        var a,b,c:integer;
        procedure foo();
        begin
            break;
        end

        procedure main();
        begin
            foo();
            return;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_break_not_in_loop_2(self):
        input = """
        var a,b,c:integer;
        procedure foo();
        begin
            return;
        end

        procedure main();
        begin
            foo();
            break;
            return;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,472))

    def testtest_break_not_in_loop_3(self):
        input = """
        var a,b,c:integer;
        procedure foo();
        var asgmt: boolean;
        begin
            while asgmt do
                begin
                    break;
                end
            if asgmt then break;
        end

        procedure main();
        begin
            foo();
            return;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,473))

#No Entry Point: 3
    def test_no_entry_1(self):
        """Test "No entry point" error: no procedure main"""
        input = """
        var a,b,c:integer;
            x: array[1 .. 3] of real;

        var y: StRiNg;
            z: BooLean;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_no_entry_2(self):
        """ Test "No entry point" error: procedure main with param """
        input = """
        var a,b,c:integer;

        procedure main(abc:string);
        var y:real;
        begin
            return;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_no_entry_3(self):
        """ Test "No entry point" error: function main """
        input = """
        var a,b,c:integer;

        function MaIn():real;
        var b:real;
        begin
            return b;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,476))

#Unreachable Statment: 5
    def test_unreachable_statement_1(self):
        input = """
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;

        function ppl(asgmt: integer): reaL;
        begin
            if c then return a + b; else return b;
            asgmt:=asgmt +1;
        end

        procedure main();
        var x: real;
        begin
            x:= ppl(a);
            return;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(asgmt),BinaryOp(+,Id(asgmt),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_unreachable_statement_2(self):
        input = """
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;

        procedure ppl(asgmt: integer);
        begin
            return;
            asgmt:=asgmt +1;
        end

        procedure main();
        var x: real;
        begin
            ppl(a);
            return;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(asgmt),BinaryOp(+,Id(asgmt),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,478))


    def test_unreachable_statement_3(self):
        input = """
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;

        procedure ppl(asgmt: integer);
        begin
            for a:=1 to 10 do
                begin
                    return;
                end

            while c do
                begin
                    return;
                end

            with x:integer; do
                begin
                    return;
                end

            a:=a+1;
            return;
            asgmt:=asgmt +1;
        end

        procedure main();
        var x: real;
        begin
            ppl(a);
            return;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(a),BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,479))


    def test_unreachable_statement_4(self):
        input = """
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;

        function ppl(asgmt: integer):real;
        begin
            if c then return b;
            a:=a + 1;
            if c then return a;
            b:=b + 1;
            return a+b;
            asgmt:=asgmt +1;
        end

        procedure main();
        var x: real;
        begin
            ppl(a);
            return;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(asgmt),BinaryOp(+,Id(asgmt),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,480))


    def test_unreachable_statement_5(self):
        input = """
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;

        procedure ppl(asgmt: integer);
        begin
            return;
            if c then return; else return;
            return;
            asgmt:=asgmt;
            return;
        end

        procedure main();
        var x: real;
        begin
            ppl(a);
            return;
        end
        """
        expect = "Unreachable statement: If(Id(c),[Return(None)],[Return(None)])"
        self.assertTrue(TestChecker.test(input,expect,481))

# Unreachable Function/Procedure: 5

    def test_unreachable_function_or_procedure_1(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl1(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
            return ppl2(asgmt);
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
            return asgmt1 + asgmt2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl1(10) + ppl2(11);
            return;
        end
        """
        expect = "Unreachable Function: ppl3"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachable_function_or_procedure_2(self):
        input = """
        function ppl1(asgmt:integer):integer;
        begin
            asgmt:=asgmt + 1;
            return ppl1(asgmt);
        end

        function ppl2(asgmt:integer):integer;
        begin
            asgmt:=asgmt*2;
            return ppl2(asgmt);
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
            return asgmt1 + asgmt2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl3(10,ppl2(11));
            return;
        end
        """
        expect = "Unreachable Function: ppl1"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachable_function_or_procedure_3(self):
        input = """
        procedure ppl1(asgmt:integer);
        begin
            asgmt:=asgmt + 1;
        end

        procedure ppl2(asgmt:integer);
        begin
            asgmt:=asgmt*2;
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
            return asgmt1 + asgmt2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl3(10,11);
            ppl1(a);
            return;
        end
        """
        expect = "Unreachable Procedure: ppl2"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachable_function_or_procedure_4(self):
        input = """
        procedure ppl1(asgmt:integer);
        begin
            asgmt:=asgmt + 1;
        end

        procedure ppl2(asgmt:integer);
        begin
            asgmt:=asgmt*2;
        end

        function ppl3(asgmt1,asgmt2:integer):integer;
        begin
            ppl2(asgmt1);
            asgmt1:=asgmt1*2;
            asgmt2:=asgmt2*2;
            return asgmt1 + asgmt2;
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            a := ppl3(10,11);
            return;
        end
        """
        expect = "Unreachable Procedure: ppl1"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_unreachable_function_or_procedure_5(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 3] of integer;

        function foo(): integer;
        var i:integer;
        begin
            return 1;
        end

        procedure goo();
        begin
        end

        procedure main();
        begin
            a:=foo();
        end
        """
        expect = "Unreachable Procedure: goo"
        self.assertTrue(TestChecker.test(input,expect,486))

# Test Random: 13
    def test_random_1(self):
        input = """
        procedure main();
        begin
            a := 1+2-3*4 mod 5 div 6;
            c := 1/2;
            d := (1 > 2 )and (1.2 > 2) and (1 < 2.2) and (1.2 < 2.2);
            d := d and then d or else d;
            d := d and d or d;
            d := (1>2) and (1>=2) and (1<2) and (1<=2) and (1<>2);
            e := e;
        end

        var a: integer;
        var b: string;
        var c: real;
        var d: boolean;
        var e: array[1 .. 3] of integer;
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(e),Id(e))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_random_2(self):
        input = """
        function foo(a: integer): integer;
        begin
            if d then
                return 1;
            else
                if d then
                        a:=1;
                    else
                        return 1;
            end

        procedure main();
        begin
        end

        var a: integer;
        var b: string;
        var c: real;
        var d: boolean;
        var e: array[1 .. 3] of integer;
        """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_random_3(self):
        input = """
        procedure foo();
        var a:integer;
        begin
            while true do
            begin
                if 1>2 then
                    break;
                else
                    return;
                a:=1;
            end
        end

        procedure main();
        var a:integer;
            b:real;
            c:boolean;
            d:string;
            e:array[1 .. 4] of integer;
        begin
            foo();
            return;
        end
        """
        expect = "Unreachable statement: AssignStmt(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_random_4(self):
        input = """
        procedure main();
        begin
            with x:real; do
                with x:integer; do
                    x:=1.0;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_random_5(self):
        input = """
        procedure main();
        begin
            with x:real; do
                with y:integer; do
                begin
                    x:=1.5;
                    y:=1;
                end

            x:=1;
        end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_random_6(self):
        input = """
        function foo(): real;
        begin
            with x:real; do
                with y:integer; do
                    with z: integer; do
                        return x+y+z;
                return 1;
        end

        procedure main();
        begin
        end
        """
        expect = "Unreachable statement: Return(Some(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_random_7(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 4] of integer;

        procedure main();
        begin
            a:=getInt();
            putInt(a);
            putIntLn(a);
            c:=getFloat();
            putFloat(c);
            putFloatLn(c);
            putBool(d);
            putBoolLn(d);
            putString(b);
            putStringLn(b);
            putLn();

            return 0;
        end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_random_8(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 4] of integer;

        procedure main();
        begin

        end

        procedure GEtInt();
        begin
        end
        """
        expect = "Redeclared Procedure: GEtInt"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_random_9(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 4] of integer;

        procedure main();
        begin
            println("hello");
            println(d);
        end

        procedure println(s:string);
        begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(println),[Id(d)])"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_random_10(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 3] of integer;

        procedure foo();
        begin
            return;
        end

        procedure goo();
        var foo: integer;
        begin
            foo();
        end

        procedure main();
        begin
            goo();
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_random_11(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 3] of integer;

        procedure foo();
        begin
            return;
        end

        procedure goo(foo: integer);
        begin
            foo();
        end

        procedure main();
        begin
            goo();
        end
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_random_12(self):
        input = """
        procedure main();
        begin
            for a := 1 to 2 do
                with a: integer; do
                begin
                    with a: integer; do
                        break;
                    break;
                end

        end

        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 3] of integer;
        """
        expect = "Unreachable statement: Break"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_random_13(self):
        input = """
        var a: integer;
            b: string;
            c: real;
            d: boolean;
            e: array[1 .. 3] of integer;

        procedure main();
        begin
        end

        var main:integer;
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,499))
