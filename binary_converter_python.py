#Base 10 to Binary converter program
import math

x = int(input("Enter a number to see its binary conversion ")) #Prompts the user to enter an integer
y = [] # creating an empty list
z = x
remainder = [] #creating an empty list to store remainder

def dec2Binary():
    global x,y,z,remainder

    #code for finding the binary number from decimal
    while(x>0): #A while loop that runs until the quotient is greater than zero
        remainder.append(x % 2) #Adds the remainder to the variable remainder that holds an empty list.
        x = x//2
        y.append(x)
        
    print("The binary form of " + str(z) + " is "+ str(remainder[::-1])) #Reverses the list stored in the remainder variable to get the binary form 

def binary2Decimal():
    global x,y,z,remainder
    decimal_number = 0
    power= 0
    while x > 0:
        decimal_number += 2 ** power * (x % 10)
        x //= 10
    print("The decimal (base 10) form of " + str(z) + " is " + str(decimal_number))

    
dec2Binary()

binary2Decimal()
