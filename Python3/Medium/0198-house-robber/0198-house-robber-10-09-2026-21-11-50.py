class Solution:
    def rob(self, nums: list[int]) -> int:

        def solve(i, isLooted):
            if i >= n:
                return 0

            if memo[i][isLooted] != -1:
                return memo[i][isLooted]

            take = 0
            if not isLooted:
                take = nums[i] + solve(i + 1, True)

            skip = solve(i + 1, False)

            memo[i][isLooted] = max(take, skip)

            return memo[i][isLooted]

        n = len(nums)

        memo = [[-1] * 2 for _ in range(n + 1)]

        return solve(0, False)
