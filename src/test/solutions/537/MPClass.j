.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/T()Z
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/F()Z
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/T()Z
	dup
	ifle Label2
	invokestatic MPClass/FOO()Z
	iand
Label2:
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/F()Z
	dup
	ifle Label3
	invokestatic MPClass/FOO()Z
	iand
Label3:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static T()Z
Label0:
	iconst_1
	ireturn
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static F()Z
Label0:
	iconst_0
	ireturn
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static FOO()Z
Label0:
	ldc "FOO!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
	return
.limit stack 2
.limit locals 0
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
