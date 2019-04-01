.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static printSum(III)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	iload_2
	iadd
	invokestatic io/putIntLn(I)V
	iconst_0
	istore_0
	iconst_0
	istore_1
	iconst_0
	istore_2
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	bipush 6
	bipush 7
	invokestatic MPClass/printSum(III)V
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
.limit locals 2
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
