.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static newArray()[Z
.var 0 is a [Z from Label0 to Label1
Label0:
	iconst_3
	newarray boolean
	astore_0
	aload_0
	iconst_1
	iconst_1
	iadd
	iconst_1
	bastore
	aload_0
	iconst_1
	ineg
	iconst_1
	iadd
	aload_0
	iconst_1
	iconst_1
	iadd
	baload
	bastore
	aload_0
	iconst_0
	iconst_1
	iadd
	aload_0
	iconst_1
	ineg
	iconst_1
	iadd
	baload
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	bastore
	aload_0
	areturn
Label1:
	return
.limit stack 16
.limit locals 1
.end method

.method public static printArray([Z)V
.var 0 is a [Z from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label3
Label2:
	iconst_1
	ineg
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
	iconst_1
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
	iadd
	baload
	invokestatic io/putBoolLn(Z)V
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/newArray()[Z
	iconst_0
	iconst_1
	iadd
	baload
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/newArray()[Z
	invokevirtual [Z/clone()Ljava/lang/Object;
	checkcast [Z
	invokestatic MPClass/printArray([Z)V
Label1:
	return
.limit stack 3
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
