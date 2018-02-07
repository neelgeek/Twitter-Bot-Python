#list comprehensions

nos = [20 ,34 , 45 , 63]
doub_nos = []
#normal method

for no in nos:
	doub_nos.append(no*2)
print(doub_nos)

#comprehension method

doub_nos = [ no*2 for no in nos ]
print(doub_nos)

#to double only even nos

doub_nos= [ no*2 for no in nos if no%2==0 ]
print(doub_nos)

for no in nos:
	if no%2==0:
		doub_nos.append(no*2)
print(doub_nos)