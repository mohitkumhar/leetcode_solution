class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        def solve(i, taken):
            if i >= n:
                return 0
            if memo[i][taken] != -1:
                return memo[i][taken]

            take = 0
            if not taken:
                take = nums[i] + solve(i + 1, True)
            skip = solve(i + 1, False)

            memo[i][taken] = max(take, skip)
            return memo[i][taken]

        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]
        return solve(0, False)
