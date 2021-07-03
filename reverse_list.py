#Reverse a list in python

k = [x for x in range(1,10)]

def reverse_list(list):
    print("The original list : ", list)
    length = len(list) // 2 #number of times elements will be swapped in the list
    start = length - 1
    end = length * -1 #turn negative to access elements from the end of the list
    while(start >= 0 and end != 0):
        temp = list[start]
        list[start] = list[end]
        list[end] = temp
        start = start - 1
        end = end + 1
    print("The reversed list: ", list)


reverse_list(k)
