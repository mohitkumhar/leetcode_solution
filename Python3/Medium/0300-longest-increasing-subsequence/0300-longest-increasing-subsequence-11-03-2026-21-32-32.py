class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        def solve(i, prev):
            if i >= n:
                return 0
            if memo[i][prev + 1] != -1:
                return memo[i][prev + 1]

            take = 0
            if prev == -1 or nums[prev] < nums[i]:
                take = 1 + solve(i + 1, i)
            skip = solve(i + 1, prev)

            memo[i][prev + 1] = max(take, skip)
            return memo[i][prev + 1]

        n = len(nums)
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        return solve(0, -1)
