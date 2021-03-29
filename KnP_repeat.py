from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time
import sys

n = int(sys.argv[1])
if n < 7:
    raise Exception('no edges for Kn for n<7')

for s in range(1,200001):
    startTime = time.time()
    g = (n+1)//4 #(works for pegasus_graph(g) for n>6
    nodes = 0
    edges = n*(n-1)/2
    c = 0
    c_edges = 0
    lc = 0   #longest chain
    sc = 100 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.pegasus_graph(g), random_seed=s)
    for i in range(0,n):
        nodes += len(Kn[i])
        if len(Kn[i]) < sc:
                sc = len(Kn[i])
        if len(Kn[i]) > 1:
            c += 1
            edges += len(Kn[i])-1
            c_edges += len(Kn[i])-1
            if len(Kn[i]) > lc:
                lc = len(Kn[i])
    t = (time.time()-startTime)
    print("n=",n,"M=",g,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
