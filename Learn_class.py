class employee:
    pass
    #no attributes and methods

emp_1 = employee()
emp_2 = employee()

#instance variable can be created manually
emp_1.first = "aayushi"
emp_1.last = "Johari"
emp_1.email = "aayushi@yahoo.com"
emp_1.pay = 10000

emp_2.first = "sahil"
emp_2.last = "patel"
emp_2.email = "patelsahil012@gmail.com"
emp_2.pay = 10000

print(emp_1.email)
print(emp_2.email)

import keyword

print(keyword.kwlist)
#this will get you the list of all keywords in python.

print(keyword.iskeyword('alkjsdfhlakjdshfalkdsjf'))
#this will return true, if the mentioned name is a keyword


import math

def areaCircle(radius):
    return math.pi * radius * radius

radiusValue = 2
circleArea = areaCircle(radiusValue)

print("Area of the circle with %f units radius is %f units" %(radiusValue, circleArea))

def min():
    list_1 = [5,6,71,45,45]
    max = list_1[0]
    min = list_1[0]
    midpoint = 0
    mode = list_1[0]
    counter = 0
    for i in list_1:
        if(i < min):
            min = i
        elif(i > min):
            max = i
    #finding the median from the list
    #getting the length of the list
    length = len(list_1)
    if(length % 2 == 0):
        midpoint = (list_1[length // 2] + list_1[(length // 2) - 1]) / 2
    elif(length % 2 != 0):
        midpoint = (list_1[length // 2]) 
   

    
    
    


    print("The mode of the list ", mode)
    print("The median of the list is " , midpoint)
    print("The minimum number from the list is ", min) #returns the minimum number from the list
    print("The maximum number from the list is ", max) #returns the maximum number from the list

min()