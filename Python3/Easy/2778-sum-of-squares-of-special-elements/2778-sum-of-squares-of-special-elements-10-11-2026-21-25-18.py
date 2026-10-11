class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range(1, n + 1):
            if n % i == 0:
                result += nums[i - 1] * nums[i - 1]

        return result
