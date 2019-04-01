.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.a [I
	iconst_0
	iconst_3
	iadd
	iconst_1
	iconst_2
	iconst_3
	iconst_4
	imul
	iconst_5
	bipush 10
	iconst_2
	iconst_3
	iadd
	idiv
	isub
	iadd
	iadd
	imul
	iastore
	getstatic MPClass.a [I
	iconst_1
	iconst_3
	iadd
	iconst_2
	ineg
	getstatic MPClass.a [I
	iconst_0
	iconst_3
	iadd
	iaload
	ineg
	imul
	iconst_3
	imul
	iastore
	getstatic MPClass.a [I
	iconst_1
	iconst_3
	iadd
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 10
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
	bipush 7
	newarray int
	putstatic MPClass.a [I
	return
.limit stack 1
.limit locals 0
.end method
