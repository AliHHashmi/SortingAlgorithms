def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

arr = [5, 4, 6, 10, 8, 3, 9, 7, 1, 2]
bubbleSort(arr)
print("Sorted array using Bubble Sort is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
