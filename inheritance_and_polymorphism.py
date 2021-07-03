class Human:

    def __init__(self, age, name):
        self.name = name
        self.age = age
    
class Dancer:

    def __init__(self, style):
        self.style = style
    

#inheriting from two different class 
class Student(Human, Dancer):
    def __init__(self, age, name, style):
        Human.__init__(self, age, name) #only useful in one inheritance
        Dancer.__init__(self, style)
    pass

John = Student(20, 'John', 'HipHop')

print("My name is ", John.name, ". I am ", John.age, "years old and enjoy ", John.style)


