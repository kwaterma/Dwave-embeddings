from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

for m in range(2,24):
    for n in range(1,m+1):
        print(m,n,g)
        startTime = time.time()
        s = 1
        g = int((((m//2)*(n//4))^^0.5)//2)
        nodes = 0
        edges = n*(n-1)/2
        c = 0
        c_edges = 0
        lc = 0   #longest chain
        sc = 100 #shortest chain
        Kn = find_embedding(nx.complete_bipartite_graph(m,n), dnx.chimera_graph(g,g,4), random_seed=s)
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
        print("m=",m,"n=",n,"cells=",g**2,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference=",int(lc-sc),"seed=",s,"time=",t)
        print(Kn)
print("done")
