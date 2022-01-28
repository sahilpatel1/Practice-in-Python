#using the enumerate function in Python

"""
Why use it?
You must have a counter variable to keep track of things and print on the screen
You must not forget to increment count
You must increment count after using print()
"""

seasons = ["Spring", "Summer", "Fall", "Winter"]

#pass in the start parameter with 1 to kickoff counting from that point
for count, seasons in enumerate(seasons, start =  1):
    print(count, seasons)
    
