# MSSV:1612541
# Ho va ten: Tran Truong Tuan Phat
# Lop: MT16TN

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType( ' + str([str(x) for x in self.partype ]) + "," + str(self.rettype)+ ')'

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol( ' + str(self.name) + "," + str(self.mtype)+ "," + str(self.value)+ ')'

def checkValidAssign(left,right):
    if (type(left), type(right)) in [(VoidType,VoidType),(IntType,FloatType)]:
        return True

    elif not type(left) is ArrayType and not type(right) is ArrayType and type(left)==type(right):
        return True

    elif type(left) is ArrayType and type(right) is ArrayType:
        if type(right.eleType) is bool:
            return True
        else:
            return type(left.eleType) is type(right.eleType) and left.lower==right.lower and left.upper==right.upper
    else:
        return False

def checkTypeMismatch(ast,at,lst,isStatement,isUnary=False):
    if isUnary==False:
        if len(lst)!=len(at) or True in [not checkValidAssign(a,b) for a,b in zip(at,lst)]:
            raise TypeMismatchInStatement(ast) if isStatement else TypeMismatchInExpression(ast)
    else:
        if len(lst)!=len(at) or True in [not type(a) in b for a,b in zip(at,lst)]:
            raise TypeMismatchInStatement(ast) if isStatement else TypeMismatchInExpression(ast)


