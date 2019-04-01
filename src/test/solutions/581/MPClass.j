.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I

.method public static foo(Ljava/lang/String;I)Ljava/lang/String;
.var 0 is x Ljava/lang/String; from Label0 to Label1
.var 1 is num I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
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
	iload_1
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label2
Label3:
	getstatic MPClass.n I
	iconst_1
	iadd
	putstatic MPClass.n I
	getstatic MPClass.n I
	bipush 20
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "END"
	areturn
	goto Label9
Label8:
	ldc "PPL"
	iconst_5
	invokestatic MPClass/foo(Ljava/lang/String;I)Ljava/lang/String;
	areturn
Label9:
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 15
	putstatic MPClass.n I
	ldc "ppl"
	iconst_5
	invokestatic MPClass/foo(Ljava/lang/String;I)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
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
