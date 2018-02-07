# strings

greeting = "hello"
greeting2 = 'hello'
greeting3 = "I'm doing good"
# or
greeting3 = 'I\'m doing good' 
 # in both cases greeting3[1] is '

 print(greeting[0])

 print(greeting[4]) 
 #or
 print(greeting[-1])

 #substring

 print(greeting[0:3]) 
 print(greeting[-1:1]) 
 print(greeting[2:-1])

 a = "python"
 b = "programming"
 print(a+b)
 print(a*2 + b*2)
 print('p' in a)
 print('p' not in a)

 lang = "c,java,python,ruby,c++"
 print(len(lang))
 print(lang.split(',')) #only delimitter
 print(lang.split(" ",len(lang))) #delimitter plus no of splits

 s= "python is a simple programming language"
 print(s.title())  
 print(s.capitalize())
 print(s.count('s',0,len(a))) 
 print(s.find('i',0,len(b))) 
 print(s.upper()) 