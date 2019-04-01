.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static newArray()[I
.var 0 is a [I from Label0 to Label1
Label0:
	bipush 51
	newarray int
	astore_0
.var 1 is i I from Label2 to Label3
Label2:
	iconst_0
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
	bipush 50
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	aload_0
	iload_1
	iconst_0
	isub
	iload_1
	iastore
	goto Label4
Label5:
Label3:
	aload_0
	areturn
Label1:
	return
.limit stack 10
.limit locals 2
.end method

.method public static sumArray([I)I
.var 0 is a [I from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label3
.var 2 is sum I from Label2 to Label3
Label2:
	iconst_0
	istore_2
	iconst_0
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
	bipush 50
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_2
	aload_0
	iload_1
	iconst_0
	isub
	iaload
	iadd
	istore_2
	goto Label4
Label5:
	iload_2
	ireturn
Label3:
Label1:
	return
.limit stack 8
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/newArray()[I
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	invokestatic MPClass/sumArray([I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
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
