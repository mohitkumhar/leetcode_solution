class Solution:
    def canJump(self, nums: list[int]) -> bool:

        def solve(i):
            if i >= n:
                return False
            if i == n - 1:
                return True
            
            if memo[i] != -1:
                return memo[i]

            for idx in range(1, nums[i] + 1):
                if solve(i + idx):
                    memo[i + idx] = True
                    return True

            memo[i] = False
            return False

        n = len(nums)
        memo = [-1] * (n + 1)

        return solve(0)
