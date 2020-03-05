'''
syntax:
if Condition1:
	Statements
elif Condition2:
	Statements
elif Condition3:
	Statements
elif Condition4:
	Statements
--------------------------
-------------------------
-----------------
else:
	Statements
'''
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
if a>b and a>c:
	print("a is big:",a)
elif b>a and b>c:
	print("b is big:",b)
elif c>a and c>b:
	print("c is big:",c)
else:
	print("Second  or Third Nums are same")

