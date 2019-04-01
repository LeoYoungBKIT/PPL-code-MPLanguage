.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass.i I
	getstatic MPClass.i I
	iconst_1
	isub
	putstatic MPClass.i I
Label2:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	getstatic MPClass.i I
	bipush 10
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass.i I
	iconst_5
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label3
Label8:
	goto Label2
Label3:
	getstatic MPClass.i I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass.i I
	getstatic MPClass.i I
	iconst_1
	isub
	putstatic MPClass.i I
Label9:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
	getstatic MPClass.i I
	bipush 10
	if_icmplt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	goto Label9
	goto Label16
Label15:
	getstatic MPClass.i I
	invokestatic io/putInt(I)V
Label16:
	goto Label9
Label10:
Label1:
	return
.limit stack 9
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
