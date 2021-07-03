#Define the class
class Student:
    pass #It does nothing but it is a statement that accepts the class definition

#Here's the constructor function definition
#The self stands in for the object that is being created

    def __init__(self, newname, newage, newgpa):
        self.name = newname
        self.age = newage
        self.gpa = newgpa
        print("Running the constructor")

    #Another class function. Simply prints out a message
    def springBreak(self):
        print("This function will not be specific about all the things that occur during spring break .. Be non sensible.")

        print("By the way, since we\'re discussing spring break, I won't mention my name, but I'm nly ", self.age, " years old")

#Calling the constructor of Student to
# make a Student object and save it like usual
mystudent = Student("Monty", 20, 2.0)
print("Name: ", mystudent.name)

#Call out a function from the object by putting a call 
# statement to the right of the dot

mystudent.springBreak()

#Each object has its own memory, data, ability to call its defined functions.
# They are independent of each other

mystudent2 = Student("Python", 18, 2.7)
print("Name in the 2nd object", mystudent2.name)
print("Name in the 1st object: ", mystudent.name)

class Player:
    
    def __init__(self, newname):
        self.name = newname
        self.hp = 80 #player begins with full hp?
        print("A new player approaches ... named", self.name, " with ", self.hp, " health points\n")

    #Add a function to use the powerup
    def getPowerup(self, newpowerup):
        self.hp += newpowerup.hp
        print(self.name, " receives ", newpowerup.hp, " from a powerup")
        print("Health of " , self.name , " is " , self.hp)
    
class Powerup:
    def __init__(self, hp):
        #The constructor function accepts 1 parameter
        # to be the amount of health points the player gets
        #when using the powerup
        self.hp = hp

p1 = Player("Monty")
pu = Powerup(5)

#Call the getPowerup function on the player object
# passing in the powerup object to be used by the 
# player to update their status in a beneficial way
p1.getPowerup(pu)

