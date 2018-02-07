# map and filter function

# filter
# takes in function and list as arguments and returns list of items for which the function evaluates to true

#retireve odd nos
list1 = [1,2,3,4,5,6,7,8,9]

#normal filter
def odd(num):
	return num%2!=0

list2 = list(filter(odd,list1))
print(list2)

#filter using lambda
list2 = list(filter(lambda x:(x%2!=0), list1))
print(list2)


list3= []
for item in list1:
	if item%2!=0:
		list3.append(item)
print(list3)

print([ item for item in list1 if item%2!=0])   #using comprehension


#map
# takes in function and list as arguments and returns the result of function performed on all items
#double the nos

def doub(x):
	return x*2

list4 = list(map(doub,list1))

#map with lambda
list4 = list(map(lambda x:(x*2), list1)) 


list5 = []
for item in list1:
	list5.append(doub(item))

print( [ item*2 for item in list1 ])  #using comprehension


#taking multiple inputs at once using map
a,b,c=map(int,input().strip().split())