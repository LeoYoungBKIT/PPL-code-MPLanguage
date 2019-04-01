.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static INTMAX I
.field static INTMIN I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 2147483647
	putstatic MPClass.INTMAX I
	getstatic MPClass.INTMAX I
	iconst_1
	ineg
	imul
	iconst_1
	isub
	putstatic MPClass.INTMIN I
	getstatic MPClass.INTMAX I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.INTMIN I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.INTMAX I
	getstatic MPClass.INTMIN I
	iadd
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
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
