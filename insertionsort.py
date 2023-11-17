
def insertion_sort(A): #array in input
    for j in range(1, len(A), 1): #parto dal secondo elemento (j = 1)
        key = A[j]  #prendo ogni volta l'elemento in posizione j-esima
        i = j-1 
        while i >= 0 and A[i]>key: #se l'elemento precedente è maggiore dell'elemento in posizion j-esime gli scambio
            A[i+1]=A[i]
            i -=1   #decremento i e controllo così ogni elemento precedente dell'array
            A[i+1]= key