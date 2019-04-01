# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDecl.
    def visitVarDecl(self, ctx:MPParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listDecls.
    def visitListDecls(self, ctx:MPParser.ListDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDecl.
    def visitFuncDecl(self, ctx:MPParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listParams.
    def visitListParams(self, ctx:MPParser.ListParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#params.
    def visitParams(self, ctx:MPParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proDecl.
    def visitProDecl(self, ctx:MPParser.ProDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#types.
    def visitTypes(self, ctx:MPParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primtype.
    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundtype.
    def visitCompoundtype(self, ctx:MPParser.CompoundtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrtype.
    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lower.
    def visitLower(self, ctx:MPParser.LowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#upper.
    def visitUpper(self, ctx:MPParser.UpperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp6.
    def visitExp6(self, ctx:MPParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrelement.
    def visitArrelement(self, ctx:MPParser.ArrelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstmt.
    def visitAssignstmt(self, ctx:MPParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstmt.
    def visitIfstmt(self, ctx:MPParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestmt.
    def visitWhilestmt(self, ctx:MPParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstmt.
    def visitForstmt(self, ctx:MPParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstmt.
    def visitBreakstmt(self, ctx:MPParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestmt.
    def visitContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstmt.
    def visitReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstmt.
    def visitCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstmt.
    def visitWithstmt(self, ctx:MPParser.WithstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstmt.
    def visitCallstmt(self, ctx:MPParser.CallstmtContext):
        return self.visitChildren(ctx)



del MPParser