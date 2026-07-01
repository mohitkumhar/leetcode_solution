class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)] 

        def solve(idx, prev):
            if idx >= n:
                return 0

            if memo[idx][prev] != -1:
                return memo[idx][prev]

            skip = solve(idx + 1, prev)

            take = skip
            if prev == -1 or nums[prev] < nums[idx]:
                take = 1 + solve(idx + 1, idx)

            memo[idx][prev] = max(take, skip)
            return memo[idx][prev]

        return solve(0, -1)
