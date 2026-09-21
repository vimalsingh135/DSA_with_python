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
