# MSSV:1612541
# Ho va ten: Tran Truong Tuan Phat
# Lop: MT16TN

from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(list(reduce(lambda x,y: x+y,[self.visit(t) for t in ctx.declaration()],[])))


    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        '''declaration: varDecl  | funcDecl | proDecl;'''
        return self.visit(ctx.getChild(0))


    def visitVarDecl(self, ctx:MPParser.VarDeclContext):
        '''varDecl: VAR listDecls+;'''
        return list(reduce(lambda x,y: x+y,[self.visit(t) for t in ctx.listDecls()],[]))


    def visitListDecls(self, ctx:MPParser.ListDeclsContext):
        '''listDecls: IDENTIFIER (COMMA IDENTIFIER)* COLON types SEMI;'''
        '''a,b,c:INTEGER; --> [VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]'''
        return [VarDecl(Id(x.getText()),self.visit(ctx.types())) for x in ctx.IDENTIFIER()]


    def visitFuncDecl(self, ctx:MPParser.FuncDeclContext):
        '''  FUNCTION IDENTIFIER LB listParams? RB COLON types SEMI varDecl? compoundstmt'''
        local, para = self.visit(ctx.varDecl()) if ctx.varDecl() else [], self.visit(ctx.listParams()) if  ctx.listParams() else []
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()),para,local,self.visit(ctx.compoundstmt()),self.visit(ctx.types()))]


    def visitListParams(self, ctx:MPParser.ListParamsContext):
        '''listParams: params (SEMI params)*;'''
        return list(reduce(lambda x,y:x+y,[self.visit(t) for t in ctx.params()],[]))


    def visitParams(self, ctx:MPParser.ParamsContext):
        '''params: IDENTIFIER (COMMA IDENTIFIER)* COLON types;'''
        return [VarDecl(Id(x.getText()),self.visit(ctx.types())) for x in ctx.IDENTIFIER()]


    def visitProDecl(self, ctx:MPParser.ProDeclContext):
        '''proDecl: PROCEDURE IDENTIFIER LB listParams RB SEMI varDecl? compoundstmt;'''
        local, para = self.visit(ctx.varDecl()) if ctx.varDecl() else [], self.visit(ctx.listParams()) if  ctx.listParams() else []
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()),para,local,self.visit(ctx.compoundstmt()))]

    def visitLiteral(self, ctx:MPParser.LiteralContext):
        '''literal: INTLIT | REALIT | BOOLIT | STRLIT;'''
        if ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.REALIT(): return FloatLiteral(float(ctx.REALIT().getText()))
        if ctx.BOOLIT(): return BooleanLiteral(False) if ctx.BOOLIT().getText().lower()=="false" else BooleanLiteral(True)
        if ctx.STRLIT(): return StringLiteral(str(ctx.STRLIT().getText()))


    def visitTypes(self, ctx:MPParser.TypesContext):
        '''types: primtype | compoundtype'''
        return self.visit(ctx.primtype()) if ctx.primtype() else self.visit(ctx.compoundtype())


    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        '''primtype: BOOLEAN | INTEGER | REAL | STRING;'''
        if ctx.BOOLEAN(): return BoolType()
        if ctx.INTEGER(): return IntType()
        if ctx.REAL(): return FloatType()
        return StringType()


    def visitCompoundtype(self, ctx:MPParser.CompoundtypeContext):
        '''compoundtype: arrtype;'''
        return self.visit(ctx.getChild(0))


    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        '''arrtype: ARRAY LSB lower DDOT upper RSB OF primtype;'''
        return ArrayType(self.visit(ctx.lower()),self.visit(ctx.upper()),self.visit(ctx.primtype()))


    def visitLower(self, ctx:MPParser.LowerContext):
        '''lower: SUB? INTLIT;'''
        return int(ctx.INTLIT().getText())*(-1) if ctx.SUB() else int(ctx.INTLIT().getText())


    def visitUpper(self, ctx:MPParser.UpperContext):
        '''upper: SUB? INTLIT;'''
        return int(ctx.INTLIT().getText())*(-1) if ctx.SUB() else int(ctx.INTLIT().getText())


    def visitOperand(self, ctx:MPParser.OperandContext):
        '''operand: literal | IDENTIFIER | funcall;'''
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.getChild(0))


    def visitExp(self, ctx:MPParser.ExpContext):
        '''exp: exp AND THEN exp1 | exp OR ELSE exp1 | exp1;'''
        if ctx.AND() and ctx.THEN(): return BinaryOp("andthen",self.visit(ctx.exp()),self.visit(ctx.exp1()))
        if ctx.OR() and ctx.ELSE(): return BinaryOp("orelse",self.visit(ctx.exp()),self.visit(ctx.exp1()))
        if ctx.exp1(): return self.visit(ctx.exp1())


    def visitExp1(self, ctx:MPParser.Exp1Context):
        '''exp1: exp2 EQUAL exp2 | exp2 NOTEQUAL exp2 | exp2 LESSTHAN exp2 | exp2 GREATERTHAN exp2 | exp2 LESSEQUAL exp2 | exp2 GREATEREQUAL exp2 | exp2;'''
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1))) if ctx.getChildCount()==3 else self.visit(ctx.exp2(0))


    def visitExp2(self, ctx:MPParser.Exp2Context):
        '''exp2: exp2 ADD exp3 | exp2 SUB exp3 | exp2 OR exp3 | exp3;'''
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.getChildCount()==3 else self.visit(ctx.exp3())


    def visitExp3(self, ctx:MPParser.Exp3Context):
        '''dxp3: exp3 DIV_F exp4 | exp3 MUL exp4 | exp3 DIV exp4 | exp3 MOD exp4 | exp3 AND exp4 | exp4;'''
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4())) if ctx.getChildCount()==3 else self.visit(ctx.exp4())


    def visitExp4(self, ctx:MPParser.Exp4Context):
        '''exp4: SUB exp4 | NOT exp4 | exp5;'''
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp4())) if ctx.getChildCount()==2 else self.visit(ctx.exp5())


    def visitExp5(self, ctx:MPParser.Exp5Context):
        '''exp5: exp5 LSB exp RSB | exp6;'''
        return ArrayCell(self.visit(ctx.exp5()),self.visit(ctx.exp())) if ctx.getChildCount()==4 else self.visit(ctx.exp6())


    def visitExp6(self, ctx:MPParser.Exp6Context):
        '''exp6: LB exp RB | operand;'''
        return self.visit(ctx.exp()) if ctx.getChildCount()==3 else self.visit(ctx.operand())


    def visitArrelement(self, ctx:MPParser.ArrelementContext):
        '''arrelement: exp5 LSB exp RSB;'''
        return ArrayCell(self.visit(ctx.exp5()),self.visit(ctx.exp()))


    def visitFuncall(self, ctx:MPParser.FuncallContext):
        '''funcall: IDENTIFIER LB (exp (COMMA exp)*)? RB;'''
        return CallExpr(Id(ctx.IDENTIFIER().getText()),[self.visit(x) for x in ctx.exp()])


    def visitStmt(self, ctx:MPParser.StmtContext):
        '''stmt: assignstmt | ifstmt | whilestmt | forstmt | breakstmt | continuestmt | returnstmt | compoundstmt | withstmt | callstmt;'''
        return self.visit(ctx.getChild(0))


    def visitAssignstmt(self, ctx:MPParser.AssignstmtContext):
        '''assignstmt: lhs (ASSIGN lhs)* ASSIGN exp SEMI;'''
        d=[self.visit(x) for x in ctx.lhs()][::-1]
        e=[self.visit(ctx.exp())] + d[:-1]
        return list(map(lambda x:Assign(x[0],x[1]),zip(d,e)))


    def visitLhs(self, ctx:MPParser.LhsContext):
        '''lhs: (IDENTIFIER | arrelement);'''
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.arrelement())


    def visitIfstmt(self, ctx:MPParser.IfstmtContext):
        '''ifstmt: IF exp THEN stmt (ELSE stmt)?;'''
        return [If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)))] if ctx.ELSE() else [If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),[])]


    def visitWhilestmt(self, ctx:MPParser.WhilestmtContext):
        '''whilestmt: WHILE exp DO stmt;'''
        return [While(self.visit(ctx.exp()),self.visit(ctx.stmt()))]


    def visitForstmt(self, ctx:MPParser.ForstmtContext):
        '''forstmt: FOR IDENTIFIER ASSIGN exp (TO | DOWNTO) exp DO stmt;'''
        return [For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),True,self.visit(ctx.stmt()))] if ctx.TO() else [For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),False,self.visit(ctx.stmt()))]


    def visitBreakstmt(self, ctx:MPParser.BreakstmtContext):
        '''breakstmt: BREAK SEMI;'''
        return [Break()]


    def visitContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        '''continuestmt: CONTINUE SEMI;'''
        return [Continue()]


    def visitReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        '''returnstmt: RETURN exp? SEMI;'''
        return [Return(self.visit(ctx.exp()))] if ctx.exp() else [Return()]


    def visitCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        '''compoundstmt: BEGIN stmt* END;'''
        return list(reduce(lambda x,y:x+y,[self.visit(t) for t in ctx.stmt()],[]))


    def visitWithstmt(self, ctx:MPParser.WithstmtContext):
        '''withstmt: WITH listDecls+ DO stmt;'''
        return [With(list(reduce(lambda x,y: x+y,[self.visit(x) for x in ctx.listDecls()],[])),self.visit(ctx.stmt()))]


    def visitCallstmt(self, ctx:MPParser.CallstmtContext):
        '''callstmt: IDENTIFIER LB (exp (COMMA exp)*)? RB SEMI;'''
        return [CallStmt(Id(ctx.IDENTIFIER().getText()),[self.visit(x) for x in ctx.exp()])]
