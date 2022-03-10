                                                            Python Programming Language   🐍
                                                           ==================================



🔴 Why Learning Python ? 
🔵 Python is highly versatile. You can use it for both small and complex tasks, and it is used across many different industries — from its more common applications in data science and software engineering to environments like mobile app development,
 artificial intelligence, and machine learning. This multifaceted use is due to the wide array of Python libraries available (over 125,000, to be specific). Libraries are collections of pre-written code in a particular language that anyone can access, meaning that once you’ve learned the basics of Python, you’ll likely be able to understand and use a huge amount of code developed by other programmers.
Another important aspect of Python’s versatility is its ability to run with other programming languages. A few common examples of Python implementation with other languages are Jython (Python integrated with Java) and CPython (Python integrated with C). Lastly, Python offers cross-platform functionality, meaning that it will function properly whether you’re working with Windows, Linux, or macOS.


==> To Print output in python ==>   write print(" ") , it can possible single quote print(' ')

ℹ️ - in the First , What is A Variable ?
🪗 - Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program.

ℹ️ - Assigning Value to Variables ? 
🪗 - Naming variables is known as one of the most difficult tasks in computer programming. When you are naming variables, think hard about the names. Try your best to make sure that the name you assign your variable is accurately descriptive and understandable to another reader. Sometimes that other reader is yourself when you revisit a program that you wrote months or even years earlier.
When you assign a variable, you use the = symbol. The name of the variable goes on the left and the value you want to store in the variable goes on the right.

like ==>  

name = 'waled'
print(name) ===>  return waled ☑️


print('my name is ' + name) ===> return my name is waled ☑️     ==> this way called Concatination is the connect between string & variable 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Strings  📝
===========

🔖 print('welcome') ==> write String welcome 

🔖 print('welc\nome') ==> write welc in line and ome in another side 

🔖 print('welc\tome') ==> write welc and take space 4k and write ome

🔖 print('welc\aome') ==> write welcome and ring sound

🔖 print('welc\"ome') ==> write welc"ome 



text = 'waled'

🎗 print(text.upper()) ==>  create the string in upper case state
🎗 print(text.lower()) ==>  create the string in lower case state
🎗 print(text.isUpper()) ==> check the characters and return true or false
🎗 print(text.isLower()) ==> check the characters and return true or false
🎗 print(len(text)) ==> return numbes of characters ex waled = 5
🎗 print(text[0]) ==> return characters of index say 0 = w the indexing in programming start from 0
🎗 print(text.index('e')) ==> return the index of character like 'e' = 3
🎗 print(text.replace('old', 'new')) ==>  in the first it replaced the old String by new string like  
          text = 'hello world ' 
          print(text.replace('hello', 'welcome')) ==> return welcome world

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Numbers ¹²³
============

num = 5
print(num+ 'is my perfect number') ==> ❌ Because it's a String 
print (str(num) +  'is my perfect number') ==> ✔️ return 5 is my perfect number


num = -10 
print(abs(num)) ==> print 10 abs return absolute value 

num1 = 2 
num2 = 3 
print(pow(num1 , num2)) ==> return 2^3 = 8 

print(max(2, 10)) ==> return max value = 10

print(min(2, 10)) ==> return min value = 2

print(round(2,8)) ==> return round of number  = 3

print(floor(3.7)) ==> return floor of number default min = 3

print(ceil(3.2)) ==> return ceil of number default max = 4

print(sqrt(9)) ==> return square of num = 3 
 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Getting Input ✉
=================

৳ name = input('Enter Your Name : ')

৳ age = input('Enter Your Age : ')

print('Hello '+name + ' My Age is ' + age )

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Building calculator ⌨️
=======================


৳ num1 = input('enter num one :')
৳ num2 = input('enter num two :')

result = num1 + num2

print (result)  ===========> The output if input 10 and 10 like (1010) Because it's String  Wrong way ❌  



num1 = input('enter num one :')
num2 = input('enter num two :')

result = int(num1) +int(num2)

print (result)  ===========> The output if input 10 and 10   = 20 right way ✔️


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
MAD LIBS 🎩
============

color = input('Enter a Color : ')

plural_noun = input('Enter a Plural noun : ')

adjective = input('Enter an Adjective : ')


print('trees are ' + color)

print(plural_noun + ' are mean')

print('please keep it ' + adjective)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Lists 📄
=========

🔎 friends = ['ali', 'ahmed' , 12, False , 12.9, 'c']
print(friends[5])  ==> print  = c



🔎friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
print(friends[1:3]) ==> print the element start indexing 1 to the element before the end index 


🔎friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
print(friends[3:]) ==> print the all elemts starts from index 3 to the end 


🔎friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends[0] = 'malak'
print(friends[0])  ==> print malak this is editing from variable List 



🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
ages = [10,20,30,40,50,60]
friends.extend(ages)
print(friends)==> print ['ali', 'ahmed', 'mohame', 'waled', 'marwan', 'abdullah', 10, 20, 30, 40, 50, 60] return  Concatinatinate two lists 


