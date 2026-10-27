class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float("-inf")
        currSum = 0

        for num in nums:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)

        return maxSum
