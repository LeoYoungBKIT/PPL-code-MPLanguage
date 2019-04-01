.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static globalInt I
.field static globalFloat F
.field static globalBool Z
.field static globalArray [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is localInt I from Label0 to Label1
.var 2 is localFloat F from Label0 to Label1
.var 3 is localBool Z from Label0 to Label1
.var 4 is localArray [F from Label0 to Label1
Label0:
	iconst_5
	newarray float
	astore 4
	iconst_1
	ineg
	iconst_2
	ineg
	imul
	iconst_1
	iadd
	iconst_3
	irem
	putstatic MPClass.globalInt I
	getstatic MPClass.globalInt I
	i2f
	fstore_2
	aload 4
	iconst_2
	iconst_1
	isub
	fload_2
	fastore
	getstatic MPClass.globalArray [F
	iconst_1
	iconst_1
	isub
	aload 4
	iconst_2
	iconst_1
	isub
	faload
	fastore
	getstatic MPClass.globalArray [F
	iconst_1
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
	aload 4
	iconst_2
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
	fload_2
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.globalInt I
	invokestatic io/putIntLn(I)V
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
	iconst_5
	newarray float
	putstatic MPClass.globalArray [F
	return
.limit stack 1
.limit locals 0
.end method
