## Search in a sorted 2D matrix
# brute force approach
def search_in_2D_matrix(mat,t):
    for i in mat:
        for j in i:
            if j==t:
                return True
    return False
print ("the target element in the matrix is:", search_in_2D_matrix(mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ],t=8))

#optimal solution
def searchMatrix(mat, target):
    if not mat or not mat[0]:
        return False

    n, m = len(mat), len(mat[0])
    low, high = 0, n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row, col = mid // m, mid % m
        val = mat[row][col]

        if val == target:
            return True
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 8))
print(searchMatrix([[1,2,4],[6,7,8],[9,10,34]], 78))


##Implement Pow(x,n) | X raised to the power N
# by Python's built-in ** operator
def pow(x,n):
    a=x**n
    return a
print("the answer is:", pow(x=2.0000,n=10))

#brute force approach 
def mypow(x,n):
    if n<0:
        x=1/x
        n=-n
    result=1
    for i in range(n):
        result *=x
    return result
print("the answer is:", mypow(x=2.0000,n=10))

#optimal approach
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:       # n is odd
            result *= x
            n -= 1
        else:                # n is even
            x *= x
            n //= 2

    return result

print(myPow(2.0, 10))
print(myPow(2.0, -2))   

## Find the Majority Element that occurs more than N/2 times
## brute force approach
def majority_element(nums):
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[j]==nums[i]:
                count+=1
        if count>n//2:
            return nums[i]
    return -1
print ("the that occurs more than N/2 times is:", majority_element(nums=[7, 0, 0, 1, 7, 7, 2, 7, 7]))

## Better: Hashmap (O(n) time, O(n) space):
def majorityElement_hashmap(nums):
    count = {}
    n = len(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n // 2:
            return num
    return -1
print ("the that occurs more than N/2 times is:", majority_element(nums=[7, 0, 0, 1, 7, 7, 2, 7, 7]))

## Optimal: Boyer-Moore Voting Algorithm (O(n) time, O(1) space)
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

print(majorityElement([7,0,0,1,7,7,2,7,7]))  

## Majority Elements(&gt;N/3 times) | Find the elements that appears more than N/3 times in the array
def majority_E(nums):
    n=len(nums)
    for i in range (n):
        count=0
        for j in range(n):
            if nums[j]==nums[i]:
                count+=1
        if count>n//3:
            return nums[i]
print ("the majority element is", majority_E(nums=[1, 2, 1, 1, 3, 2] ))

# hashmap
def maj_element(nums):
    count={}
    n=len(nums)
    for i in range (n):
        count[nums]= count.get(nums,0) + 1
        if count>n//3:
            return nums
print ("the majority element is", majority_E(nums=[1, 2, 1, 1, 3, 2] ))

## Grid Unique Paths : DP on Grids (DP8)
def grid_unique_paths(arr,n,m):
    x=len(arr)
    for n in range(x):
        for 
