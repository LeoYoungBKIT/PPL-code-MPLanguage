.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static x()Z
Label0:
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.a I
	iconst_1
	ireturn
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static nx()Z
Label0:
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.a I
	iconst_0
	ireturn
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
	putstatic MPClass.a I
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	invokestatic MPClass/nx()Z
	invokestatic MPClass/x()Z
	iand
	dup
	ifgt Label2
	invokestatic MPClass/x()Z
	ior
Label2:
	dup
	ifle Label3
	invokestatic MPClass/nx()Z
	iand
Label3:
	invokestatic MPClass/x()Z
	dup
	ifgt Label4
	invokestatic MPClass/nx()Z
	invokestatic MPClass/nx()Z
	iand
	ior
Label4:
	ior
	invokestatic io/putBool(Z)V
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
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
