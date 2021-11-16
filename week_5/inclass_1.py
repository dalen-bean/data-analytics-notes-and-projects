# Algorithm analysis and Recurssion

#Recurssion

lst =['coke zero', 'skateboarding', 'guitar', 'baseball']

# for item in lst:
#     print(item)

# print('--------') 

def print_lst(lst, idx):
# base case
    if idx == len(idx):
        return
    print(lst[idx])
    print_lst(lst, idx + 1)
#Return statement
print_lst(lst, 0)

#logbase 2 of 8 = 3

