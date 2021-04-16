from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time
import sys

n = int(sys.argv[1])
if n < 2:
    raise Exception('no edges for Kn for n<2')

for s in range(1,200001):
    startTime = time.time()
    g = (n-2)//4+1 #+1 for n>2, +2 for n>140, +3 for n>160, +4 for n>170, +5 for n>175, +6 for n>180, +7 for n>185
    nodes = 0
    edges = n*(n-1)/2
    c = 0
    c_edges = 0
    lc = 0   #longest chain
    sc = 100 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.chimera_graph(g,g,4), random_seed=s)
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
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain differnce",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
