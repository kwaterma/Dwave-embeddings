#will calculate the embedding of a Kn graph onto single layer Pegasus for a single value of n and every value of s
#can be used to find the best possible version of the embedding if run to a high enough seed

from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time
import sys

def pegasus1(g): #creates a single layer of pegasus graphs (4 edges between cells)
    G=dnx.chimera_graph(g,g,4)
    for a in range(0,g*g*8-1,2):
        G.add_edge(a,a+1)
    return G

n = int(sys.argv[1]) #get n from the command line, works for n=3 to n=140 (partially untested), adding extra cells step needs to be refined
for s in range(1,200000): #seed
    startTime = time.time()
    g = (n+1)//4 #graph size, +0 works for n<140, after that extra cells are added
    if n > 140: #somewhat corrects extra cells needed for larger calculations
        g += (n-131)//9
    nodes = 0
    edges = n*(n-1)/2 #calculate how many regular edges are in the Kn graph, before chains are added in the embedding
    c = 0 #chains
    c_edges = 0 #chain edges
    lc = 1 #longest chain
    sc = 1000 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), pegasus1(g), random_seed=s)
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
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
