#Python has an order of operations that begins with ** operator, *, /, //, and %.
'''
** - Power operator
%  - Modulus/remainder
// - Integer division / floored quotient
/  - Division with accurate quotient
*  - Multiplication
-  - Subtraction
+  - Addition
'''

print(7 * 100570)

'''
The three common data types are :
Integers = -2,-1,-3,9,0 (whole numbers)
Floating-point numbers = 3.4, 2.4, 2.0 (decimal numbers)
Strings = "a", "apple", "abercrombie & finch"
'''

# String concatenation occurs when two strings are added (+) together

print("Alice" + "Bob")

# String replication using the * operator

print("Alice Bob " * 3)

"""
Naming Variables using the following rules:
1. It can be only one word
2. It can use only letters, numbers, and the underscore (_) character.
3. It can't begin with a number.
"""

#Asking for a name
print("Hello world!")
print("What is your name?")
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is : ")
print(len(myName))


print("What is your age?") #ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

# The input() function takes an input from the user
# Anything that ends with "()" is a function
print(len("My very energetic monster just scarfed nachos."))
print(str(20))
print("I am " + str(20) + " years old.")
print("I have eaten " + str(99) + " burritos")

'''
Ex: 1 Python Basics
1 *,-,/,+ are operators and 'hello' and -88.8 are values.
2 spam is a variable and 'spam' is a string
3 Float, String, Integers
4 Expression are numbers combined with operators. They end up in a single value once the evaluation is done.
5 An expression is an evaluation, whereas a statement consists of a variable that holds a value
6 The variable bacon has a value of 21
7 The first expression evaluates to spamspamspam and the other will be spamspamspam
8 Python doesn't allow variable names to begin with numbers
9 int(), str(), float()
10 The expression has 99 as an integer and requires a conversion using the str() method

Extra: The round() function returns a floating number rounded to a precise decimal place as mentioned.
For example,
x = round(6.79, 1) will result in x = 6.8
'''







