
def Levenshtein(X, Y):
    m = len(X)
    n = len(Y)
    # Inizializza la matrice con zeri
    c = np.zeros((m+1, n+1))
    
    # Imposta i valori della prima riga e della prima colonna e della prima riga
    for i in range(0, m+1):
        c[i][0] = i
    for j in range(0, n+1):
        c[0][j] = j
    
    # Calcola la distanza di Levenshtein
    for i in range(1, m+1):
        for j in range(1, n+1):
            cancellazione = 1 + c[i-1][j]
            inserimento = 1 + c[i][j-1]
            sostituzione = c[i-1][j-1]
            
            # Se i caratteri corrispondenti sono diversi, aggiungi 1 alla sostituzione
            if X[i-1] != Y[j-1]:
                sostituzione += 1
            
            # Calcola il minimo tra cancellazione, inserimento e sostituzione
            c[i][j] = min(sostituzione, inserimento, cancellazione)
    
    # Restituisci il valore finale della distanza di Levenshtein
    return c[m][n]
