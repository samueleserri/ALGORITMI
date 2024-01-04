bianco = "bianco"
grigio = "grigio"
nero = "nero"

def adiacenti(u, V, E):
    return [arco[1] for arco in E if arco[0] == u]

tempo = 0
colore = {}
predecessore = {}
tempo_inizio = {}
tempo_fine = {}

def DFS(V, E):
    for v in V:
        colore[v] = bianco
        predecessore[v] = None

    for u in V:
        if colore[u] == bianco:
            DFS_visiting(V, E, u)

def DFS_visiting(V, E, u):
    global tempo
    tempo += 1
    tempo_inizio[u] = tempo
    colore[u] = grigio
    for v in adiacenti(u, V, E):
        if colore[v] == bianco:
            predecessore[v] = u
            DFS_visiting(V, E, v)
    colore[u] = nero
    tempo += 1
    tempo_fine[u] = tempo
