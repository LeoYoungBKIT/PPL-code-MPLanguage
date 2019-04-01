.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	bipush 100
	i2f
	fstore_1
	bipush 100
	ineg
	i2f
	fstore_2
Label4:
	fload_1
	fload_2
	fcmpl
	ifeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iconst_1
	ineg
	i2f
	fload_1
	fadd
	fstore_1
	iconst_1
	i2f
	fload_2
	fadd
	fstore_2
	goto Label4
Label5:
	fload_1
	fload_2
	fsub
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 6
.limit locals 3
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
