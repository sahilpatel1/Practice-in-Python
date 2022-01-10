"""
Stats from the list
1. Minimum
2. Maximum
3. Mean
4. Median
5. Mode

- Sahil Patel
"""

l = [40,60,80,90,100,200,45]

def mean(n):
    avg = 0
    if type(n) == list:
        avg = sum(n) / len(n)
    else:
        return "Not a list"
    return round(avg,2)

def median(n):
    median = 0
    if type(n) == list:
        n.sort()
        if len(n) % 2 == 0:
            median = ( n[len(n) // 2] + n[ (len(n) // 2) - 1] ) / 2
        else:
            median = n[len(n) // 2]
    else:
        return "Not a list"
    return round(median, 2)

def min(n):
    minimum = 0
    if type(n) == list:
        n.sort()
        return n[0]
    return "Not a list"

def max(n):
    maximum = 0
    if type(n) == list:
        n.sort()
        return n[len(n) - 1]
    return "Not a list"

def mode(n):
    if type(n) == list:
        #using a tuple
        #tuple holding number of occurrences, the number that occurs
        max_count = (0,0)
        for num in n:
            occurences = n.count(num)
            if occurences > max_count[0]:
                max_count = (occurences, num)
            return max_count[1]
    return "Not a list"

print("The list being computed : ", l)  
print("The mean is ", mean(l))
print("The median is ", median(l))
print("The mode is ", mode(l))
print("The minimum is ", min(l))
print("The maximum is ", max(l))
