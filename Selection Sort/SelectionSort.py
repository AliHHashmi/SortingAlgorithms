def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [5, 4, 6, 10, 8, 3, 9, 7, 1, 2]
selectionSort(arr, len(arr))
print("Sorted array using Selection Sort is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")