.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static absFloat(I)F
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	i2f
	ldc 1.0
	fmul
	freturn
	goto Label5
Label4:
	iload_0
	ineg
	i2f
	ldc 1.0
	fmul
	freturn
Label5:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 167
	invokestatic MPClass/absFloat(I)F
	invokestatic io/putFloatLn(F)V
	sipush 167
	ineg
	invokestatic MPClass/absFloat(I)F
	invokestatic io/putFloatLn(F)V
	sipush 167
	invokestatic MPClass/absFloat(I)F
	sipush 167
	ineg
	invokestatic MPClass/absFloat(I)F
	fsub
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 2
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
