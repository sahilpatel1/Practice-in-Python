#program that keeps adding a stream of numbers
#until user press "q"

"""
sum = 0.0
while(True):
    user_input = (input("Enter a number to add : "))
    if(user_input != 'q'):
        sum = round(sum + float(user_input),2)
        print(f"Order total so far: {sum}")
    else:
        print("Thanks for using our calculator")
        print(f"Your Bill total is {sum}")
        break
"""


# 5! = 5 * 4 * 3 * 2 * 1 = 60

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

