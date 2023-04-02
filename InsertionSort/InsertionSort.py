def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [5, 4, 6, 10, 8, 3, 9, 7, 1, 2]
insertionSort(arr)
print("Sorted array using Insertion Sort is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
