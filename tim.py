"""
string, integer, float, boolean, string, string
"""
"""
#Opening a text file
f = open('hi.txt', 'r') 

print(f.mode)
print(f.name)

#explicitly close the file once you open it
f.close() #endup with leaks if you don't close the files



#using the context manager instead
with open('hi.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end = "")

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())



The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " , self.name)

p1 = Person("John", 56)

print(p1.name)
p1.myFunc()

#only delete the p1 properties
del p1.name

del p1.age

"""

str1 = "Koe"
str2 = "Joe"
if(len(str1) == len(str2)):
    print("Strings are same")
else:
    print("Strings are not same")

print(5 == 5)

for number in range(-4, 5):
    if(number > 0):
        print("positive")
    else:
        print("negative")


    
    


    


