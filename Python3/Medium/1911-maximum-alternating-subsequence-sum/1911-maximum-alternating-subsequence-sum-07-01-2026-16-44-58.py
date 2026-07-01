class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def solve(i, flag):
            if i >= n:
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]

            val = nums[i]
            if flag:
                val = -val

            take = val + solve(i + 1, not flag)
            skip = solve(i + 1, flag)

            memo[i][flag] = max(take, skip)
            return memo[i][flag]

        return solve(0, False)
