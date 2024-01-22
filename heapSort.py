def maxHeapify(arr,i):
    l= 2*i+1
    r= 2*i+2

    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < len(arr) and arr[r] > arr[i]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr,largest)

def build_maxHeap(arr):
    n = int((len(arr)//2)-1)
    for i in range(n, -1, -1):
        maxHeapify(arr,i)

arr = [11,6,5,20,8,2,7]
build_maxHeap(arr)
print(arr)
