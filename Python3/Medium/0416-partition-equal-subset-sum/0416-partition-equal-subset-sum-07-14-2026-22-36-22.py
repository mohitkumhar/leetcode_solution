class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                take = False
                if nums[i - 1] <= j:
                    take = dp[i - 1][j - nums[i - 1]]
                skip = dp[i - 1][j]

                dp[i][j] = take or skip

        return dp[n][target]
