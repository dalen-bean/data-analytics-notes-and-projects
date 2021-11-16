def factorial(n):
    res = 1.0
    while n > 1:
        res*= n
        n-=1
        
    return res

n = eval(input("enter a nuber: "))
print(factorial(n))

# for i in range(100):
#     print(factorial(i))

#create a recursive function for the blackjack game
def add_nums(n):
    if n == 0:
        return 0
    return n + add_nums(n-1)  
    
print(add_nums(10))