## largest element in the array 
def largest_element(arr):
    largest = arr[0]
    for i in range (1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest  

arr = [2,89 , 00,56,78, 11, 90, 45]
print("largest element:", largest_element(arr))

## second largesr element in the array 
def sec_largest_element(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range (1,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]
    return second_largest

arr = [2,89 , 00,56,78, 11, 90, 45]
print("second largest element:", sec_largest_element(arr))

## check if the is sorted or not 
def is_sorted(arr):
    for i in range (len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr = [1,2,3,4,5,6,7,8,9]
print("is the array sorted?", is_sorted(arr))

## remove duplicates from the array
def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

arr = [1,2,2,3,4,4,5]
print("array after removing duplicates:", remove_duplicates(arr))

## maximum consecutive ones in an array 
def max_consecutive_ones():
    arr = [1, 1, 0, 1, 1, 1,0,1,1,1,1]
    max_count = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
print("maximum consecutive ones:", max_consecutive_ones())


## find the number that appears once in an array and other number appears twice
def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [1, 2, 3, 2, 1]
print("the number that appears once:", find_single_number(arr))

## longest subarray with given sum k(positive integers)
def longest_subarray_with_sum_k(arr, k):
    max_length = 0
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == k:
            max_length = max(max_length, end - start + 1)

    return max_length