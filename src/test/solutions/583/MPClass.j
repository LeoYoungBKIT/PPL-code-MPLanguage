.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
Label2:
	iconst_1
	ifle Label3
Label4:
	iconst_1
	ifle Label5
Label8:
	iconst_0
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	goto Label9
	goto Label8
Label9:
	goto Label5
	goto Label4
Label5:
	goto Label3
	goto Label2
Label3:
	sipush 10000
	ineg
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	sipush 10000
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_1
	iload_1
	imul
	bipush 9
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	goto Label10
Label16:
	iload_1
	invokestatic io/putIntLn(I)V
	goto Label10
Label11:
Label1:
	return
.limit stack 11
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
