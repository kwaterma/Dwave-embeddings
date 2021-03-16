from minorminer import find_embedding
import random
import networkx as nx
import dwave_networkx as dnx


n = 8
#if n == 65:
#for n in (52,58):
#for n in range(56,61):
#for q in range(1,21):
for a in range(1,20):
    q = 3
    g = (n-2)//4+1
    nodes = 0
    edges = n*(n-1)/2
    chains = 0
    c_edges = 0
    lc = 0   #longest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.chimera_graph(g,g,4), random_seed=q)
    for i in range(0,n):
        nodes += len(Kn[i])
        if len(Kn[i]) > 1:
            chains += 1
            edges += len(Kn[i])-1
            c_edges += len(Kn[i])-1
            if len(Kn[i]) > lc:
                lc = len(Kn[i])
    if (nodes < 709) and (lc < 22):
        print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",edges,"chains=",chains,"chain edges=",c_edges,"longest chain=",lc,"seed=",q)
        print(Kn)