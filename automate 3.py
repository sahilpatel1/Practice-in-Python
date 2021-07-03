'''
# A function is a miniprogram within a program
def hello():
    print("Sahil Patel \n" * 5) # \n starts a new line
hello() #Calling a function or Revoke it

# Functions organize code and enforces the idea of deduplicating code

#Passing Arguments inside the parentheses ()
def hello(name): #In this function, name is a parameter that is a variable that holds an argument "Sahil"
    print("Hello there, " + name)

hello("Sahil")

import random

def getanswer(answer):
    if answer == 1:
        return "It is certain"
    elif answer == 2:
        return "It is decidely so"
    elif answer == 3:
        return "Yes"
    elif answer == 4:
        return "Reply hazy try again"
    elif answer == 5:
        return "Ask again later"
    elif answer == 6:
        return "Concentrate and ask again"
    elif answer == 7:
        return "My reply is no"
    elif answer == 8:
        return "Outlook not so good"
    elif answer == 9:
        return "Very doubtful"

r = random.randint(1,9)
fortune = getanswer(r)
print(fortune)

# Global scope can be used by a local scope
print("car","house","money","fame",sep=",") #Passing key arguments

def spam():
    global eggs
    eggs = "spam" #this is the global

def bacon():
    eggs = "bacon" #this is a local

def ham():
    print(eggs) #this is the global

eggs = 42 #this is the global
spam()
print(eggs)

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: #The code under "execpt" runs when an error occurs 
        print("Error: Invalid argument")

print(spam(2))
print(spam(12))
print(spam(14))
print(spam(0))

#Let's play a guessing game

import random
secret = random.randint(1,20)
print("I am thinking of a number between 1 and 20")

#Asking a player to guess the right number
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secret:
        print("The number is too low")
    elif guess > secret:
        print("The number is too high")
    else:
        break #This condition is the correct guess and it breaks out of the for loop!
if guess == secret:
    print("Congrats! You chose the correct number")
else:
    print("Nope, the number I was thinking was " + str(secret))
'''
#The collatz sequence


def collatz(number):
    number = int(input("Enter an integer: "))
    while(number!=1):
        if(number%2 == 0):
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)


collatz(5)
    
