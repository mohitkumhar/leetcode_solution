class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * n

        for i in range(n):
            take = nums[i] + dp[i - 2]
            skip = dp[i - 1]

            dp[i] = max(take, skip)

        return dp[n - 1]
