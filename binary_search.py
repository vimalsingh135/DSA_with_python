## Nth Root of a Number using linear Search
def nth_root(m,n):
    for i in range(1,m+1):
        power = i ** n
        if power==m:
            return i
        if i ** n>m:
            break

    return -1
print (nth_root(27,3))  # Output: 3
print (nth_root(16,4))  # Output: 2

## Nth Root of a Number using Binary Search
def func(mid, n, m):
    ans = 1
    for i in range(n):
        ans *= mid
        if ans > m:
            return 2  # too big
    if ans == m:
        return 1      # exact match
    return 0           # too small

def NthRoot(n, m):
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 2:
            high = mid - 1   # mid^n too big, search left
        else:
            low = mid + 1    # mid^n too small, search right
    return -1

# Test cases
print(NthRoot(3, 27))  # 3
print(NthRoot(4, 69))  # -1

## Median of Row Wise Sorted Matrix
from bisect import bisect_right

class solution:
    def count_smaller_equal(self, matrix, m, n, x):
        count = 0
        for i in range (m):
            count += bisect_right(matrix[i], x)   ## Count of elements less than or equal to x in each row
        return count
    def median(self, matrix, m, n):
            low=min(matrix[i][0] for i in range(m))
            high=max(matrix[i][n-1] for i in range(m))
            required = (m*n)//2
    
            while low<=high:
                mid = (low+high)//2
                count = self.count_smaller_equal(matrix, m, n, mid)
                if count<=required:
                    low=mid+1
                else:
                    high=mid-1
            return low

# Test
sol = solution()
matrix = [
    [1, 4, 9],
    [2, 5, 6],
    [3, 8, 7]  # NOTE: this row isn't sorted in your example, should be [3,7,8]
]
matrix = [
    [1, 4, 9],
    [2, 5, 6],
    [3, 7, 8]
]
print("Median:", sol.median(matrix, 3, 3))  

## Search Single Element in a sorted array
class Solution:
      # Function to find the single non-duplicate element using binary search
    def singleNonDuplicate(self, arr):
        # Get the size of the array
        n = len(arr)

        # Edge case: only one element in the array
        if n == 1:
            return arr[0]

        # Edge case: first element is the unique one
        if arr[0] != arr[1]:
            return arr[0]

        # Edge case: last element is the unique one
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        # Initialize binary search bounds
        low, high = 1, n - 2

        # Perform binary search
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2

            # Check if middle element is the unique one
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]

            # If mid is in the left half (pairing is valid)
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Move to the right half
                low = mid + 1
            else:
                # Move to the left half
                high = mid - 1

        # Dummy return (not reachable if input is valid)
        return -1

# Driver code
if __name__ == "__main__":
    # Input array with all elements appearing twice except one
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store the result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)


## Search Element in a Rotated Sorted Array
class Solution:
    # Function to search target in rotated sorted array using binary search
    def search(self, nums, target):
        # Set initial search space
        low = 0
        high = len(nums) - 1

        # Run loop while valid search space exists
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If target found at mid, return index
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # If target lies in left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1

# Driver code
nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
result = obj.search(nums, target)

print(result)

## Median of 2 sorted arrays
class Solution:
    def median(self, arr1, arr2):
        # Always binary search on the smaller array for efficiency
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        m, n = len(arr1), len(arr2)
        total = m + n
        half = (total + 1) // 2  # elements needed in the left partition
        
        low, high = 0, m
        
        while low <= high:
            cut1 = (low + high) // 2   # elements taken from arr1 into left half
            cut2 = half - cut1          # elements taken from arr2 into left half
            
            # Boundary values around the cut in arr1
            left1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = arr1[cut1] if cut1 < m else float('inf')
            
            # Boundary values around the cut in arr2
            left2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = arr2[cut2] if cut2 < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                # Valid partition found
                if total % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                high = cut1 - 1   # took too much from arr1, shrink
            else:
                low = cut1 + 1    # took too little from arr1, expand
        
        return -1  # shouldn't reach here if inputs are valid


# Test
sol = Solution()
print(sol.median([2, 4, 6], [1, 3, 5]))  # 3.5
print(sol.median([2, 4, 6], [1, 3]))     # 3.0

## K-th Element of two sorted arrays
class Solution:
    def kthElement(self, a, b, k):
        m = len(a)
        n = len(b)

        # Ensure a is smaller array for optimization
        if m > n:
            # Swap a and b
            return self.kthElement(b, a, k)
        
        # Length of the left half
        left = k

        # Apply binary search
        low = max(0, k - n)
        high = min(k, m)
        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = left - mid1

            # Initialize l1, l2, r1, r2
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = a[mid1] if mid1 < m else float('inf')
            r2 = b[mid2] if mid2 < n else float('inf')

            # Check if we have found the answer
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                # Eliminate the right half
                high = mid1 - 1
            else:
                # Eliminate the left half
                low = mid1 + 1
        
        # Dummy return statement
        return -1

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

# Create an instance of Solution class
solution = Solution()

# Print the answer
print(f"The {k}-th element of two sorted arrays is: {solution.kthElement(a, b, k)}")