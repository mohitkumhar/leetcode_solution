class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * 2 for _ in range(n+1)]

        def solve(idx, nums, flag):
            if idx >= n:
                return 0

            if memo[idx][flag] != -1:
                return memo[idx][flag]

            skip = solve(idx + 1, nums, flag)

            val = nums[idx]
            if not flag:
                val = -val

            take = val + solve(idx + 1, nums, not flag)

            ans = max(skip, take)
            memo[idx][flag] = ans

            return ans

        return solve(0, nums, True)
