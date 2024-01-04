distanza = {}
predecessore = {}

def RELAX(u, v, w):
    if distanza[u]+w < distanza[v]:
        distanza[v]=distanza[u]+w
        predecessore[v]=u

def bellman_ford(V, E, W,  s): #s nodo sorgente
    for v in V:
        distanza[v]= float('inf')
        predecessore[v]= None
    distanza[s]= 0
    for i in range(0, len(V)-1):
        for (u,v) in E:
            RELAX(u, v, W[u][v])
