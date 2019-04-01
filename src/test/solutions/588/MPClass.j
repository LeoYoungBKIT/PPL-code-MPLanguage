.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
Label0:
	bipush 12
	istore_1
	iconst_4
	i2f
	iconst_5
	i2f
	fdiv
	iload_1
	i2f
	fmul
	bipush 34
	i2f
	fdiv
	iconst_3
	i2f
	fsub
	bipush 76
	i2f
	iconst_4
	i2f
	fdiv
	fadd
	iconst_4
	ineg
	ineg
	ineg
	ineg
	ineg
	bipush 7
	imul
	i2f
	fsub
	bipush 7
	ineg
	ineg
	ineg
	ineg
	i2f
	fsub
	bipush 7
	ineg
	ineg
	ineg
	ineg
	i2f
	fsub
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
	fload_2
	ldc 5.0
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	fload_2
	ldc 5.0
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	fload_2
	iconst_5
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	iload_1
	i2f
	ldc 12.0
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBoolLn(Z)V
	iload_1
	bipush 12
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
	iload_1
	bipush 12
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 13
.limit locals 4
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