🔎 another way 
friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
ages = [10,20,30,40,50,60]
friends += ages 
print(friends)

🔎friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.append('samy')
print(friends) ==> Print all data in list after add element samy

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.insert(0, 'wael')
print(friends) ==> Print all data in list after add element wael adding by index

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.remove('ahmed')
print(friends)Print all data in list after removing element ahmed

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.clear()
print(friends) ==> Clear All List

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.pop()
print(friends) ==> delete the last element in list and print iist


🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
print(friends.count('ali')) ==> count how many ali write in list 

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
friends.sort()
print(friends)  ==>  print all list after sorted all elements

🔎 friends = ['ali', 'ahmed' , 'mohame', 'waled' ,'marwan', 'abdullah']
newList = friends.copy()
print(newList) ==> print copy list

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Tuples 📉
==========


🔎 orders = (10,20,30)
print(orders) ==> print all variable in tuple (10,20,30)

🔎 orders = (10,20,30)
print(orders[1])==> printindex 1 in tuple

🔴 Tuples not update data in variable

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Functions 🗝
=============

🗝 def sayHi ():
    print('Hello Users')
    
    
sayHi()  ==> print Hello Users




🗝 def sayHi (name ):
    print('Hello ' + name)
    
    
sayHi("waled") ==> print Hello waled




🗝 def sayHi (name , age):
    print('Hello ' + name + ' and My Age is : '+ str(age))
    
    
sayHi("waled" , 22)




🗝 def cube(num):
  return  num*num*num
    
result =cube(2)

print(result)




🗝 def sum(num1 , num2):
    return  num1+num2

result = sum(2, 8)
print(result)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Conditions  ⚜️
===============

a = 33
b = 200
if b > a:
  print("b is greater than a") 



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


🔴 Indentation: Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Building calculator ⌨️
=======================

num1 = float(input('Enter Num 1 : '))
operator = input('Please Enter an Operator ')
num2 = float(input('Enter Num 2 : '))


if operator =='+':
    print(num1+num2)
    
elif operator =='-':
    print(num1-num2)
    
elif operator =='*':
    print(num1*num2)
    
elif operator =='/':
    print(num1/num2)

elif operator =='%':
    print(num1%num2)
    
else:
    print('Wrong Answer !')


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Dictionary ▨
============== like Map 

▨ month = {
    'jan' : 'january',
    'fab' : 'febrawry',
    'mar' : 'mars',
    'apr' : 'arril',
    
    }


print(month) ==> print all Dic







▨ month = {
    'jan' : 'january',
    'feb' : 'febrawry',
    'mar' : 'mars',
    'apr' : 'arril',
    
    }


print(month['feb']) ==> print dec when element = feb

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
loops ⎚卍
==========

卍 i = 1
while i<=10:
    print(i)
    i += 1 
    
    
print('Loop has been ended') ==> print nums from 1 to 10  and this phase




i = 1
while i < 6:
  print(i)
  if i == 3:
    break  ==> Exit the loop when i is 3 
  i += 1 




  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue ==>Continue to the next iteration if i is 3
  print(i)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)   ==> Loop the elements in List



for x in range(6):
  print(x) ==> Print element from 0 to 5


for x in range(2, 6):
  print(x) ==> print element from 2 to 5 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Exponents Function ⌾
======================

⌾ def power(baseNum, powNum):
    result =1 
    for index in range (powNum):
        result = result * baseNum
    return result
print(power(5,5))
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
2 D.List  ❆
=============

 ❆ list = [
        
        [1,2,3],
        [4,5,6,],
        [7,8,9,],
        [0],
        
        ]

print(list[1]) ==> Print[4,5,6]






 ❆ list = [
        
        [1,2,3],
        [4,5,6,],
        [7,8,9,],
        [0],
        
        ]

print(list[2][0]) ==> print 7 first index of row , second index of columns

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Comments ♯ 
===========



♯  #hello 


♯  #hhhhh
♯  #jjjjjjj
♯  #oooooo

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Try & Except ☋
===============

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Reading File 📜
================

workfile = open('C:/Users/zs/Desktop/xxx.txt', 'r')
print(workfile.read())

workfile.close() ==> print all data in file



workfile = open('C:/Users/zs/Desktop/xxx.txt', 'r')
print(workfile.read())

workfile.close() ==> print true or false to accept data 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Write File 📜
===============

workfile = open('C:/Users/zs/Desktop/WWW.txt', 'w')
print(workfile.write("Hello World !"))

workfile.close()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Classes & Objects 📁
=====================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Inheritance 🚻
===============

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Iterantors ➰
=============

mytuple = ("Waled", "Saied", "Khames")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mytuple = ("Waled", "Saied", "Khames")

for x in mytuple:
  print(x)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Dates 📅
=========

import datetime
x = datetime.datetime.now()
print(x)


import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Py Json  📉
============
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])






import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
# the result is a JSON string:
print(y)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

String Formating 📒
=====================

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Created By : Waled Saied ✎

