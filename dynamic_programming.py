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