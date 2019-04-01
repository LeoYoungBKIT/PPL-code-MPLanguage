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
	iload 4
	istore_1
Label4:
	iload_1
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iconst_0
	istore_2
Label8:
	iload_2
	iconst_4
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iconst_0
	istore_3
Label12:
	iload_3
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
	iload_3
	iconst_1
	iadd
	istore_3
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label12
Label13:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
	iload 4
	invokestatic io/putInt(I)V
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
