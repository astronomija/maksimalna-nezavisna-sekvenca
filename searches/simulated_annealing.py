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

        current[a], current[b] = current[b], current[a]
        current_seq ,current_card = solutionValue(current,adj)
        if (current_card > best_card) or (1/i > random.random()):
            best = current
            best_card = current_card
            best_seq = current_seq
    return  best_seq,  best_card

def simulated_annealing_slow(graph, iterations = 500):
    best = list(graph.nodes)
    #bolje uzeti cvor sa manjim stepenom na pocetku zato sto je veca sansa da nece moci u niz na kraju
    # best.sort(key=lambda x: graph.degree[x])
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        a = random.randint(0, len(best) - 1)
        b = random.randint(0, len(best) - 1)
        current[a], current[b] = current[b], current[a]
        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / math.sqrt(i) > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
    return best_s, best_c

def simulated_annealing_sort(graph, iterations = 500):
    best = list(graph.nodes)
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

#varijanta simuliranog kaljenja u kome menjamo random n/2 sekvencu cvorova u permutaciji
#dobijamo novu permutaciju i izracunavamo vrednost za nju
def simulated_annealing_variation(graph, iterations = 500):
    #vise random izmena, ali moguce je zameniti n/2 cvorova
    best = list(graph.nodes)
    best_s, best_c = solutionValue(best, graph.adj)
    for i in range(1,iterations):
        current = best
        pom = current.copy()
        n = random.randint(0, math.floor((len(best) - 1)/2))
        indexes = []
        values = []
        for _ in range(n):
            r=random.randint(0, len(best) - 1)
            indexes.append(r)
            values.append(current[r])
        random.shuffle(indexes)
        random.shuffle(values)

        for j in range(n):
            index = indexes[j]
            current[index] = values[j]

        current_s, current_c = solutionValue(current,graph.adj)
        if (current_c > best_c) or (1 / i > random.random()):
            best = current
            best_c = current_c
            best_s = current_s
        else:
            current = pom
    return best_s, best_c