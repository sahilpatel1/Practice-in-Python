def sum(x,y):
    return x + y

def multiply(x,y):
    return x * y

def subtract(x,y):
    if(x > y):
        return x - y
    elif(y > x):
        return y - x
    else:
        return 0

def divide(x,y):
    if(x < y):
        return y // x
    else:
        return x // y
