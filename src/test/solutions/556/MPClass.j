.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static t I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1000000
	ineg
	putstatic MPClass.a I
	ldc 1000000
	putstatic MPClass.b I
	getstatic MPClass.a I
	putstatic MPClass.t I
	getstatic MPClass.b I
	putstatic MPClass.a I
	getstatic MPClass.t I
	putstatic MPClass.b I
	getstatic MPClass.a I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.b I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
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
