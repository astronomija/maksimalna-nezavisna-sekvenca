import networkx as nx
import numpy as np
import time
from utilis import createGraph, drawGraph, solutionValue
import searches.simulated_annealing as an
import searches.brute_force as bf
import searches.genetic as gen

import searches.genetic as gen
import matplotlib.pyplot as plt

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

#test(bf.brute_force_search, edges=10, nodes=10)

def compare(f1,f2,edges=10,nodes=10,iterations=100):
    print('Comparing {} and {}'.format(f1.__name__,f2.__name__))
    results = {
        f1.__name__: 0,
        f2.__name__:0,
        'equal' : 0
    }

    #poredimo u koliko iteracija su algoritmi dobili istu sekvencu
    #a u koliko je prvi odnstno drugi dao bolje resenje
    for i in range(0,iterations):
        graph = createGraph(edges,nodes)
        res1 = f1(graph)[1]
        res2 = f2(graph)[1]

        if res1>res2:
            results[f1.__name__] += 1
        elif res2 >res1:
            results[f2.__name__] += 1
        else:
            results['equal'] += 1
    print(results)

compare(gen.genetic_search, an.simulated_annealing_sort)