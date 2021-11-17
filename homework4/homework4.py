import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt


url1 = 'https://api.coingecko.com/api/v3/simple/price?ids='

url2 =  '&vs_currencies='

g = nx.DiGraph() #Create a Graph
edges = []
data=[]

ids = [ 'ripple', 'bitcoin-cash', 'eos', 'litecoin', 'ethereum', 'bitcoin' ]
vs_currencies = [ 'xrp', 'bch', 'eos', 'ltc', 'eth', 'btc']

url1 = 'https://api.coingecko.com/api/v3/simple/price?ids='

url2 =  '&vs_currencies=' 

urls = []
keys = []
x = 0

#get Cardano Exchange Rates
for i in ids:
    url = url1+"cardano,"+i +url2+"ada,"+vs_currencies[x]
    request = requests.get(url)
    data = json.loads(request.text)
    # print(url)
    # print(data)
    # print( vs_currencies[x],"ada", data['cardano'][vs_currencies[x]])
    edges.append((vs_currencies[x],"ada", data['cardano'][vs_currencies[x]]))
    x+=1

#Get the first part of the URL & Save the keys to access data later 
for i in ids:
    for j in ids:
        if i == j:
            pass
        else:
        # print(i,j)
            url = url1+ i+","+ j + url2
            urls.append(url)
            keys.append((i,j))
            # print(url)
            
#Add the tickers to the end of the URL and Save the Data
x = 0   
info = []
for i in vs_currencies:
    for j in vs_currencies:
        if i == j:
            pass
        else:
            # print(urls[x]+ i+","+ j)
            request = requests.get(urls[x]+ i + "," + j)
            data = json.loads(request.text)
            # print(data)
            # print(i, j ,data[keys[x][1]][i])
            # print(j, i ,data[keys[x][0]][j])
            
            
            #Append Json data in my edges list
            edges.append((i, j ,data[keys[x][1]][i]))
            edges.append((j, i ,data[keys[x][0]][j]))
            x +=1


g.add_weighted_edges_from(edges)


results = {}

greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []

for n1, n2 in combinations(g.nodes,2):
    print("paths from", n1, "to", n2, "--------------------------------------------")
    if n2 == 'ada':
        pass
    else:
        for path in nx.all_simple_paths(g, source=n1, target=n2):
            # print(path)
            
            path_weight_to = 1
            for i in range(len(path)-1):
                path_weight_to *= g[path[i]][path[i+1]]["weight"]
                
            path.reverse()
            
            path_weight_from = 1
            for i in range(len(path)-1):
                path_weight_from *= g[path[i]][path[i+1]]["weight"]
                
            path_weight_factor = path_weight_to * path_weight_from
            print("path weight factor for path",path,":",path_weight_factor)
            
            
        if path_weight_factor > greatest_weight:
            greatest_weight = path_weight_factor
            greatest_path = path
        if path_weight_factor < lowest_weight:
            lowest_weight = path_weight_factor
            lowest_path = path

#Save Results as a dictionary 
results["greatest_path"] = greatest_path
results['greatest_weight'] = greatest_weight

results["lowest_path"] = lowest_path
results["lowest_weight"] = lowest_weight

#Dump results into a json file
json.dump(results, open("results.json", "w"))

#Log results to the console 
print("greates path", greatest_path, "at Weight: ", greatest_weight)
print("Lowest Path", lowest_path, "at Weight: ", lowest_weight)
print(0)

pos= nx.circular_layout(g)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,"weight")
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("crypto_graph.png")

#     #CARDANO PROBLEM:
#     #Use a try accept block
#     #Or use an if statement to make sure all the edges exists on the way back
    
## Save results as a JSON file


# ############## OUTPUT REQUIREMENTS ################

# Your program will run for all paths, in all currency pairs to find the highest and lowest paths weights factor (value near 1.0).  The further away from 1.0, the better the arbitrage opportunity.  

# The output will show :

# All the paths to and from each coin, the path weight, and the path weights factor 
# Keep track of the smallest and greatest path weights factor, and output them to the console, and the end of your output.

# Note: the prices are constantly changing, so your output path weights will be different than mine below.  Make sure everything is output clearly and easy to read.