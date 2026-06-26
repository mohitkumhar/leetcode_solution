class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def solve(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            take = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return solve(0)
