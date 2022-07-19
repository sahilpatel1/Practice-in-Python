#recursion is when a function calls itself and stops when a base condition is met
print()
print("The below execution is using recursion : ")
def recursive_cal(number):
    if(number < 1):
        return
    print(number)
    
    
    return recursive_cal(number - 1)
    
recursive_cal(10)

print()
print("The below execution is using a for loop : ")
def recursive_cal(number):
    for i in range(number, -1, -1):
        print(i)
        
recursive_cal(10)


def recursive_cal(number):
    if (number > 10):
        return 
    print(number)
    return recursive_cal(number + 1)
    
recursive_cal(1)

for i in range(1,11):
    print("hello world")