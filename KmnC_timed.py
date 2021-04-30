#will calculate the embedding of a Kmn graph onto Chimera for every value of m and n with a seed of 1

from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for m in range(2,200): #works for n=2 to n=10, adding extra cells step needs to be added
    for n in range(1,m+1):
        startTime = time.time()
        s = 1 #seed
        g = ((((m+3)//2)*((n+2)//2))**0.5)//1 #graph size, +0 works for n<11, after that extra cells are added
        nodes = 0
        edges = m*n #calculate how many regular edges are in the Kmn graph, before chains are added in the embedding
        c = 0 #chains
        c_edges = 0 #chain edges
        lc = 1 #longest chain
        sc = 100 #shortest chain
        Kmn = find_embedding(nx.complete_bipartite_graph(m,n), dnx.chimera_graph(g,g,4), random_seed=s)
        for i in range(0,m+n): #go through each node in the source graph to update totals. may be better done as collecting lists of each values and adding totals after, allowing averages and offsets to be found as well
            nodes += len(Kmn[i])
            if len(Kmn[i]) < sc:
                sc = len(Kmn[i])
            if len(Kmn[i]) > 1:
                c += 1
                edges += len(Kmn[i])-1
                c_edges += len(Kmn[i])-1
                if len(Kmn[i]) > lc:
                    lc = len(Kmn[i]) #lc counts how many nodes are in the longest chain, not how many chain edges there are
        t = (time.time()-startTime)
        print("m=",m,"n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",int(lc-sc),"seed=",s,"time=",t)
        print(Kmn)
print("done")
