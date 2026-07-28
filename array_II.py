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

## stock buy and sell problem
def max_profit(prices):
    min_profit=float('inf')
    max_profit=0
    for price in prices:
        if price<min_profit:
            min_profit=price
        elif price-min_profit>max_profit:
            max_profit=price-min_profit
    return max_profit
print("maximum profit:", max_profit([7,1,5,3,6,4]))

## rearranging array elements by sign
def rearrangment(arr):
    positives=[]
    negatives=[]
    n=len(arr)
    for i in range(n):
        if arr[i]>0:
            positives.append(arr[i])
        elif arr[i]<0:
            negatives.append(arr[i])
    result=[]
    i,j=0,0
    while i<len(positives) and j<len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i+=1
        j+=1

    return result
print("the rearranging array elements are:",rearrangment(arr=[1,2,-4,-5]) )

## next permutation
def nextPermutation(arr):
    n = len(arr)
    
    # Step 1: find pivot (first decreasing point from right)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    
    if i >= 0:  # pivot found (not fully descending)
        # Step 2: find smallest element > arr[i] from the right side
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]  # swap
    
    # Step 3: reverse the suffix after i (works even if i == -1, reverses whole array)
    arr[i+1:] = reversed(arr[i+1:])
    
    return arr
print("the next permutation array:", nextPermutation(arr=[1,2,3]) )

## longest concecutive sequence array
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:   # only start counting if num is a sequence start
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest

print("the lonest concecutive sequence is:",longestConsecutive(nums=[1,2,100,101,200,3,4,5]) )

## set matrix zero 
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_positions = []
    
    # Step 1: find all original zeros
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_positions.append((r, c))
    
    # Step 2: zero out rows and columns
    for r, c in zero_positions:
        for i in range(cols):
            matrix[r][i] = 0      # zero the whole row
        for i in range(rows):
            matrix[i][c] = 0      # zero the whole column
    
    return matrix
print("the zero matrix:", setZeroes(matrix=[[1,1,1],[1,0,1],[1,1,1]]))

## rotation of a matrix by 90 degree
def matrix_rotate(matrix):
    n= len(matrix)
    for i in range (n):
        for j in range (i+1,n):
            matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
print("the matrix after 90 degree rotation:", matrix_rotate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

## count the maximum subarray with given k
def subarraySum(arr, k):
    prefix_sum = 0
    count = 0
    sum_freq = {0: 1}   # base case: empty prefix has sum 0
    
    for num in arr:
        prefix_sum += num
        
        if (prefix_sum - k) in sum_freq:
            count += sum_freq[prefix_sum - k]
        
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    
    return count