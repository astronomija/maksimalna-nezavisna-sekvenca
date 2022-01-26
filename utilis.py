import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def createGraph(edges =10,nodes = 10):
    if nodes <= 1:
        raise  Exception('2 or more nodes required')

    graph = nx.Graph()
    while len(graph.edges) < edges:
        nodeA = random.randint(1,nodes)
        nodeB = random.randint(1,nodes)
        while nodeA == nodeB:
            nodeB = random.randint(1,nodes)
        if nodeA > nodeB:
            nodeA, nodeB = nodeB,nodeA
        if(nodeA,nodeB) in graph.edges:
            continue
        graph.add_edge(nodeA,nodeB)
    return graph

G = createGraph()

#iscrtava graf i boji cvorove koji su ukljuceni u rezultat,tj koji
#predstavljaju maksimalnu nezavisnu sekvencu u crveno ,dok su ostali plave boje
def drawGraph(graph,result):
    plt.figure(figsize=(8,8))
    nx.draw(graph,with_labels=True,node_color = [('red' if x in result else 'blue')
                                                 for x in graph.nodes])
    plt.show()


def solutionValue(iteration,adj):
    solution = []

    for v in iteration:
        #proveravamo da li je cvor vec u resenju i ako jeste preskacemo ga
        if v in solution:
            continue
        #adj je vektor suseda za svaki cvor
        #ako cvor nema susede preskacemo ga

        if adj[v] is 0:
            continue
        #ako neki cvor iz resenja za suseda ima neki od cvorova koji su susedi i cvoru koji proveravamo
        #i taj svor preskacemo
        if any(u in solution for u in adj[v]):
            continue
        #ako postoji cvor koji nije susedan ni sa jednim drugim cvorom iz resenja dodajemo ga u resenje
        if any((x not in solution) and all(u not in adj[y] for y in solution) for u in adj[v] for x in adj[u]):
            solution.append(v)
    #konacno gledamo duzinu dobijene sekvence
    cardinality = len(solution)

    return  solution,cardinality

