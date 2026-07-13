## selection sort
##The Selection Sort algorithm features atime complexity of O(n²) across all operational scenarios 
# an auxiliary space complexity of O(1).
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print("the sorted array is :", selection_sort([89, 0, 45, 23, 12, 78, 89, 34, 56, 12]))


##bubble sort
## The worst-case and average-case time complexity of bubble sort is O(n²) , its best-case time complexity is O(n) (when optimized)
# its space complexity is O(1)
def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("the sorted array is :", bubble_sort([64, 25, 12, 22, 11]))

##insertion sort
##Insertion sort has a worst-case and average-case time complexity of O(n²), a best-case time complexity of O(n), 
# an auxiliary space complexity of O(1)
def insertion_sort(arr):
    n=len(arr)
    for i in range (n):
        j=i
        while arr[j] < arr[j-1] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
print("the sorted array is :", insertion_sort([64, 25, 12, 22, 11]))

## merge sort
## Merge sort has a time complexity of O(n log n) in all cases
# a space complexity of O(n).

def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0

        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1

        while i<len(left_half):
            arr[k]=left_half[i]
            i +=1
            k +=1

        while j<len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1
    return arr
print("the sorted array is :", merge_sort([64, 25, 12, 22, 11, 90, 34, 56, 12]))

## quick sort
## Quick sort has a worst-case time complexity of O(n²), an average-case time complexity of O(n log n), and a best-case time complexity of O(n log n).
# Its space complexity is O(log n) due to the recursive nature of the algorithm.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
print("the sorted array is :", quick_sort([64, 25, 12, 22, 11]))


