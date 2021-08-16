def heapDesign(arr, n, i):
    maxnum = i
    left = 2 * i + 1 
    right = 2 * i + 2

    if left < n and arr[maxnum] < arr[left]:
        maxnum = left

    if right < n and arr[maxnum] < arr[right]:
        maxnum = right

    if maxnum != i:
        arr[i], arr[maxnum] = arr[maxnum], arr[i]
        heapDesign(arr, n, maxnum) 
 
def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapDesign(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapDesign(arr, i, 0)


array = [11,4,5,8,6,1,7,3,2,10,9]
print("Array Before: ", array)
heapSort(array)
n = len(array)
print("Array after: ", array)
