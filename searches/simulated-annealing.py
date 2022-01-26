import random
import  math
import time
from utilis import solutionValue,createGraph,drawGraph

def simulated_annealing(graph,iterations = 500):
    best = list(graph.nodes)
    adj = graph.adj
    best_seq, best_card = solutionValue(best,adj)
    for i in range(1,iterations):
        current = best
        #trazimo random indekse na kojima cemo uraditi zamenu
        #da bismo dobili novu permutaciju nad kojom trazimo
        #maksimalnu nezavisnu sekvencu
        a = random.randint(0,len(best) - 1)
        b = random.randint(0,len(best) - 1)

        current[a], current[b] = current[b],current[a]
        current_seq ,current_card = solutionValue(current,adj)
        if (current_card > best_card) or (1/i > random.random()):
            best = current
            best_card = current_card
            best_seq = current_seq
    return  best_seq,  best_card

graph = createGraph(5, 5)
simulated_annealing(graph)

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

test(simulated_annealing,5,5)