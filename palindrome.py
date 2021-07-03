#Microsoft question
#what is a palindrome
#a word, phrase, or sequence that reads the same backward as forward
#examples are rotator, madam, deed, kayak, radar, etc.

word = "keeper"
word = word.lower()  #turn the word in lowercase letters
word = word.upper() #turn the word in uppercase letters


start_position = 0 #declaring the starting position from the leftmost letter
end_position = len(word) - 1 #declaring the ending position from the rightmost letter

start_string = word 
end_string = word

loop_run = len(word)

decision = False #variable initialized with False value

while(loop_run > 0):
    
    if(start_string[start_position] == end_string[end_position]):
        start_position += 1 #check letters to the right | --->
        end_position -= 1 #check letters to the left    <--- | 
        decision = True #decision remains true as long as letters from both ends match
    else:
        decision = False #decision when letters mismatch
    loop_run -= 1 #subtract 1 to end loop after n times

if(decision == True):
    print("The word", "\"",word,"\"", "is a palindrome")
else:
    print("The word", "\"",word,"\"", "is not a  palindrome")

l1 = ['eat','sleep','repeat']

obj1 = enumerate(l1) #store it as an enumerate object in variable obj1

print("Return type", type(obj1))
for i in obj1:
    print(i)

from array import array

