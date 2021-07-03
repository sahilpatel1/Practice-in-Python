mystr = "sahil is a good boy"
print(mystr[0:5])

print(len(mystr)) #returns the length of the string

string1 = "amazing"

i = [string1[0:7], string1[0:3], string1[2:5], string1[-7:-3]]
for z in range(len(i)):
    print(i[z])


print("string count is ", string1.count("amazing"))