class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType())),
                   Symbol("putInt", MType([IntType()], VoidType())),
                   Symbol("getFloat", MType([], FloatType())),
                   Symbol("putFloat", MType([FloatType()], VoidType())),
                   Symbol("putFloatLn", MType([FloatType()], VoidType())),
                   Symbol("putBool", MType([BoolType()], VoidType())),
                   Symbol("putBoolLn", MType([BoolType()], VoidType())),
                   Symbol("putString", MType([StringType()], VoidType())),
                   Symbol("putStringLn", MType([StringType()], VoidType())),
                   Symbol("putLn", MType([], VoidType()))]

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)


    def checkUndeclared(self,name,c,kind):
        res=self.lookup(name.lower(),c,lambda x:x.name.lower())
        if type(kind) is Identifier:
            if res is None or type(res.mtype) is MType:
                raise Undeclared(Identifier(),name)

        elif type(kind) is Procedure:
            if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
                raise Undeclared(kind,name)

        elif type(kind) is Function:
            if res is None or not type(res.mtype) is MType or type(res.mtype.rettype) is VoidType:
                raise Undeclared(Function(),name)
        return res


    def traverseList(self,lstmt,c):
        for i in range(0,len(lstmt)):
            _refevi=c.copy()
            _refevi[2]=c[2]
            _stmt=self.visit(lstmt[i],_refevi)
            if not _stmt:
                if i<len(lstmt)-1:
                    raise UnreachableStatement(lstmt[i+1])
                return False
        return True


    def visitProgram(self,ast, c):
        c=c.copy()
        lsdecl=[self.visit(x,[c,True]) for x in ast.decl]
        isMain=False
        lst=zip(ast.decl,lsdecl)
        funclist=[]
        [self.visit(a,[c,b,funclist]) if not b is None else None for a,b in lst]
        funcdecl=[x for x in c if type(x.mtype) is MType and not x in self.global_envi]
        for x in funcdecl:
            if x.name.lower()!="main" and not x.name.lower() in funclist:
                raise Unreachable(Procedure() if type(x.mtype.rettype) is VoidType else Function(),x.name)
            elif x.name.lower()=="main" and type(x.mtype.rettype) is VoidType and x.mtype.partype==[]:
                isMain=True
        if not isMain:
            raise NoEntryPoint()
        return None


    def visitFuncDecl(self,ast, c):
        if c[1]==True:
            if self.lookup(ast.name.name.lower(),c[0],lambda x:x.name.lower()) is not None:
                if type(ast.returnType) is VoidType:
                    raise Redeclared(Procedure(),ast.name.name)
                else: raise Redeclared(Function(),ast.name.name)

            _local=[]
            _param=[]
            for x in ast.param:
                if self.lookup(x.variable.name.lower(),_local,lambda x:x.name.lower()) is not None:
                    raise Redeclared(Parameter(),x.variable.name)

                _local.append(Symbol(x.variable.name,x.varType))
                _param.append(x.varType)
            c[0].append(Symbol(ast.name.name, MType(_param, ast.returnType)))
            return _local
        [self.visit(x,[c[1]]) for x in ast.local]
        c.append((ast.name.name,ast.returnType))
        c.append(False)
        isNotReturn=self.traverseList(ast.body,c)
        if isNotReturn and not type(ast.returnType) is VoidType:
            raise FunctionNotReturn(ast.name.name)


    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name.lower(),c[0],lambda x:x.name.lower()) is not None:
            raise Redeclared(Variable(),ast.variable.name)
        c[0].append(Symbol(ast.variable.name, ast.varType))
        return None


    def visitBinaryOp(self,ast,c):
        _left=self.visit(ast.left,c)
        _right=self.visit(ast.right,c)
        at=[_left,_right]
        if ast.op in ['+','*','-','/']:
            checkTypeMismatch(ast,at,[[IntType,FloatType],[IntType,FloatType]],False,True)
            return FloatType() if ast.op=='/' else (FloatType() if FloatType in (type(_left),type(_right)) else IntType())
        elif ast.op.lower() in ['div','mod']:
            checkTypeMismatch(ast,at,[IntType(),IntType()],False)
            return IntType()
        if ast.op in ['<','<=','>','>=','<>','=']:
            checkTypeMismatch(ast,at,[[IntType,FloatType],[IntType,FloatType]],False,True)
            return BoolType()
        else:
            checkTypeMismatch(ast,at,[BoolType(),BoolType()],False)
            return BoolType()


    def visitUnaryOp(self, ast, c):
        _body=self.visit(ast.body,c)
        if ast.op=='-':
            checkTypeMismatch(ast,[_body],[[FloatType,IntType]],False,True)
        else:
            checkTypeMismatch(ast,[_body],[BoolType()],False)
        return _body


    def visitCallExpr(self, ast, c):
        at=[self.visit(x,c) for x in ast.param]
        res=self.checkUndeclared(ast.method.name,c[0],Function())
        checkTypeMismatch(ast,at,res.mtype.partype,False)
        if c[2][0]!=ast.method.name:
            c[1].append(ast.method.name.lower())
        return res.mtype.rettype


    def visitId(self,ast,c):
        return self.checkUndeclared(ast.name,c[0],Identifier()).mtype


    def visitArrayCell(self, ast, c):
        arr=self.visit(ast.arr,c)
        checkTypeMismatch(ast,[arr,self.visit(ast.idx,c)],[ArrayType(0,0,True),IntType()],False)
        return arr.eleType


    def visitAssign(self, ast, c):
        lhs=self.visit(ast.lhs,[c[1]+c[0],c[2],c[3]])
        exp=self.visit(ast.exp,[c[1]+c[0],c[2],c[3]])
        at=[[IntType,BoolType,FloatType]]
        checkTypeMismatch(ast,[lhs],at,True,True)
        checkTypeMismatch(ast,[exp],[lhs],True)
        return True


    def visitWith(self, ast, c):
        c[0]=c[1]+c[0]
        c[1]=[]
        for x in ast.decl:
            if self.lookup(x.variable.name.lower(),c[1],lambda x:x.name.lower()) is not None:
                raise Redeclared(Variable(),x.variable.name)
            c[1].append(Symbol(x.variable.name,x.varType))
        return self.traverseList(ast.stmt,c)


    def visitIf(self,ast,c):
        _env=c.copy()
        checkTypeMismatch(ast,[self.visit(ast.expr,[c[1]+c[0],c[2],c[3]])],[BoolType()],True)
        a=self.traverseList(ast.thenStmt,c)
        b=self.traverseList(ast.elseStmt,c)
        return a or b


    def visitFor(self, ast, c):
        at=[self.visit(ast.id,[c[1]+c[0],c[2],c[3]]),self.visit(ast.expr1,[c[1]+c[0],c[2],c[3]]),self.visit(ast.expr2,[c[1]+c[0],c[2],c[3]])]
        checkTypeMismatch(ast,at,[IntType(),IntType(),IntType()],True)
        c[4]=True
        self.traverseList(ast.loop,c)
        return True


    def visitWhile(self, ast, c):
        checkTypeMismatch(ast,[self.visit(ast.exp,[c[1]+c[0],c[2],c[3]])],[BoolType()],True)
        c[4]=True
        self.traverseList(ast.sl,c)
        return True


    def visitCallStmt(self,ast,c):
        res=self.checkUndeclared(ast.method.name,c[1]+c[0],Procedure())
        at1=[self.visit(x,[c[1]+c[0],c[2],c[3]]) for x in ast.param]
        at2=res.mtype.partype
        checkTypeMismatch(ast,at1,at2,True)
        if c[3][0]!=ast.method.name:
            c[2].append(ast.method.name.lower())
        return True


    def visitBreak(self, ast, c):
        if c[4]:
            return False
        else:
            raise BreakNotInLoop()


    def visitContinue(self, ast, c):
        if c[4]:
            return False
        else:
            raise ContinueNotInLoop()


    def visitReturn(self, ast, c):
        if ast.expr:
            exp=self.visit(ast.expr,[c[1]+c[0],c[2],c[3]])
            checkTypeMismatch(ast,[exp],[c[3][1]],True)
        return False


    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()
