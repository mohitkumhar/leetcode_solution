class Solution:
    def rob(self, nums: list[int]) -> int:

        def solve(i, isLooted):
            if i >= n:
                return 0

            if memo[i][isLooted] != -1:
                return memo[i][isLooted]

            take = 0
            if isLooted == 0:
                take = nums[i] + solve(i + 1, 1)

            skip = solve(i + 1, 0)

            memo[i][isLooted] = max(take, skip)
            return memo[i][isLooted]

        n = len(nums)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        return solve(0, 0)
