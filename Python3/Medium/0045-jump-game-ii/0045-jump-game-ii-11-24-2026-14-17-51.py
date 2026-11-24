class Solution:
    def jump(self, nums: list[int]) -> int:

        def solve(i):
            if i >= n:
                return float("inf")
            if i == n - 1:
                return 0

            if memo[i] != -1:
                return memo[i]

            jump = float("inf")
            for j in range(1, nums[i] + 1):
                jump = min(jump, 1 + solve(i + j))

            memo[i] = jump
            return memo[i]

        n = len(nums)
        memo = [-1] * (n + 1)

        return solve(0)
