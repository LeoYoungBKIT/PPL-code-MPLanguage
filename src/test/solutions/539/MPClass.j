.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static func([FIIF)[F
.var 0 is x [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is z F from Label0 to Label1
.var 4 is t I from Label0 to Label1
Label0:
	iload_1
	istore 4
	iload 4
	iconst_1
	isub
	istore 4
Label2:
	iload 4
	iconst_1
	iadd
	istore 4
	iload 4
	iload_2
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_0
	iload 4
	iconst_1
	isub
	aload_0
	iload 4
	iconst_1
	isub
	faload
	iconst_2
	i2f
	fmul
	fload_3
	fmul
	fastore
	goto Label2
Label3:
	aload_0
	areturn
Label1:
	return
.limit stack 10
.limit locals 5
.end method

.method public static print([F)V
.var 0 is x [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_2
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_0
	iload_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_2
	newarray float
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
	iconst_2
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
	iload_2
	i2f
	fastore
	goto Label2
Label3:
	aload_1
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	iconst_1
	iconst_2
	iconst_3
	i2f
	invokestatic MPClass/func([FIIF)[F
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	iconst_1
	iconst_2
	iconst_1
	ineg
	i2f
	invokestatic MPClass/func([FIIF)[F
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	invokestatic MPClass/print([F)V
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
