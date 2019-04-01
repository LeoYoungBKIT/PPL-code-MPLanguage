.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static foo(ILjava/lang/String;FZ)I
.var 0 is x I from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
.var 2 is z F from Label0 to Label1
.var 3 is t Z from Label0 to Label1
Label0:
	iload_3
	ifle Label2
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label2:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	getstatic MPClass.i I
	bipush 110
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iload_0
	ireturn
	goto Label6
Label5:
	iload_0
	iconst_1
	iadd
	ldc "PPL"
	fload_2
	ldc 1.5
	fadd
	iload_3
	ifgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	invokestatic MPClass/foo(ILjava/lang/String;FZ)I
	iload_0
	iadd
	ireturn
Label6:
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	putstatic MPClass.i I
	bipush 10
	ldc "ppl"
	ldc 1.23
	iconst_1
	invokestatic MPClass/foo(ILjava/lang/String;FZ)I
	i2f
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
