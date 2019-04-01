.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static globalInt I
.field static globalFloat F
.field static globalBool Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is localInt I from Label0 to Label1
.var 2 is localFloat F from Label0 to Label1
.var 3 is localBool Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iload_1
	putstatic MPClass.globalInt I
	iconst_1
	i2f
	fstore_2
	fload_2
	putstatic MPClass.globalFloat F
	iconst_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	putstatic MPClass.globalBool Z
	getstatic MPClass.globalBool Z
	istore_3
	getstatic MPClass.globalInt I
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	getstatic MPClass.globalFloat F
	invokestatic io/putFloatLn(F)V
	fload_2
	invokestatic io/putFloatLn(F)V
	iload_3
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.globalBool Z
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
