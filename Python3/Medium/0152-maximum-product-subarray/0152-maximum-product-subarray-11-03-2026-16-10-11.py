class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        leftProd = 1
        rightProd = 1
        maxProd = float('-inf')

        for i in range(n):
            leftProd *= nums[i]
            rightProd *= nums[n - i - 1]

            maxProd = max(maxProd, leftProd, rightProd)

            leftProd = leftProd if leftProd != 0 else 1
            rightProd = rightProd if rightProd != 0 else 1

        return maxProd
