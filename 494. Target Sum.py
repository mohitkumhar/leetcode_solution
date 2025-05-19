class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (target + total) % 2 == 1 or total < abs(target):
            return 0

        subset_sum = (target + total) // 2

        dp = [[0] * (subset_sum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(subset_sum + 1):

                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]

                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(nums)][subset_sum]