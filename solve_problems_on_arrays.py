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

## two sum problem in an array
## the brute force approach
def two_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+ arr[j] == target:
              return True
            else:
                return False
print("two sum problem:", two_sum([2,7,11,15],9))

## the hashmap approach
def two_sum_hasmap(arr, target):
    num_dict = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
print("two sum problem:", two_sum_hasmap([2,7,11,15],9))

## the two pointer approach
def two_sum_two_pointer(arr, target):
    arr.sort()  # Sort the array first
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

print("two sum problem:", two_sum_two_pointer([2,7,11,15],9))

## sort the array of 0s, 1s and 2s
def sort_012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
print("sorted array of 0s, 1s and 2s:", sort_012([0, 1, 2, 0, 1, 2, 1, 0]))