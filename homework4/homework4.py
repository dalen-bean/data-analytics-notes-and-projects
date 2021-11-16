import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt

# Get exchange rates from coingecko.com  (if edge == none skip that cycle)
# Use later 'cardano', 'ada',  

ids = [ 'ripple', 'bitcoin-cash', 'eos', 'litecoin', 'ethereum', 'bitcoin' ]
vs_currencies = [ 'xrp', 'bch', 'eos', 'ltc', 'eth', 'btc' ]

crypto = {'ripple': 'xrp', 
'bitcoin-cash': 'bch',
'eos': 'eos', 
'litecoin': 'ltc',
'ethereum': 'eth',
'bitcoin': 'btc'}

#Save the ID:s and tickers as Key value pairs

url1 = 'https://api.coingecko.com/api/v3/simple/price?ids='

url2 =  '&vs_currencies='

g = nx.DiGraph() #Create a Graph
edges = []
data=[]
key1 = ids
i=0
urls = [] # First Half
urls2 = [] # second Half

#Get the first half of the url
for c1, c2 in permutations(crypto, 2):
    url = url1+c1+","+c2
    urls.append(url)
 
#Get the second half of the url   
for c3, c4 in permutations(vs_currencies,2):
    url = url2+c3+","+c4
    urls2.append(url)
    # print(url)

x = 0
# Combine the 2 urls and save the data   
while i < len(urls):
    url = urls[i]+urls2[i]
    print(url)
    request = requests.get(url)
    data = json.loads(request.text)
    print(ids[x+1],vs_currencies[x+1],ids[x],vs_currencies[x], data)
    i += 1
    if x >= 5:
        x =0
    else:
        x += 1
    
    
# for c1, c2 in combinations(ids,2):
#     for c3, c4 in permutations(vs_currencies,2):
#         url = url1+c1+","+c2+url2+c3+","+c4
#         print(url)
        # request = requests.get(url)
        # data = json.loads(request.text)
        # edges.append((c4, c3, data[c1][c4]))
        # edges.append((c3,c4,data[c2][c3]))
        
        # data should look like this ['ett','btc', 0.03092437]
        # print(c4, c3, data[c1][c4])
        # print(c3,c4,data[c2][c3])
        # print(edges)
# print(edges)

input("Hit enter to continue:")

g.add_weighted_edges_from(edges)
# g.add_weighted_edges_from((['ett','btc', 0.03092437]), ('btc', 'eth', 32.34243)) #Add edges to the graph


greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []

for n1, n2 in combinations(g.nodes,2):
    print("paths from", n1, "to", n2, "--------------------------------------------")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path)
        
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
    
print("greates path", greatest_path, "at Weight: ", greatest_weight)
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




# Calculate the weight(currency exchange rate) of an edge
# g[‘btc’][‘eth’]['weight'] # returns 32.34243

# g[‘eth’][‘btc’][‘weight’] # returns 0.0309095

# g.nodes # list of all nodes

# nx.all_simple_paths(g,'btc','eth')#shows all the paths to and from bitcoin and etherium

# To calculate the weight of the path multiply the weights of all the edges in the path:

# g[‘btc’][‘xrp’][‘weight’] * g[‘xrp’][‘eth’][‘weight’] # 32.5358904
 
# Then calculate the weight of the reverse path.  For the example above, the reverse path would be [‘eth’, ‘xrp’, ‘btc’].  The path weight is calculated as follows:
 
# g[‘eth’][‘xrp’][‘weight’] * g[‘xrp’][‘btc’][‘weight’] # 0.03078474

# Now that you have the weight of the path to and from node1 and node2, multiply them both:
 
# 32.5358904 * 0.03078474 * = 1.0016089266324961

# When the path to and from the nodes are in equilibrium, the factor of both path weights, will be exactly 1.0.  

# As you can see in this example, the paths are in dis-equilibrium.  Meaning if you spent 1 bitcoin, and then bought ripple, then ethereum, then ripple, then bitcoin, you would own 1.0016~ bitcoin.  An increase of 0.0016 bitcoin is equivalent to $90.27 (as of the time I wrote this assignment).





# ############## OUTPUT REQUIREMENTS ################

# Your program will run for all paths, in all currency pairs to find the highest and lowest paths weights factor (value near 1.0).  The further away from 1.0, the better the arbitrage opportunity.  

# The output will show :

# All the paths to and from each coin, the path weight, and the path weights factor 
# Keep track of the smallest and greatest path weights factor, and output them to the console, and the end of your output.

# Note: the prices are constantly changing, so your output path weights will be different than mine below.  Make sure everything is output clearly and easy to read.