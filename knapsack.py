def knapsack(pesi, valori, C):  # C = capacità zaino
    n = len(pesi)
    M = np.zeros((n + 1, C + 1))
    
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if pesi[i - 1] <= j:
                M[i][j] = max(M[i - 1][j], valori[i - 1] + M[i - 1][j - pesi[i - 1]])
            else:
                M[i][j] = M[i - 1][j]

    return M
