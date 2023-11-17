def partition(A, p, r):
    # Choose the rightmost element as the pivot
    x = A[r]
    # Initialize the index of the smaller element
    i = p - 1
    
    # Iterate through the subarray [p, r-1]
    for j in range(p, r):
        # If the current element is less than or equal to the pivot
        if A[j] <= x:
            # Increment the index of the smaller element
            i += 1
            # Swap the current element with the element at the smaller index
            A[i], A[j] = A[j], A[i]
    
    # Swap the pivot element with the element at the next index after the smaller elements
    A[i + 1], A[r] = A[r], A[i + 1]
    # Return the index of the pivot after partitioning
    return i + 1

def quicksort(A, p, r):
    # Base case: if the subarray has one or zero elements, no sorting is needed
    if p >= r:
        return
    
    # Partition the array and get the index of the pivot
    q = partition(A, p, r)
    
    # Recursively sort the subarrays on the left and right of the pivot
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)