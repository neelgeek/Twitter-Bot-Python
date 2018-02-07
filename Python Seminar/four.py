#dictionaries

dict1 = {1:'a', 2:'b', 3:'c'}
print(dict1[1])
dict1[4]='d' #update the dict

del dict1[1]
print(dict1)
dict1.clear() 
del dict1

dict1.get(2,"not in the dictionary")
dict1.has_key(3)  #bool return

dict1.keys()
dict1.values()

list(dict1.keys())
list(dict1.values())
