
from queue import Queue

# Definizione di colori
bianco = "bianco"
grigio = "grigio"
nero = "nero"

def BFS(V, E ,start):
    colore = {}       # Dizionario per memorizzare il colore di ciascun vertice
    distanza = {}     # Dizionario per memorizzare la distanza di ciascun vertice
    predecessore = {}  # Dizionario per memorizzare il predecessore di ciascun vertice

    # Inizializzazione di tutti i vertici
    for v in V:
        colore[v] = bianco
        distanza[v] = float('inf')  # Inizializzato a infinito
        predecessore[v] = None

    colore[start] = grigio     # Il vertice di partenza è grigio
    distanza[start] = 0        # La distanza dal vertice di partenza a se stesso è 0

    Q = Queue()               # Creazione di una coda per gestire la visita BFS
    Q.put(start)              # Inserimento del vertice di partenza nella coda
    
