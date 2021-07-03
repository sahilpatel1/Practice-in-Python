"""

Name: Sahil Patel
Class: Online Computer Architecture
Professor: Dr. Kwak
Programming Language: Python

"""

"""
Assignment Requirements
Convert hexadecimal to decimal
Convert hexadecimal to binary
Convert decimal to hexadecimal

"""

#import the math library
import math


#function converts from binary to decimal
#requires binary number (base 2) as an argument
def binary_to_decimal(bin):
  
  string1 = str(bin) #convert the binary number as string to use it in the for loop
  decimal_value = 0

  for i in range(0,len(string1) + 1):
    decimal_value = bin % 10 * math.pow(2,i) + decimal_value
    bin = bin // 10
  print("The decimal equivalent for " + string1 + " is " + str(decimal_value))
  




#function converts from decimal to binary_to_decimal
#requires decimal number (base 10) as an argument

def decimal_to_binary(decimal):
  binary_value = []
  y = decimal

  while(y != 0):
    binary_value.append(y % 2)
    y = y // 2

  binary_value.reverse()
  print("The binary equivalent for " + str(decimal) + " is " + " ".join(str(x) for x in binary_value))



#function converts from decimal to hexadecimal
#requires decimal number (base 10) as an argument
def decimal_to_hexadecimal():
    
    decimal = int(input("Please enter a decimal value to find its hexadecimal equivalent: "))
    hexadecimal_value = []
    y = decimal

    while(y != 0):
        hexadecimal_value.append(y % 16)
        y = y // 16

    hexadecimal_value.reverse()

    for i in range(len(hexadecimal_value)):
        if(hexadecimal_value[i] == 10):
            hexadecimal_value[i] = "A"
        elif(hexadecimal_value[i] == 11):
            hexadecimal_value[i] = "B"
        elif(hexadecimal_value[i] == 12):
            hexadecimal_value[i] = "C"
        elif(hexadecimal_value[i] == 13):
            hexadecimal_value[i] = "D"
        elif(hexadecimal_value[i] == 14):
            hexadecimal_value[i] = "E"
        elif(hexadecimal_value[i] == 15):
            hexadecimal_value[i] = "F"
       

    print("The hexadecimal equivalent for " + str(decimal) + " is " + "".join(str(x) for x in hexadecimal_value))



#function converts from hexadecimal to binary
def hexadecimal_to_binary(hexadecimal):
    z = int(hexadecimal, 16)
    string1 = " "
    while z > 0:
       string1 = (str(z % 2) + string1)
       z = z >> 1 #using bitwise operator to shift value by 1
    print("The binary equivalent for hex value " + hexadecimal + " is " + string1)

    return string1


#function converts from hexadecimal to decimal
#requires a hexadecimal argument as a string
def hexadecimal_to_decimal(hexadecimal):
    print("First, converting hexadecimal to binary ...")
    x = hexadecimal_to_binary(hexadecimal)
    print("Now, converting binary to decimal ...")
    x = binary_to_decimal(int(x))
    

hexadecimal_to_binary("1000")
    
"""

Name: Sahil Patel
Class: Online Computer Architecture
Professor: Dr. Kwak
Programming Language: Python

"""


#import the math library
import math


#function converts from binary to decimal

def binary_to_decimal():
  bin = int(input("Enter a binary number (base 2) to see its decimal (base 10) equivalent : "))
  string1 = str(bin) #convert the binary number as string to use it in the for loop
  decimal_value = 0

  for i in range(0,len(string1) + 1):
    decimal_value = bin % 10 * math.pow(2,i) + decimal_value
    bin = bin // 10
  print("The decimal equivalent for " + string1 + " is " + str(decimal_value))
  
#function converts from decimal to binary
def decimal_to_binary():
  binary_value = []
  decimal = int(input("Enter a decimal number (base 10) to see its binary (base 2) equivalent : "))
  y = decimal

  while(y != 0):
    binary_value.append(y % 2)
    y = y // 2

  binary_value.reverse()
  print("The binary equivalent for " + str(decimal) + " is " + " ".join(str(x) for x in binary_value))


#function converts from decimal to hexadecimal
def decimal_to_hexadecimal():
    
    decimal = int(input("Please enter a decimal (base 10) value to find its hexadecimal (base 16) equivalent: "))
    hexadecimal_value = []
    y = decimal

    while(y != 0):
        hexadecimal_value.append(y % 16)
        y = y // 16

    hexadecimal_value.reverse()

    for i in range(len(hexadecimal_value)):
        if(hexadecimal_value[i] == 10):
            hexadecimal_value[i] = "A"
        elif(hexadecimal_value[i] == 11):
            hexadecimal_value[i] = "B"
        elif(hexadecimal_value[i] == 12):
            hexadecimal_value[i] = "C"
        elif(hexadecimal_value[i] == 13):
            hexadecimal_value[i] = "D"
        elif(hexadecimal_value[i] == 14):
            hexadecimal_value[i] = "E"
        elif(hexadecimal_value[i] == 15):
            hexadecimal_value[i] = "F"
       

    print("The hexadecimal equivalent for " + str(decimal) + " is " + "".join(str(x) for x in hexadecimal_value))



#function converts from hexadecimal to binary
def hexadecimal_to_binary():
    hexadecimal = input("Enter a hexadecimal (base 16) value to see its binary (base 2) equivalent : ")
    z = int(hexadecimal, 16)
    string1 = " "
    while z > 0:
       string1 = (str(z % 2) + string1)
       z = z >> 1 #using bitwise operator to shift value by 1
    print("The binary equivalent for hex value " + hexadecimal + " is " + string1)




#function converts from hexadecimal to decimal using an indirect approach by first converting hex to binary and then from binary to decimal
def hexadecimal_to_decimal():
    hexadecimal = input("Enter a hexadecimal (base 16) value to see its decimal (base 10) equivalent : ")
    print("To achieve this, first converting hex value into binary ...")
    z = int(hexadecimal, 16)
    string1 = " "
    while z > 0:
       string1 = (str(z % 2) + string1)
       z = z >> 1 #using bitwise operator to shift value by 1
    print("The binary equivalent for hex value " + hexadecimal + " is " + string1)

    print("Now, converting binary to decimal value ... ")
    decimal_value = 0
    bin = int(string1)
    for i in range(0,len(string1) + 1):
        decimal_value = bin % 10 * math.pow(2,i) + decimal_value
        bin = bin // 10
    print("The decimal equivalent for " + string1 + " is " + str(decimal_value))

    print()
    print("This means, the decimal equivalent for hex value " + hexadecimal + " is " + str(decimal_value))

    

"""
The script provides 5 functions that require input from user

1. binary_to_decimal()
2. decimal_to_binary()
3. decimal_to_hexadecimal()
4. hexadecimal_to_binary()
5. hexadecimal_to_decimal()

"""
#required for the assignment
#using this function, entering 45 should give 2D
decimal_to_hexadecimal() 



    
