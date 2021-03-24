from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for n in range(172,201):
    startTime = time.time()
    s = 1
    g = (n-2)//4+4 #+1 works for n>1, +2 for n>155, +3 for n>157, +4 for n>172
    nodes = 0
    edges = n*(n-1)/2
    chains = 0
    c_edges = 0
    lc = 0   #longest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.chimera_graph(g,g,4), random_seed=s)
    for i in range(0,n):
        nodes += len(Kn[i])
        if len(Kn[i]) > 1:
            chains += 1
            edges += len(Kn[i])-1
            c_edges += len(Kn[i])-1
            if len(Kn[i]) > lc:
                lc = len(Kn[i])
    t = (time.time()-startTime)
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",chains,"chain edges=",c_edges,"longest chain=",lc,"seed=",s,"time=",t)
    print(Kn)
print("done")
