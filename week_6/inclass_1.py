#Homework 3 due in two weeks -- Web JSON APIs


#Sorting -- This is an N^2 Sort, becasue there are two for loops

def sort(lst):
    for i in range(len(lst)- 1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst
    
print(sort([3,2,1,6,5,4,8,1,5,6,4]))

# Sorting -- Insertion : You make two lists and insert the unsorted list into the sorted list N^2/2 sort.
# Sorting -- Selection Sort: Selects the smallest/largest Item and goes through and swaps them.
# Sorting -- 

#Dictionaries --

