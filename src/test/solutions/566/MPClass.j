.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static y I

.method public static foo1()Z
Label0:
	bipush 10
	putstatic MPClass.x I
	iconst_1
	ireturn
Label1:
	return
.limit stack 3
.limit locals 0
.end method

.method public static foo2()Z
Label0:
	bipush 10
	putstatic MPClass.y I
	iconst_1
	ireturn
Label1:
	return
.limit stack 3
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass.x I
	iconst_5
	putstatic MPClass.y I
	iconst_1
	iconst_1
	iadd
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	dup
	ifgt Label4
	invokestatic MPClass/foo1()Z
	ior
Label4:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_1
	iadd
	iconst_2
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	invokestatic MPClass/foo2()Z
	ior
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass.x I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.y I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 6
.limit locals 2
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
