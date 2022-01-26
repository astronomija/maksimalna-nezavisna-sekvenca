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
    for permutation in permutations:
        #print(permutation)
        curr_s, curr_c = solutionValue(permutation,adj)
        if curr_c > best_cardinality:
            best_cardinality = curr_c
            best_sequence = curr_s

    return [curr_s, curr_c]

def test(search_f, edges=10, nodes=10, draw=True):
    print('Creating graph')
    graph = createGraph(edges, nodes)

    print('Testing', search_f.__name__)
    start = time.time()
    result = search_f(graph)
    end = time.time()
    print('{} with {} nodes and {} edges took {:.3f}s'.format(search_f.__name__, nodes, edges, end - start))
    print('Final result', result[0], ' card: ', result[1])

    if draw:
        drawGraph(graph, result[0])

test(brute_force_search,8,8)