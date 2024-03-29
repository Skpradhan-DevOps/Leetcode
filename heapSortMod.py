def max_heapify(A,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,n, largest)


def build_max_heap(A):
    n = len(A)
    for i in range((n//2)-1, -1,-1):
        max_heapify(A,n, i)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        max_heapify(A,i,0)




A=[33,35,42,10,7,8,14,19,48]
build_max_heap(A)
print(A)
