from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

def pegasus1(g): # 4 pegasus graphs in a single layer (4 edges between cells)
    G=dnx.chimera_graph(g,g,4)
    for a in range(0,g*g*8-1,2):
        G.add_edge(a,a+1)
    return G

for n in range(190,201):
    startTime = time.time()
    s = 1
    g = (n+1)//4+3 #+0 works for pegasus1(g) for n>2, +1 for n>157, +2 for n>178, +3 for n>190
    nodes = 0
    edges = n*(n-1)/2
    chains = 0
    c_edges = 0
    lc = 0   #longest chain
    Kn = find_embedding(nx.complete_graph(n), pegasus1(g), random_seed=s)
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
