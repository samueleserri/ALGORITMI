
def merge(A, p, q, r):
    #p = indice di inizio, q = indice mediana, r = indice di fine
    L = A[p:q+1]  #sotto array di sinistra
    R = A[q+1:r+1] #sotto array di destra
    i, j = 0, 0
    for k in range(p, r):
        if i >= len(L) or (j < len(R) and R[j] < L[i]): #confronto l'elemento i-esimo dell'array
#di sinistra con l'elemento j-esimo dell'array di destra 
            A[k]=R[j]
            j+=1
        else:
            A[k]=L[i]
            i+=1
            
def mergesort(A, p, r):
    if p>=r:
        return
    q = (p+r)//2
    mergesort(A, p, q) #spezzo l'array in 2 parti e faccio 2 chiamate ricorsive
    mergesort(A, q+1, r)
    merge(A, p, q, r) 
