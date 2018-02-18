print("hello world")
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#OR

a , b , c = 5 , 2.0 , 1+2j
# or
a=5;b=2.0;c=1+2j

b =25
print(b)
b+= 5
print(b)

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print('The value of x is %3.2f' %x)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

name = input("what is your name")
print(name)


length = float(input("enter length of rectangle"))
breadth = float(input("enter breadth of rectangle"))

area = length * breadth
print("the area of the rectangle is", area) 

print ("the length is" , length, "and the breadth is" , breadth)

print("the length is {0} and breadth is {1} ".format(length,breadth))

print("the length is {0:.5} and breadth is {1:.5} ".format(length,breadth))
print("the length is {0:.5f} and breadth is {1:.5f} ".format(length,breadth))
print("the length is %f and the breadth is %f %(length,breadth)")
print(f"the length is {length:.5} and breadth is {breadth:.5} ")

