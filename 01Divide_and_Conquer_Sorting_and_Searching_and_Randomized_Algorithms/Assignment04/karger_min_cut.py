import copy
import random
import numpy as np
from tqdm import tqdm

def karger(graph):
    """
    randomized contraction algorithm for the min cut problem
    """
    while len(graph) > 2:
        i = random.choice(list(graph.keys()))
        j = random.choice(graph[i])
        graph = contract(graph, i, j)
    return len(graph[i])

def contract(graph, i, j):
    """
    contract 2 nodes
    """
    neighbors = graph.pop(j)
    graph[i] += neighbors
    for k in graph:
        for l in range(len(graph[k])):
            if graph[k][l] == j:
                graph[k][l] = i
    graph[i] = list(filter(lambda x: x != i, graph[i]))
    return graph

# load txt as graph
graph = {}
with open('./kargerMinCut.txt', 'r') as f:
    for line in f:
        temp = [int(i) for i in line.split()]
        # add adjacent list
        graph[temp[0]] = temp[1:]

# run many times
n = len(graph)
iters = 800
min = n ** 2
print('Begin {} times running...'.format(iters))
tbar = tqdm(range(iters), ascii=True)
for _ in tbar:
    cuts = karger(copy.deepcopy(graph))
    if cuts < min:
        min = cuts
        tbar.set_description("Current Min Cut {}".format(min))

print('Done!')
print('Mincut is', min)
