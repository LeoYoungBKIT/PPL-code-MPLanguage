.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
.var 2 is y [F from Label0 to Label1
.var 3 is z [Z from Label0 to Label1
.var 4 is t [Ljava/lang/String; from Label0 to Label1
.var 5 is i I from Label0 to Label1
Label0:
	iconst_5
	anewarray java/lang/String
	astore 4
	iconst_5
	newarray boolean
	astore_3
	iconst_5
	newarray float
	astore_2
	iconst_5
	newarray int
	astore_1
	iconst_1
	ineg
	istore 5
	iload 5
	iconst_1
	isub
	istore 5
Label2:
	iload 5
	iconst_1
	iadd
	istore 5
	iload 5
	iconst_3
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_1
	iload 5
	iconst_1
	iadd
	iload 5
	iastore
	goto Label2
Label3:
	iconst_2
	istore 5
	aload_1
	aload_1
	aload_1
	aload_1
	iload 5
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iconst_3
	iastore
	aload_3
	aload_1
	aload_1
	aload_1
	aload_1
	iload 5
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	aload_3
	aload_1
	iload 5
	iconst_1
	iadd
	iaload
	iconst_1
	iadd
	baload
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	bastore
	iconst_1
	ineg
	istore 5
	iload 5
	iconst_1
	isub
	istore 5
Label8:
	iload 5
	iconst_1
	iadd
	istore 5
	iload 5
	iconst_3
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	aload_3
	iload 5
	iconst_1
	iadd
	baload
	invokestatic io/putBoolLn(Z)V
	goto Label8
Label9:
Label1:
	return
.limit stack 21
.limit locals 6
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
