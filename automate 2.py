spam = 2 + 2 == 4 and not 2 + 2 == 4 and 2 * 2 == 2 + 2
print(spam)

'''
name = input("Enter a name ")
password = input("enter your password ")
if name == "Mary":
    print("Hello Mary")
if password == "swordfish":
    print("Access granted")
else:
    print("Wrong password, Please try again!")

        
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break #Breaks out of the loop when the condition is true

name = input("Enter a name ")
age = int(input("Enter your age ")) 
if name=="Alice":
    print("Hi, Alice.")
elif age<21:
    print("You are not Alice, kiddo")
elif age > 100:
    print("You are not Alice, grannie.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")

spam = 0
if spam < 5:
    print("Hello, world")
    spam = spam + 1
print()
spam = 0
while spam <= 5:
    print("Hello, world")
    spam = spam + 1

while True:
    print("Who are you?")
    name = input()
    if name!= "Joe":
        continue #Takes you back to the start of the while loop if the name isn't Joe
    print("Hello, Joe. What is the password?")
    password = input()
    if password == "swordfish":
        break
print("Access granted")


balls = 0
while balls == False:
    print("You need more balls")
    break
name = "Sahil Patel"
for i in range(0,5):n
    print("My name is " + name + " " + str(i + 1))


num = 0
for i in range(num,101):
    num = num + i
print("The total when you add numbers starting from 0 to 100 is " + str(num))

for i in range(5,-1,-1):
    print(i)

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for i in range(0,12):
    print(str(i + 1) + " " + months[i])

# Importing modules from the standard library requires using the word "import" and the module name that will be used.
# To use multiple modules, you can do something like: import random, date, time, and so on...

import random
for i in range(20):
    print(str(i + 1) + " " + str(random.randint(1,21)))
    
import sys
while True:
    print("Type exit to exit")
    response = input()
    if(response == "exit"):
        sys.exit()
    print("You typed " + response + " . ")
'''
'''
Ex: 2 Practice Questions

1 True and False
2 And, or, not
3 For boolean "AND":
    T and F = F
    T and T = T
    F and F = F
    F and T = F

  For boolean "OR":
    T or T = T
    T or F = F
    F or F = F
    F or T = F

  For boolean "not":
    not True = False
    not False = True

4
    1. False
    2. False
    3. True
    4. False
    5. False
    6. True

5. >, >=, <, <=, !=, ==
6. The equal to operator checks if both sides are equal where an assignment passes a value to a variable.
7. A condition instructs a computer when to run a block of code and you should use conditions when a problem has two or more conditions to arrive at a solution.
9.

    spam = int(input("Enter a number "))
    if(spam == 1):
        print("Hello")
    elif(spam == 2):
        print("Howdy")
    else:
        print("Greetings!")

10 To get out of an infinite loop, press Ctrl + C which throws a Keyboard error.
11 Break gets out of a loop when a condition is met and continue jumps back to the while or for loop if the condition isn't met.
12 First has a stopping point, second with a starting and a stopping point, and the third has a start, stop, and an increment value.
13 

    num = 0
    while(num!=10):
        num = num + 1
        print(num)
    print()
    for i in range(1,11):
        print(i)
14 I would call the function bacon() as spam.bacon()
'''
