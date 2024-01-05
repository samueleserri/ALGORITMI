def LCS(X, Y):
     # Creiamo una matrice (m+1) x (n+1) inizializzata con zeri
    n = len(X)
    m = len(Y)
    c = np.zeros((m+1, n+1))
    # Riempimento della matrice utilizzando l'algoritmo LCS
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Se i caratteri correnti sono uguali, incrementiamo la lunghezza della sottosequenza comune
            if Y[i-1] == X[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
            # Altrimenti, prendiamo il massimo tra le sottosequenze comuni precedentemente calcolate
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    # Il valore nell'angolo in basso a destra della matrice rappresenta la lunghezza della LCS
    return c[m][n]
