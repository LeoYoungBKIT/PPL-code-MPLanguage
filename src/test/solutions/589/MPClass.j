.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static sortArray([I)[I
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is temp I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 8
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	bipush 8
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	aload_0
	iload_2
	iconst_0
	isub
	iaload
	aload_0
	iload_2
	iconst_1
	iadd
	iconst_0
	isub
	iaload
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	aload_0
	iload_2
	iconst_0
	isub
	iaload
	istore_3
	aload_0
	iload_2
	iconst_0
	isub
	aload_0
	iload_2
	iconst_1
	iadd
	iconst_0
	isub
	iaload
	iastore
	aload_0
	iload_2
	iconst_1
	iadd
	iconst_0
	isub
	iload_3
	iastore
Label12:
	goto Label6
Label7:
	goto Label2
Label3:
	aload_0
	areturn
Label1:
	return
.limit stack 16
.limit locals 4
.end method

.method public static printArray([I)V
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 9
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_0
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putIntLn(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is myArray [I from Label0 to Label1
Label0:
	bipush 10
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_0
	isub
	bipush 50
	iastore
	aload_1
	iconst_1
	iconst_0
	isub
	bipush 70
	iastore
	aload_1
	iconst_2
	iconst_0
	isub
	iconst_0
	iastore
	aload_1
	iconst_3
	iconst_0
	isub
	bipush 10
	iastore
	aload_1
	iconst_4
	iconst_0
	isub
	bipush 90
	iastore
	aload_1
	iconst_5
	iconst_0
	isub
	bipush 60
	iastore
	aload_1
	bipush 6
	iconst_0
	isub
	bipush 30
	iastore
	aload_1
	bipush 7
	iconst_0
	isub
	bipush 20
	iastore
	aload_1
	bipush 8
	iconst_0
	isub
	bipush 40
	iastore
	aload_1
	bipush 9
	iconst_0
	isub
	bipush 80
	iastore
	aload_1
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	invokestatic MPClass/sortArray([I)[I
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	invokestatic MPClass/printArray([I)V
	aload_1
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	invokestatic MPClass/printArray([I)V
Label1:
	return
.limit stack 26
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
