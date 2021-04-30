from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time
import sys

n = int(sys.argv[1]) #works for n=3 to an untested upper bound, adding extra cells step needs to be added
for s in range(1,200001): #seed
    startTime = time.time()
    g = (n+22)//12 #graph size, untested, after some point will need extra cells need to be added
    nodes = 0
    edges = n*(n-1)/2 #calculate how many regular edges are in the Kn graph, before chains are added in the embedding
    c = 0 #chains
    c_edges = 0 #chain edges
    lc = 1 #longest chain
    sc = 1000 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.pegasus_graph(g), random_seed=s)
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
    print("n=",n,"M=",g,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
