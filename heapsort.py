def heapify(arr, n, i):
    largest = i
    l = 2*+1
    r = 2*i+2
    if l < n and arr[largest]<arr[l]:
        largest = 1
    if r < n and arr[largest] < arr[r]:
        largest = r    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

