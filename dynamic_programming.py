## Maximum Product Subarray in an Array
from pyparsing import nums


class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(nums[i], maxProduct * nums[i])
            minProduct = min(nums[i], minProduct * nums[i])
            result = max(result, maxProduct)

        return result

print (Solution().maxProduct([2, 3, -2, 4]))  

## frog jump
def frogJump(heights):
    n=len(heights)
    dp=[0]*n
    dp[0]=0
    for i in range(1,n):
        dp[i]= min(dp[i-1]+abs(heights[i]-heights[i-1]), dp[i-2]+abs(heights[i]-heights[i-2]))
    return dp[n-1]
print(frogJump([10, 20, 30, 10]))    # 20
print(frogJump([10, 20, 10]))        # 20


## Frog jump with K distances

class Solution:
    def frogJump(self, heights, k):
        n = len(heights)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, k + 1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + abs(heights[i] - heights[i - j]))

        return dp[n - 1]

print(Solution().frogJump([10, 20, 30, 10], 2))    # 20
print(Solution().frogJump([10, 20, 10], 1))        # 20
print(Solution().frogJump([10, 5, 20, 0, 15], 2))  # 15

## HOUSE ROBBER PROBLEM
class Solution:
    def rob(self, nums):
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]

print(Solution().rob([1,2,3,1]))  # 4
print(Solution().rob([2,7,9,3,1]))  # 12
print(Solution().rob([2,1,1,2]))  # 4


## Ninja Training Problem
class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0

        # dp[j] = best total points ending with activity j on the current day
        dp = matrix[0][:]  # day 0 base case

        for i in range(1, n):
            new_dp = [0, 0, 0]
            for j in range(3):
                # pick best from previous day where activity != j
                best_prev = max(dp[k] for k in range(3) if k != j)
                new_dp[j] = matrix[i][j] + best_prev
            dp = new_dp

        return max(dp)
print(Solution().ninjaTraining([[1,2,3], [10,15,10], [3,5,12]]))  # 25
