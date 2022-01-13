"""
find whether two strings are anagrams
Anagrams are words with same characters and same frequencies of characters
"""

def check_anagram(first, second):
    #check if the length of both words are same
    #if yes, then move forward or declare False
    if len(first) == len(second):
        f = sorted(first)
        s = sorted(second)
        for i,k in zip(f,s):
            if i != k:
                return False
    else:
        return False
    
    return True

string_1 = input("Enter first string : ")    
string_2 = input("Enter second string : ")

print(check_anagram(string_1, string_2))