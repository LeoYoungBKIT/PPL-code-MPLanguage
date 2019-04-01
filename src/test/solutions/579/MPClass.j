.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I

.method public static foo1(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
Label4:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo2(I)I
	ireturn
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo2(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
Label4:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo3(I)I
	ireturn
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo3(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
Label4:
	iload_0
	invokestatic io/putIntLn(I)V
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo1(I)I
	ireturn
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass.n I
	getstatic MPClass.n I
	invokestatic MPClass/foo1(I)I
	istore_1
Label1:
	return
.limit stack 3
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
