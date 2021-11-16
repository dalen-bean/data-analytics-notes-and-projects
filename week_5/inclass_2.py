#Reccursion Review
lst = ['diet coke', 'hiking', 'rugby', 'pizza', 'fijitas']

def print_item(lst, idx):

    if idx>= len(lst):
        return
    
    print(lst[idx])
    
    print_item(lst, idx + 1)
    
print_item(lst, 0)
print("------------")
#Write the fibonacci number formula Fn = Fn-1 +Fn-2...



def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return n
    else:
        sums = [0,1]
        for i in range(2, n + 1):
            sums.append(sums[i-1]+ sums[i-2])
        return sums[-1]
            
print(fibonacci(8))

def fib(n):
    if n == 0 or n== 1:
        return n
    return((fib(n-1) + fib(n-2)))
    
print(fib(8))

def sort(lst):
    for i in range(len(lst)- 1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
print(sort([3,2,1,6,5,4,8,1,5,6,4]))
    
    