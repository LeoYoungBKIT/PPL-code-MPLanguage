.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo([I)V
.var 0 is a [I from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label3
Label2:
	iconst_1
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_5
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	aload_0
	iload_1
	iconst_1
	isub
	iload_1
	iastore
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 10
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_5
	newarray int
	astore_1
	iconst_1
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iconst_5
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_1
	iload_2
	iconst_1
	isub
	iconst_0
	iastore
	goto Label2
Label3:
	aload_1
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	invokestatic MPClass/foo([I)V
	iconst_1
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iconst_5
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
	goto Label6
Label7:
Label1:
	return
.limit stack 10
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
