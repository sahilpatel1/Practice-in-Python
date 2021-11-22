#given a nested list, flatten (a single list containing all the elements from the nested list) the list.


#note that code works for both single list and nested list

def flat_list(n):
    new_list = []
    
    #iterate based on the length/number of elements in the list
    for i in range(len(n)):
        
        if(type(n[i]) == list):
            #iterate based on the length/number of elements in the nested list
            for x in range(len(n[i])):
                new_list.append(n[i][x])
        else:
            new_list.append(n[i])
            
    return new_list
    
#this is a nested list (basically an outer list containing inner lists)
l = [ [6,7], [1,3], [5,2] ]
first = [6,7,8,9]


print(flat_list(first))
