.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iload_1
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	iload_1
	iconst_2
	imul
	istore_1
Label7:
	goto Label8
Label4:
	bipush 11
	istore_1
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpeq Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	iload_1
	iconst_3
	imul
	iconst_2
	idiv
	istore_1
Label11:
Label8:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 10
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
