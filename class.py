#Coded in Python 
class Person: #class that acts as a blueprint for its instances
    def __init__(self, employee_position, name, annual_salary):
        self.employee_position = employee_position
        self.name = name
        self.annual_salary = annual_salary

    def display_info(self): #method of the class Person
        print(self.name, "is a", self.employee_position, " and has an annual salary of", self.annual_salary, ".")

employee1 = Person("manager", "Robert Brown", 100000) #instance or object of the class with the given parameters
employee1.display_info() #object using the method defined in the class Person

list1 = [i for i in range(10)]
list2 = []
for i in range(len(list1)):
    if(list1[i] % 2 == 0):
        list2.append("True")
    else:
        list2.append("False")


print(list1)
print(list2)

#creating a dictionary
dict1 = {1: "Rahul", 2: "Kwik"}


