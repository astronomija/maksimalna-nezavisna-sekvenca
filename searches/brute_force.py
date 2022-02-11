import numpy as np
import random
import time
from matplotlib import pyplot as plt
import itertools
from utilis import createGraph,drawGraph,solutionValue

def brute_force_search(graph):
    nodes = list(graph.nodes)
    #mapa suseda svih cvorova u grafu
    adj = graph.adj
    nodes.sort()
    permutations = itertools.permutations(nodes)
    best_cardinality = 0
    best_sequence = []
    bestPermutation = []
    #isprobava svaku mogucu permutaciju cvorova
    for permutation in permutations:
        #print(permutation)
        curr_s, curr_c = solutionValue(permutation,adj)
        if curr_c > best_cardinality:
            best_cardinality = curr_c
            best_sequence = curr_s
            bestPermutation = permutation
    print(bestPermutation)
    return [best_sequence, best_cardinality]
