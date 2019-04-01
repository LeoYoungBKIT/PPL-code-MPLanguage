.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static fibo(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifle Label6
	iload_0
	ireturn
	goto Label7
Label6:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/fibo(I)I
	iload_0
	iconst_2
	isub
	invokestatic MPClass/fibo(I)I
	iadd
	ireturn
Label7:
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	bipush 28
	istore_1
	iload_1
	invokestatic MPClass/fibo(I)I
	invokestatic io/putIntLn(I)V
	bipush 7
	invokestatic MPClass/fibo(I)I
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
