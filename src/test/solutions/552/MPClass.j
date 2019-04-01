.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.a [Z
	iconst_3
	iconst_3
	iadd
	iconst_1
	bastore
	getstatic MPClass.a [Z
	iconst_3
	ineg
	iconst_3
	iadd
	getstatic MPClass.a [Z
	iconst_3
	iconst_3
	iadd
	baload
	bastore
	getstatic MPClass.a [Z
	iconst_2
	ineg
	iconst_3
	iadd
	getstatic MPClass.a [Z
	iconst_3
	ineg
	iconst_3
	iadd
	baload
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	bastore
	getstatic MPClass.a [Z
	iconst_3
	ineg
	iconst_3
	iadd
	baload
	invokestatic io/putBool(Z)V
	getstatic MPClass.a [Z
	iconst_2
	ineg
	iconst_3
	iadd
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 16
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
	newarray boolean
	putstatic MPClass.a [Z
	return
.limit stack 1
.limit locals 0
.end method
