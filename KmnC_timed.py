from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for m in range(2,200):
    for n in range(1,m+1):
        startTime = time.time()
        s = 1
        g = ((((m+3)//2)*((n+1)//2))**0.5)//1 #
        nodes = 0
        edges = m*n
        c = 0
        c_edges = 0
        lc = 0   #longest chain
        sc = 100 #shortest chain
        Kmn = find_embedding(nx.complete_bipartite_graph(m,n), dnx.chimera_graph(g,g,4), random_seed=s)
        for i in range(0,m+n):
            nodes += len(Kmn[i])
            if len(Kmn[i]) < sc:
                sc = len(Kmn[i])
            if len(Kmn[i]) > 1:
                c += 1
                edges += len(Kmn[i])-1
                c_edges += len(Kmn[i])-1
                if len(Kmn[i]) > lc:
                    lc = len(Kmn[i])
        t = (time.time()-startTime)
        print("m=",m,"n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",int(lc-sc),"seed=",s,"time=",t)
        print(Kmn)
print("done")
