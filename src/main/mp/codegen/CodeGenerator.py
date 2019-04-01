'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''

# MSSV:1612541
# Ho va ten: Tran Truong Tuan Phat
# Lop: MT16TN

from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getBool", MType(list(), BoolType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("getString", MType(list(), StringType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        glenv = [self.visit(x,0) for x in ast.decl]
        e = SubBody(None, self.env + glenv)
        for x in ast.decl:
            self.visit(x, e)

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl(Id("<clinit>"), list(), list(), list(),VoidType()), e.sym, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c


    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        ls_param = [self.visit(x,1) for x in consdecl.param]
        intype = [ArrayPointerType(StringType())] if isMain else ls_param
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # glenv = o
        glenv = [] if o is None else o
        if consdecl.name.name == "<clinit>":
            for x in glenv:
                if type(x.mtype) is ArrayType:
                    self.emit.printout(self.visit(IntLiteral(int(str(x.mtype.upper)) - int(str(x.mtype.lower))+1),SubBody(frame, glenv))[0])
                    self.emit.printout(self.emit.emitArray(x.mtype,x.value,frame,x.name))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()
            return

        lcenv = []
        e = SubBody(frame, lcenv)
        penv = []
        p = SubBody(frame, penv)
        for x in consdecl.param :
            p = self.visit(x, p)
        for x in consdecl.local:
            e = self.visit(x, e)
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for x in e.sym:
            if type(x.mtype) is ArrayType:
                self.emit.printout(self.visit(IntLiteral(int(str(x.mtype.upper)) - int(str(x.mtype.lower))+1),e)[0])
                self.emit.printout(self.emit.emitArray(x.mtype,x.value,frame,x.name))

        e.sym = e.sym +p.sym+ glenv
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, e), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


    def visitVarDecl(self, ast, o):
        # def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String
        if o == 0:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name,ast.varType,False,None))
            return Symbol(ast.variable.name, ast.varType, CName(self.className))
        if o == 1:
            return ast.varType
        subctxt = o
        frame = o.frame
        env = o.sym
        if frame is None:

            return SubBody(None,[Symbol(ast.variable.name, ast.varType, CName(self.className))]+subctxt.sym)
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx,ast.variable.name, ast.varType,frame.getStartLabel(),frame.getEndLabel(),frame))
            return SubBody(frame,[Symbol(ast.variable.name, ast.varType, Index(idx))]+env )


    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        if o ==0:
            ls_param = [self.visit(x,1) for x in ast.param]
            return Symbol(ast.name.name, MType(ls_param, ast.returnType), CName(self.className))

        subctxt = o
        frame = Frame(ast.name, ast.returnType)

        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None,[Symbol(ast.name.name, MType(list(), ast.returnType), CName(self.className))]+subctxt.sym)


    def visitIf(self, ast, o):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        exp,exptype = self.visit(ast.expr, Access(frame, nenv, False, True))
        label1 = frame.getNewLabel()
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(label1,frame))
        list(map(lambda x: self.visit(x, o), ast.thenStmt))

        if ast.elseStmt != []:
            label2 = frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(label2,frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        if ast.elseStmt != []:
            list(map(lambda x: self.visit(x, o), ast.elseStmt))
            self.emit.printout(self.emit.emitLABEL(label2, frame))


    def visitWhile(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        exp,exptype = self.visit(ast.exp, Access(frame, nenv, False, True))
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(label2,frame))
        list(map(lambda x: self.visit(x, o), ast.sl))
        self.emit.printout(self.emit.emitGOTO(label1,frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()


    def visitFor(self, ast, o):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        op = '<=' if ast.up else '>='
        op2 = '+' if ast.up else '-'
        op3 = '-' if ast.up else '+'
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        self.visit(Assign(ast.id,ast.expr1),o)
        self.visit(Assign(ast.id,BinaryOp(op3,ast.id,IntLiteral(1))),o)
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.visit(Assign(ast.id,BinaryOp(op2,ast.id,IntLiteral(1))),o)
        self.emit.printout(self.visit(BinaryOp(op,ast.id,ast.expr2),Access(frame, nenv, False, True))[0])

        self.emit.printout(self.emit.emitIFFALSE(label2,frame))
        list(map(lambda x: self.visit(x, o), ast.loop))
        self.emit.printout(self.emit.emitGOTO(label1,frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()


    def visitWith(self, ast, o):
        ctxt = o
        frame = o.frame
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        env = o.sym
        frame.enterScope(False)
        e = SubBody(frame, [])
        for x in ast.decl :
            e = self.visit(x, e)
        env =e.sym+ env
        for y in e.sym:
            if type(y.mtype) is ArrayType:
                self.emit.printout(self.visit(IntLiteral(int(str(y.mtype.upper)) - int(str(y.mtype.lower))+1),SubBody(frame, env))[0])
                self.emit.printout(self.emit.emitArray(y.mtype,y.value,frame,y.name))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, SubBody(frame, env)), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()


    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), reversed(nenv), lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        ctype2 = MType([],ClassType('java/lang/Object'))
        in_ = ("", list())
        ls = zip(ast.param,ctype.partype)
        for x,y in ls:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is ArrayType:
                bonus = self.emit.emitINVOKEVIRTUAL(self.emit.getJVMType(typ1)+'/clone',ctype2,frame)+'\t'+ 'checkcast '+self.emit.getJVMType(typ1) + '\n'
                str1 = str1 + bonus

            if type(typ1) is IntType and type(y) is FloatType:
                bonus2 = self.emit.emitI2F(frame)
                str1 = str1 + bonus2
            if type(typ1) is ArrayPointerType and type(typ1.eleType) is IntType and type(y) is FloatType:
                bonus2 = self.emit.emitI2F(frame)
                str1 = str1 + bonus2
            in_ = (in_[0] + str1, in_[1] + [typ1])
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))


    def visitBinaryOp(self, ast, o):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        # #isFirst: Boolean
        #  emitREOP emitRELOP
        ctxt = o
        frame = ctxt.frame
        leftcode,lefttype = self.visit(ast.left,o)
        rightcode,righttype = self.visit(ast.right,o)
        leftcode2 = leftcode + self.emit.emitI2F(frame) if (type(lefttype) is IntType or ( type(lefttype) is ArrayPointerType and type(lefttype.eleType) is IntType ) )else leftcode
        rightcode2 = rightcode + self.emit.emitI2F(frame)if (type(righttype) is IntType or ( type(righttype) is ArrayPointerType and type(righttype.eleType) is IntType ) )else rightcode
        typ1 = lefttype.eleType if type(lefttype) is ArrayPointerType else lefttype
        typ2 = righttype.eleType if type(righttype) is ArrayPointerType else righttype
        if type(typ1) == type(typ2):
            if ast.op in ['+','-']:
                return leftcode+rightcode + self.emit.emitADDOP(ast.op,typ1,frame),lefttype
            elif ast.op is '*':
                return  leftcode+rightcode + self.emit.emitMULOP(ast.op,typ1,frame),lefttype
            elif ast.op is '/':
                return  leftcode2 + rightcode2 + self.emit.emitMULOP(ast.op,FloatType(),frame),FloatType()
            elif ast.op.lower() == 'div':
                return leftcode+rightcode + self.emit.emitDIV(frame),typ1
            elif ast.op.lower() == 'mod':
                return leftcode+rightcode + self.emit.emitMOD(frame),typ1
            elif ast.op == 'and':
                return leftcode+rightcode + self.emit.emitANDOP(frame),BoolType()
            elif ast.op == 'or':
                return leftcode+rightcode + self.emit.emitOROP(frame),BoolType()
            elif ast.op in ['<','>','<=','>=','=','<>']:
                return leftcode+rightcode + self.emit.emitREOP(ast.op,typ1,frame),BoolType()
            elif ast.op.lower() == 'andthen':
                label1 = frame.getNewLabel()
                code = leftcode + self.emit.emitDUP(frame)
                code = code + self.emit.emitIFFALSE(label1,frame)
                code = code +rightcode + self.emit.emitANDOP(frame)
                code = code + self.emit.emitLABEL(label1, frame)
                return code,BoolType()
            elif ast.op.lower() == 'orelse':
                label1 = frame.getNewLabel()
                code = leftcode + self.emit.emitDUP(frame)
                code = code + self.emit.emitIFTRUE(label1,frame)
                code = code +rightcode + self.emit.emitOROP(frame)
                code = code + self.emit.emitLABEL(label1, frame)
                return code,BoolType()
        else:
            if ast.op in ['+','-']:
                return leftcode2+rightcode2 + self.emit.emitADDOP(ast.op,FloatType(),frame),FloatType()
            elif ast.op in ['*','/']:
                return leftcode2+rightcode2 + self.emit.emitMULOP(ast.op,FloatType(),frame),FloatType()
            elif ast.op.lower() in ['<','>','<=','>=','=','<>']:
                return leftcode2+rightcode2 + self.emit.emitREOP(ast.op,FloatType(),frame),BoolType()


    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), reversed(nenv), lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        ctype2 = MType([],ClassType('java/lang/Object'))
        in_ = ("", list())
        ls = zip(ast.param,ctype.partype)
        for x,y in ls:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is ArrayType:
                bonus = self.emit.emitINVOKEVIRTUAL(self.emit.getJVMType(typ1)+'/clone',ctype2,frame)+'\t'+ 'checkcast '+self.emit.getJVMType(typ1) + '\n'
                str1 = str1 + bonus
            if type(typ1) is IntType and type(y) is FloatType:
                bonus2 = self.emit.emitI2F(frame)
                str1 = str1 + bonus2
            if type(typ1) is ArrayPointerType and type(typ1.eleType) is IntType and type(y) is FloatType:
                bonus2 = self.emit.emitI2F(frame)
                str1 = str1 + bonus2
            in_ = (in_[0] + str1, in_[1]+ [typ1])
        return in_[0]+ self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame),ctype.rettype


    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        bodyCode,bodyType = self.visit(ast.body,o)
        _type = bodyType.eleType if type(bodyType) is ArrayPointerType else bodyType
        if ast.op.lower() == 'not':
            return bodyCode + self.emit.emitNOT(StringType(),frame),BoolType()
        else:
            return bodyCode + self.emit.emitNEGOP(_type,frame),_type


    def visitAssign(self, ast, o):
        frame = o.frame
        frame.push()
        frame.push()
        expCode,expType=self.visit(ast.exp,Access(frame,o.sym,False,True))
        lhsCode,lhsType=self.visit(ast.lhs,Access(frame,o.sym,True,True))
        if isinstance(lhsType,FloatType) and isinstance(expType,IntType):
            expCode=expCode+self.emit.emitI2F(frame)
        if isinstance(ast.lhs,ArrayCell):
            self.emit.printout(lhsCode+expCode+self.visit(ast.lhs,Access(frame,o.sym,True,False)))
        else:
            self.emit.printout(expCode+lhsCode)
        frame.pop()
        frame.pop()


    def visitId(self, ast, o):
        frame = o.frame
        sym=self.lookup(ast.name.lower(),o.sym,lambda x:x.name.lower())
        _type=sym.mtype if not isinstance(sym.mtype,ArrayType) else ArrayPointerType(sym.mtype.eleType)
        if not isinstance(sym.value,Index):
            if isinstance(o,Access) and o.isLeft is True:
                return self.emit.emitPUTSTATIC(sym.value.value +"."+sym.name,_type,frame),sym.mtype
            else:
                return self.emit.emitGETSTATIC(sym.value.value +"."+sym.name,_type,frame),sym.mtype
        else:
            if isinstance(o,Access) and o.isLeft is True:
                return self.emit.emitWRITEVAR(sym.name,_type,sym.value.value,frame),sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name,_type,sym.value.value,frame),sym.mtype


    def visitArrayCell(self, ast, o):
        #arr:Expr
        #idx:Expr

        frame = o.frame
        arr,arrtype=self.visit(ast.arr,Access(frame,o.sym,False,True))
        idx,idxtype=self.visit(ast.idx,Access(frame,o.sym,False,True))
        idx=idx+self.visit(IntLiteral(arrtype.lower),o)[0]+ self.emit.emitADDOP("-",IntType(),frame) if arrtype.lower>=0 else idx+self.visit(IntLiteral(-arrtype.lower),o)[0]+ self.emit.emitADDOP("+",IntType(),frame)
        if isinstance(o,Access) and o.isLeft is True and o.isFirst is True:
            return arr+idx,arrtype.eleType
        elif isinstance(o,Access)and o.isLeft is True and o.isFirst is False:
            return self.emit.emitASTORE(arrtype.eleType,frame)
        else:
            return arr+idx+self.emit.emitALOAD(arrtype.eleType,frame),arrtype.eleType


    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(),frame))

    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))


    def visitReturn(self, ast, o):
        ctxt = o
        frame = o.frame
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        else:
            expcode,exptype = self.visit(ast.expr,Access(frame, o.sym, False, True))

            if type(frame.returnType) is FloatType and type(exptype) is IntType:
                self.emit.printout(expcode+self.emit.emitI2F(frame)+self.emit.emitRETURN(FloatType(),frame))
            else:
                self.emit.printout(expcode+self.emit.emitRETURN(exptype,frame))


    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value,StringType() ,frame), StringType()


    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()


    def visitIntLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()


    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
