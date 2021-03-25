from minorminer import find_embedding
import networkx as nx
import dwave_networkx as dnx
import time

def pegasus1(g): # 4 pegasus graphs in a single layer (4 edges between cells)
    G=dnx.chimera_graph(g,g,4)
    for a in range(0,g*g*8-1,2):
        G.add_edge(a,a+1)
    return G

for n in range(223,501):
    startTime = time.time()
    s = 1
    g = (n+1)//4+5 #+0 works for pegasus_graph(g) for n>7, +1 for n>191, +3 for n>211, +4 for n>217, +5 for n>223
    nodes = 0
    edges = n*(n-1)/2
    c = 0
    c_edges = 0
    lc = 0   #longest chain
    sc = 100 #shortest chain
    Kn = find_embedding(nx.complete_graph(n), dnx.pegasus_graph(g), random_seed=s)
    for i in range(0,n):
        nodes += len(Kn[i])
        if len(Kn[i]) > 1:
            c += 1
            edges += len(Kn[i])-1
            c_edges += len(Kn[i])-1
            if len(Kn[i]) > lc:
                lc = len(Kn[i])
            if len(Kn[i]) < sc:
                sc = len(Kn[i])
    t = (time.time()-startTime)
    print("n=",n,"M=",g,"nodes=",nodes,"edges=",int(edges),"chains=",c,"chain edges=",c_edges,"longest chain=",lc,"chain difference",int(lc-sc),"seed=",s,"time=",t)
    print(Kn)
print("done")
