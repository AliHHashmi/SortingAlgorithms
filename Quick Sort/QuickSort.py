def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

arr = [5, 4, 6, 10, 8, 3, 9, 7, 1, 2]
print("Sorted array using  Quick Sort is:")
quickSort(arr, 0, len(arr) - 1)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")