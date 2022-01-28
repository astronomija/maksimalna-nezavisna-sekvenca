import random
s = [-1] * 5
print(s)
start, end = sorted([random.randrange(5) for _ in range(2)])
print(start,end)
fixed_pos = list(range(start, end + 1))
print(fixed_pos)
import itertools

from utilis import createGraph,solutionValue
G1 = createGraph(5,5)

nodes = list(G1.nodes)
adj = G1.adj
nodes.sort()
permutations = itertools.permutations([1,2,3,4,5])

print(' nodes: ' , nodes)

parent1 = solutionValue([1,2,3,4,5],adj)
parent2 = solutionValue([2,4,5,1,3],adj)

print('p1: ' ,parent1,' p2: ',parent2)