class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            take = nums[i] + dp[i - 2]
            skip = dp[i - 1]

            dp[i] = max(take, skip)

        return dp[n - 1]
