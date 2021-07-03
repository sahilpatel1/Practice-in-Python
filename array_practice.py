#Creating a list
import string

numbers = [1,2,3,4] #A list
print(numbers)

for i in range(len(numbers)):
    print("Position " + str(i) +" - " + str(numbers[i]))

#Using the hex function

print(hex(45)) #returns 0x2d


#Using the ord function to return ASCII value


#Printing A - Z and its ascii equivalent

x = [] #Empty list to store a-z
for i in string.ascii_lowercase[:]:
    x.append(i)

ascii_equivalent = [] #Empty list to store ascii values for A-Z

for i in x:
    ascii_equivalent.append(ord(i))
    

print(x, "\n", ascii_equivalent)


#Creating classes and instances
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "."+ last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

#Class is a blueprint to create instances
emp_1 = Employee("Sahil", "Patel", 50000)
emp_2 = Employee("KHushi", "patel", 5)
emp_3 = Employee("Morris", "Patel", 50)
emp_4 = Employee("Monil", "Patel", 55)








