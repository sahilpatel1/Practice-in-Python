from math import *

"""

print("Hello world")
print("What is your name?") #ask for their name
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is : " , len(myName))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")

"""
#Counting register 
one_bills = int(input("Enter the total number of 1s you have : ")) * 1
five_bills = int(input("Enter the total number of 5s you have : ")) * 5
ten_bills = int(input("Enter the total number of 10s you have : ")) * 10
twenty_bills = int(input("Enter the total number of 20s you have : ")) * 20
fifty_bills = int(input("Enter the total number of 50s you have : ")) * 50
hundred_bills = int(input("Enter the total number of 100s you have : ")) * 100

total_value = one_bills + five_bills + ten_bills + twenty_bills + fifty_bills + hundred_bills
message = "Total cash in the register is :" , total_value
print(message)