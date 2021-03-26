from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for n in range(155,501):
    startTime = time.time()
    s = 1
    g = (n-2)//4+1 #+1 works for n<155
    if n > 155: #tried to correct for more cells needed for larger calculations
        g += (n-137)//8
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
    print("n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
