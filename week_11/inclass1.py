import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt


rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

g = nx.DiGraph()
edges = []
i = 0
for c1 in currencies:
    j = 0
    for c2 in currencies:
        if c1 != c2:
            edges.append((c1, c2, rates[i][j]))
            print("adding edge: ", c1, c2, rates[i][j])
        j +=1
    i += 1
g.add_weighted_edges_from(edges) 
# print(g.info())

print(g.nodes)
for n1, n2 in permutations(g.nodes,2):
    
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        high = 0
        x = 0
        weight = 0
        if n1 == currencies[x] and n2 ==currencies[x+1]:
            print(path)
            path_weight1 = 1
            path_weight2 = path_weight1
            for i in range(len(path)-1):
                path_weight1 *= g[path[i]][path[i+1]]['weight']
                path_weight2 *= g[path[i+1]][path[i]]['weight']
            x += 1
            print("weight", path_weight1*path_weight2)
                
    # for path in nx.all_simple_paths(g, source=n2, target=n1):
    #     x= 0
    #     if n2 == currencies[x+1] and n1 ==currencies[x]:
    #         print(path)
    #         path_weight2 = 1
    #         for i in range(len(path)-1):
    #             path_weight2 *= g[path[i+1]][path[i]]['weight']
    #         print("path_weight2", path_weight2)
    #         highpathweight = path_weight1 * path_weight2
    #         x +=1
    # print("Path Weight: ", highpathweight)
    
    #Equilibrium should be 1.04
