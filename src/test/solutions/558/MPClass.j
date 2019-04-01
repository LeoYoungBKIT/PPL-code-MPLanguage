.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
Label2:
	iconst_0
	ifle Label3
	ldc "FALSE"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label2
Label3:
Label6:
	sipush 256
	ineg
	iconst_1
	ineg
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	ldc "-256 > -1"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label6
Label7:
Label1:
	return
.limit stack 4
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
