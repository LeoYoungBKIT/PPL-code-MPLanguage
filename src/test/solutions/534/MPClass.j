.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [F
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.b [I
	iconst_1
	iconst_0
	isub
	ldc 1.0
	invokestatic MPClass/floatToInt(F)I
	iastore
	getstatic MPClass.b [I
	iconst_2
	iconst_0
	isub
	ldc 2.5
	invokestatic MPClass/floatToInt(F)I
	iastore
	getstatic MPClass.b [I
	iconst_1
	iconst_0
	isub
	iaload
	invokestatic io/putIntLn(I)V
	getstatic MPClass.b [I
	iconst_2
	iconst_0
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 10
.limit locals 1
.end method

.method public static intToFloat(I)F
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	i2f
	ldc 1.0
	fmul
	freturn
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static floatToInt(F)I
.var 0 is f F from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is sign I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	fload_0
	iconst_0
	i2f
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	istore_2
	goto Label5
Label4:
	iconst_1
	ineg
	istore_2
Label5:
	fload_0
	iload_2
	i2f
	fmul
	fstore_0
Label8:
	fload_0
	iconst_1
	i2f
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	fload_0
	iconst_1
	i2f
	fsub
	fstore_0
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
	iload_1
	iload_2
	imul
	ireturn
Label1:
	return
.limit stack 8
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
	iconst_2
	newarray float
	putstatic MPClass.a [F
	iconst_4
	newarray int
	putstatic MPClass.b [I
	return
.limit stack 1
.limit locals 0
.end method
