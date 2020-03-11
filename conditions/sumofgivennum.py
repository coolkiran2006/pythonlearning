num=int(input("Enter the Number:"))
sumn=0
rem=0
while num>0:
	rem=num%10
	sumn=sumn+rem
	num=num//10
print("Sum of Given number is:",sumn)

