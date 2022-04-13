# written by sahil patel
#program to get table of n 

list = [x for x in range(1,11)] #create a list to multiply n parameter passed to function table(n)

def table(n):
    k = []
    for i in range(len(list)):
        k.append(list[i] * n)
        
    print("Table of", n, ":")
    for i in range(len(list)):
        print(n, " * ", list[i], " = ", k[i])
    print()
    print()
    
#for example
#printing a multiplication table of 65
table(65)
