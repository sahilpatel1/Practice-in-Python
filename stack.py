#implementing a stack using python

"""
what is stack?
A same type container where the insertion and deletion
occurs only at one end. 

Common operations with stack are :
Push(x) where x is the element to be inserted 
Pop() removes the topmost elmeent from the stack.
Peek() prints the topmost elements from the stack.
size() prints the total number of elements in the stack.
printstack() prints the elements one by one from top to bottom. No elements are removed or popped.
"""

"""
Stack is LIFO
"""
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item = ' '):
        """
        Push the elements at the last index
        return : None
        """
        self.items.append(item)
    
    def pop(self):
        "This will remove last item and returns None"
        return self.items.pop()
        
    
    def peek(self):
        if(self.items):
            return self.items[-1]
        else:
            return None

    def size(self):
        if(self.items):
            return len(self.items)
        else:
            return None
        
    def isempty(self):
        """
        tells whether the stack is empty or not
        return : Bool value
        """
        if(self.items == []):
            return True
        else:
            return False
    
    def printstack(self):
        """returns None if no elements in the list or prints the elements from top to bottom"""
        if(self.isempty()):
            return None
        else:
            size = len(self.items)
            while(size > 0):
                print(self.items[size - 1])
                size -= 1

    def index(self, x):
        print("Element", x,  "is at index position",  self.items.index(x), "in the stack")

    def viewstack(self):
        """ prints the current list or the stack """
        print(self.items)

    def clear(self):
        self.items = []
    

if __name__ == "__main__":
    stack = Stack() #object of class Stack
    stack.push("2") #insert 2
    stack.push("3") #insert 3
    stack.push("4") # insert 4
    stack.push("5") # insert 5
    stack.printstack() #print elements from top to bottom or the last one inserted gets printed first and so on
    if(stack.isempty()):
        print("The stack is currently empty : ")
        stack.viewstack()
    else:
        print("The stack has ", stack.size(), " elements : ")
        stack.viewstack()
        stack.clear()
        stack.viewstack()
