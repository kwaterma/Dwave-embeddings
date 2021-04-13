from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time
import sys

n = int(sys.argv[1])
if n < 3:
    raise Exception('no edges for Kn for n<3')

def pegasus1(g): # 4 pegasus graphs in a single layer (4 edges between cells)
    G=dnx.chimera_graph(g,g,4)
    for a in range(0,g*g*8-1,2):
        G.add_edge(a,a+1)
    return G

for s in range(1,200000):
    startTime = time.time()
    g = (n+1)//4+3 #+1 for n>140, +2 for n>160, +3 for n>170
    nodes = 0
    edges = n*(n-1)/2
    c = 0
    c_edges = 0
    lc = 0   #longest chain
    sc = 100 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), pegasus1(g), random_seed=s)
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
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
