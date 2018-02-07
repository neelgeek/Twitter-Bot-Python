#functions

def func1():
	print("this is a function")

def func2(name , age , college):
	print(f'hello {name} , you are {age} years old and you are studying in {college} college')

func2("rohit" , 12 , "RAIT")

#default parameters
def area_rect(length=10 , breadth=10):
	area = length * breadth

area_rect()
area_rect(20,40)
area_rect(length=30)

# return keyword
def area_circle(radius):
	return 3.14*(radius**2)

area = area_circle(5)
print(area)

# functions with varialbe no of arguments
def varfunc(*args):
	for arg in args:
		print(arg)

varfunc()
varfunc(1)
varfunc(1,2,3,4)

# recursive functions
def factorial(x):
	if x==1:
		return 1
	else:
		return (x*factorial(x-1))

print(factorial(5))


#lambda funtion / anonymous function

square = lambda i: i**2
print(square(7))

sum = lambda x,y: x+y
print(sum(2,7))
