#will calculate the embedding of a Kn graph onto Chimera for every value of n with a seed of 1
#can be used to estimate run time for KnC_repeat with a single value of n and every value of s

from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for n in range(2,501): #works for n=3 to n=224, adding extra cells step needs to be refined
    startTime = time.time()
    s = 1 #seed
    g = (n-2)//4+1 #graph size, +1 works for n<155, after that extra cells are added
    if n > 155: #somewhat corrects extra cells needed for larger calculations
        g += (n-137)//8
    nodes = 0
    edges = n*(n-1)/2 #calculate how many regular edges are in the Kn graph, before chains are added in the embedding
    c = 0 #chains
    c_edges = 0 #chain edges
    lc = 1 #longest chain
    sc = 100 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.chimera_graph(g,g,4), random_seed=s)
    for i in range(0,n): #go through each node in the source graph to update totals. may be better done as collecting lists of each values and adding totals after, allowing averages and offsets to be found as well
        nodes += len(Kn[i])
        if len(Kn[i]) < sc:
            sc = len(Kn[i])
        if len(Kn[i]) > 1:
            c += 1
            edges += len(Kn[i])-1
            c_edges += len(Kn[i])-1
            if len(Kn[i]) > lc:
                lc = len(Kn[i]) #lc counts how many nodes are in the longest chain, not how many chain edges there are
    t = (time.time()-startTime)
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
