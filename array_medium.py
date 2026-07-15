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

## the hashmap approach with index return
def two_sum_hasmap(arr, target):
    num_dict = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_dict:
            return True, [num_dict[complement], i]
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

### sort the array of 0s, 1s and 2s
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

## maxmum subarray sum problem brute force approach
def max_subarray_sum(arr):
    n = len(arr)
    max_sum = float()  

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum
print("maximum subarray sum:", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))

# optimized approach using Kadane's algorithm
def max_subarray_sum_kadane(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum
print("maximum subarray sum:", max_subarray_sum_kadane([-2,1,-3,4,-1,2,1,-5,4]))