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

def simulated_annealing_sort(graph, iterations = 600):
    best = list(graph.nodes)
    #sortiramo po stepenu cvora,tj njegovom broju grana
    best.sort(key=lambda x: graph.degree[x])

    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        a = random.randint(0, len(best) - 1)
        b = random.randint(0, len(best) - 1)
        current[a], current[b] = current[b], current[a]
        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c

