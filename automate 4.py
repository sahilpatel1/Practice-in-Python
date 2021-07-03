
num = 5
while(num > 0):
   print("Sahil Patel")
   num-=1 #Subtract by 1 each time



for i in range(5, 0, -1):
   print(i, " Let's celebrate")

print()

import random # outputs a random number
for i in range(5):
   z = random.randint(1,10)
   if(z == 9):
       print("You've won a car!", str(z))
   else:
       print("You're unlucky", str(z))


name = "Alice"
age = 50

if name == "Alice":
   print("Hi, ALice")

if (age == 50):
   print("You are Alice")
   
#Break statement

name = str(input())

while True:
   if(name == "Sahil Patel"):
       print("Your name is ", name)
       break
       
#Continue statement

while True:
   print("Who are you?")
   name = input()
   if name != "Joe":
       continue
   print("hello, Joe, What is the password?")
   password = input()
   if password == "password":
       break
print("Access granted")
       

num = int(input("enter the number of rows: "))
total = 0
while total <= num:
   print("*" * total, end = " ")
   print()
   total += 1

name = "Sahil Patel"
count = 0
vowels = "aeiou"

print(len(name))

total = 0
for num in range(101):
   total = total + num
print(total)

#Tables
i = int(input("Type a number for its table: "))
for z in range(1,11):
   print(i, " * ", z, " = ", z * i)
   
for i in range(5,-1,-1): #Counts down by 1 from 5
   print(i)

for i in range(6, 10):
   print(i)
   
print()

from random import * #Allows to have a random integer value between two integers
for i in range(5):
   print(randint(1,10), end= " ")

import sys

while True:
   print("Type exit to exit")
   response = input()
   if(response == "exit"):
       sys.exit()
   print("You typed " + response + ".")


"""
Boolean Operators: not, or, and

not True returns False, not False returns True
True and True returns True, True and False returns False
"""

print(not (5 > 4))

print((not False) or (not True)) #returns True

spam = int(input("Enter a number: "))
if(spam == 1):
   print("Hello")
elif(spam == 2):
   print("Howdy")
else:
   print("Greetings!")

for i in range(1,11):
   print(i)

num = 1
while num <= 10:
   print(num)
   num+=1
   

#To import everything from a module: from xyz import *

print(abs(-78)) #Returns absolute value of a number

print(round(5.2556,3)) #Outputs 5.256 by rounding to 3 decimal places

#Using a function to avoid duplication of code

def hello(name):
   print('Hello ' + name)
   
hello("Sahil")
hello("Patel")

print("Hello ", end=", ") #Continues in a single line
print("World")

print("cats", "dogs", "mice", sep=",")

x = [12,13,16,2]

a = ["banana", "apple", "microsoft"]
for element in a:
   print(element)
   print(element)

b = [20,10,5]
total = 0
for element in b:
   total += element
print(total)


z = 0
for i in range(1,5):
   z+=i
print(z)

d = list(range(1,3))
print(d)

print(list(range(1,9)))

total3 = 0
for i in range(1,8):
   if(i % 3 == 0):
       total3 += i
print(total3)

total4 = 0
# Compute multiples of 3 and 5 upto an integer value of 100
for i in range(1,101):
   if(i % 3 == 0 or i % 5 == 0):
       total4 += i
print(total4)

# Figuring out a prime number

i = 0
store = [] #Creating an empty list for storing values later ...
num = int(input("Enter a number to see if it is prime or not : " ))
for z in range(1,num + 1):
   if(num % z == 0):
       i += 1
       store.append(z) #Adds to a list
if(i > 2):
   print(num,"is not a prime number")
else:
   print(num,"is a prime number")

print("The number you entered is divisible by: ", store)

# Functions Chapter 3

from random import *

def getAnswer(ansnum):
   if ansnum == 1:
       return "It is certain"
   elif ansnum == 2:
       return "It is decidely so"
   elif ansnum == 3:
       return "Yes"
   elif ansnum == 4:
       return "Reply hazy try again"
   elif ansnum == 5:
       return "Ask again later"
   elif ansnum == 6:
       return "Concentrate and ask again"
   elif ansnum == 7:
       return "My reply is no"
   elif ansnum == 8:
       return "Outlook not so good"
   elif ansnum == 9:
       return "Very doubtful"

r = randint(1,9) #Passing a random integer value to variable r
fortune = getAnswer(r) #Passing the result of a function getAnswer with argument r

print(fortune, " ", r)


eggs = 99 #Global variable can be used by a local scope
def spam():
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

   
def spam():
    eggs = "spam local"
    print(eggs) # prints "spam local"

def bacon():
    eggs = "bacon local"
    print(eggs) # prints "bacon local"
    spam()
    print(eggs) # prints "bacon local"

eggs = "global"
bacon()
print(eggs) # prints "global"


def square():
    x = [1,2,3,4,5]
    y = []
    for i in range(0, len(x)):
        y.append(x[i] * x[i])
    print(y)

square()

try:
    print(x)
except:
    print("An error occurred")

# In using try and else, the else is executed if try executes.

try:
    print(2 + 2)
except:
    print("Something went wrong")
finally:
    print("Nothing went wrong")

        



