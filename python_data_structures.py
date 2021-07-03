# Python data structures
# String, List, Tuple

# Indexing: access any item in the sequence using its index
# and it starts with 0.

x = "frog"
print(x[3])

#list
x = ['pig', 'cow', 'horse']
print(x[1])


#tuple
x = ("Kevin", "Niklos", "Jenny", "Craig")
print(x[0])

# slicing - slice out substrings, sublists, subtuples using indexes.
# [start : end + 1 : step]

x = "computer"
print(x[1:4]) #end is non-inclusive
print(x[1:6:2]) #increments by 2 like 
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])

#Adding two list
x = ["pig", 'cow']

y = x + ["tiger"]

str1 = " "

print(str1.join(y))

# string concatenating
x = "horse" + "shoe"
print("String " + x)

#tuple

z = ("Kevin", "niklas", "Jenny") + ("craig",)
print(z)

#multiply a sequence
#string
x = "bug " * 3
print(x)

#list
y = [8,5] * 3 
print(y)

#tuple
z = (3,4) * 3
print(z)

#checking membership - test whether an item is or is not in a sequence
# use "in" or "not in"
#string
x = "bug"
print("u" in x) #returns a boolean either true or false

#list
y = ["pig", "cow", "horse"]
print("cow" in y)
print("cow" not in y)

#tuple
z = ("Kevin", "niklas", "Jenny", "craig")
print("Kevin" in z)
print("Jenny" in z)

#iterating - iterating through the items in a sequence
x = [7,89,90]
for item in x:
    print(item)

#index & item
y = [7,8,3]
for index, item in enumerate(y):
    print(index, "-", item)

#number of items - count the number of items in a sequence
#string
x = "bug"
print(len(x))

#list
y = ["pig", "cow", "horse"]
print(len(y))

#TUPLE
z = ("Kevin", "niklas", "Jenny", "craig")
print(len(z))

#minimum - find the minimum item in a sequence lexicographically.
# Alpha or numeric types, but cannot mix types
# string
x = "bug"
print(min(x))

#list
y = ["pig", "cow", "horse"]
print(min(y))

#tuple
z = ("Kevin", "niklas", "Jenny", "Craig")
print(min(z))

# maximum - find the maximum item in a sequence lexicographically
# alpha or numeric types, but cannot mix types




