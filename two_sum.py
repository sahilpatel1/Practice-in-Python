#using brute force method which results in O(n ^ 2) time complexity

def two_sum(array, target):
    for i in range(len(array)):
        for j in range(i, len(array)):
            current_value = array[i]
            need = target - current_value
            if need == array[j]:
                return [i, j]
                
f = [1,2,4,6,10,8]                

print(two_sum(f, 14))

#results in O(n) linear time complexity when dictionary is used
def two_sum_dict(array, target):
    complements = {}
    for i in range(len(array)):
        if array[i] in complements:
            return [complements[array[i]], i] if i > complements[array[i]] else [i, complements[array[i]]]
        else:
            complements[target - array[i]] = i
print(two_sum_dict(f, 14))
