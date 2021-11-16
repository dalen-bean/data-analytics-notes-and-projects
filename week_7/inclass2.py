#Queue: Fifo Work Flow pop(0)--> takes off the first number

#Stack: Lifo Work Flow pop() --> takes off the Last number of a list
import numpy as np

prices = [float(x) for x in open("/home/ubuntu/environment/Week_3/appl.txt").readlines()]

#print(prices)

days = 5
buy =0
profit = 0.0
for i in range(len(prices)):
    if i > days:
        p = prices[i]
        avg = np.mean(prices[i-days:i])
        
        if p < avg* 0.95 and buy == 0:
            buy = p
        elif p > avg * 1.05 and buy != 0:
            profit += p- buy
            buy = 0
            
        else:
            pass #do nothing today
        
print("profit: ", profit)
print("return: ", round(100 * profit/prices[0], 2), "%")

#Mean Reversion with a Queue
f = open("/home/ubuntu/environment/Week_3/appl.txt", "r")

prices = []
line = f.readline()
#print("line: ", line)
buy = 0
profit = 0.0
first_buy = 0
while line:
    prices.append(float(line))
    line = f.readline()
    
    if len(prices) == 6:
        avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
        #print(avg)
        if prices[5] < avg * 0.95 and buy == 0:
            buy = prices[5]
            if first_buy == 0:
                first_buy = buy
        elif prices[5] > avg * 1.05 and buy != 0:
            profit += prices[5]- buy
            buy = 0
        else:
            pass #do nothing today
            
        prices.pop(0)
                
print("profit: ", profit)
print("return: ", round(100 * profit/prices[0], 2), "%")        
print(first_buy)  