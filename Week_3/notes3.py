import numpy as np

 
prices = [float(x) for x in open('Week_3/amzn.txt').readlines()]


profit = 0.0
i = 0
days = 5
buy = 0
    
for p in prices:
    if i >= days:
        avg = np.mean(prices[i-days:i])
        
        if p < avg * .95 and buy == 0:
            buy = p
            print('buying', p) 
        elif p > avg *1.05 and buy != 0:
            profit += p - buy 
            buy = 0
            print('selling at: ', p)
            
        else:
            pass
        
    i += 1

print('total profit: ', profit)
print('returns:', profit/prices[0])
    
