class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        leftProduct = 1
        rightProduct = 1

        maxProduct = nums[0]

        for i in range(n):
            leftProduct *= nums[i]
            rightProduct *= nums[n - i - 1]

            maxProduct = max(maxProduct, leftProduct, rightProduct)

            leftProduct = leftProduct if leftProduct != 0 else 1
            rightProduct = rightProduct if rightProduct != 0 else 1

        return maxProduct
