.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is k I from Label0 to Label1
.var 4 is counter I from Label0 to Label1
Label0:
	iconst_0
	istore 4
	bipush 9
	istore_1
	iload_1
	iconst_1
	iadd
	istore_1
Label2:
	iload_1
	iconst_1
	isub
	istore_1
	iload_1
	iconst_1
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	bipush 8
	istore_2
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	iload_2
	iconst_1
	isub
	istore_2
	iload_2
	iconst_1
	if_icmplt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	bipush 7
	istore_3
	iload_3
	iconst_1
	iadd
	istore_3
Label10:
	iload_3
	iconst_1
	isub
	istore_3
	iload_3
	iconst_1
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label10
Label11:
	goto Label6
Label7:
	goto Label2
Label3:
	iload 4
	bipush 7
	bipush 8
	imul
	bipush 9
	imul
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 10
.limit locals 5
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
