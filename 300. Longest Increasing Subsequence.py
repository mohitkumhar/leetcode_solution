class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(idx, prev):
            if idx >= n:
                return 0
            if memo[idx][prev] != -1:
                return memo[idx][prev]

            take = 0
            if prev == -1 or nums[idx] > nums[prev]:
                take = 1 + solve(idx + 1, idx)

            skip = solve(idx + 1, prev)
            ans = max(take, skip)
            memo[idx][prev] = ans

            return ans

        return solve(0, -1)
