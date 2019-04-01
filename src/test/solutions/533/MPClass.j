.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [F
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass.b [I
	iconst_0
	iconst_0
	isub
	iconst_0
	iastore
	getstatic MPClass.b [I
	iconst_1
	iconst_0
	isub
	getstatic MPClass.b [I
	iconst_0
	iconst_0
	isub
	iaload
	iconst_1
	iadd
	iastore
	getstatic MPClass.b [I
	iconst_2
	iconst_0
	isub
	getstatic MPClass.b [I
	iconst_1
	iconst_0
	isub
	iaload
	iconst_1
	iadd
	iastore
	getstatic MPClass.b [I
	iconst_3
	iconst_0
	isub
	getstatic MPClass.b [I
	iconst_2
	iconst_0
	isub
	iaload
	iconst_1
	iadd
	iastore
	getstatic MPClass.a [F
	getstatic MPClass.b [I
	getstatic MPClass.b [I
	iconst_1
	iconst_0
	isub
	iaload
	iconst_0
	isub
	iaload
	bipush 100
	iadd
	getstatic MPClass.b [I
	getstatic MPClass.b [I
	iconst_0
	iconst_0
	isub
	iaload
	iconst_0
	isub
	iaload
	sipush 666
	iadd
	i2f
	fastore
	getstatic MPClass.a [F
	iconst_1
	bipush 100
	iadd
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 18
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
	sipush 201
	newarray float
	putstatic MPClass.a [F
	iconst_4
	newarray int
	putstatic MPClass.b [I
	return
.limit stack 1
.limit locals 0
.end method
