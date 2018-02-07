#loops
#for loop

savings = [100,200,150,450,600]
sum=0
for saved in savings:
	sum+=saved
print("total savings are",sum)

a="whats up"
for i in a:
	print(i) # for single line use end parameter in print

savings = [100,200,150,450,600]
sum=0
for saved in savings[0:3]:
	sum+=saved
print("total savings are",sum)
#remeber to use for to iterate in a dictionary by for key,val in dictionary.items()

dict1 = {1:'a', 2:'b', 3:'c'}
for key,val in dict1.items():
	print("key is {0} and value is {1}".format(key,val))

# ranges
for i in range(6):
	print(i)
for i in range(1,10):
	print(i)
for i in range(0,21,2):
	print(i)

for i in range(10,0,-1):
	print(i)	

#while loops

num = 0

while num<10:
	print(num)
	num+=1

num = 0
while num<=50:
	if num%2==0:
		print(num)
    num+=1
    if num >40:
    	break
    if num == 37:
    	num+=1
    	continue
