# if else 
age = int(input("enter age"))
if age>0:
	print("positive age")
else:
	print("negative age")

# if elif ladder
salary=int(input("enter salary"))
if salary<10000:
	total=salary-0.1*salary
	print(total)
elif salary<50000:
	total=salary-0.2*salary
	print(total)
elif salary<100000:
	total=salary-0.3*salary
	print(total)
else:
	total=salary-0.5*salary
	print(total)

#nested if
marks = int(input("enter marks"))
if marks < 0: # to prevent negative input
	print("how come did soooo bad!")
else:
	if marks < 35:
		print("you failed")
	elif marks < 65:
		print("you did ok")
	elif marks < 85:
		print("damn youre good")
	else:
		print("how come your in rait")

# ternary operator  
a,b=10,20
min = a if a<b else b
#or
min = ( (b, a) [a < b] )  #syntax  (false_test,true_test)[test]
#or
print ("equal" if a == b else "a is greater" if a > b else "b is greater")

if a == b:
	print("equal")
else:
    if a > b:
        print("a is greater")
    else:
        print("b is greater")

#greatest of 3 numbers

# if(a>b):
# 	if(a>c):
# 		print("a is greatest")
# 	else:
# 		print("c is greatest")
# else:
# 	if(b>c):
# 		print("b is greatest")
# 	else:
# 		print("c is greatest")