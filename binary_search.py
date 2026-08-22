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