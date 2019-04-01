.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_0
	iand
	invokestatic io/putBool(Z)V
	iconst_1
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_1
	iand
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_0
	iand
	invokestatic io/putBool(Z)V
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
	return
.limit stack 0
.limit locals 0
.end method
