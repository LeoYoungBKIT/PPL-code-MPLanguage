.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
.var 3 is z I from Label0 to Label1
.var 4 is f F from Label0 to Label1
.var 5 is r F from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_2
	istore_2
	iconst_5
	ineg
	istore_3
	iload_1
	iload_2
	iadd
	i2f
	fstore 4
	fload 4
	iconst_2
	i2f
	fdiv
	fstore 5
	iload_1
	iload_2
	iadd
	iload_3
	iconst_3
	imul
	isub
	invokestatic io/putIntLn(I)V
	fload 4
	fload 5
	fmul
	iload_1
	i2f
	fmul
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 6
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
