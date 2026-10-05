class Solution:
    def rob(self, nums: list[int]) -> int:

        def solve(i, isTaken):
            if i >= n:
                return 0

            val = 0 if isTaken else 1

            if memo[i][val] != -1:
                return memo[i][val]

            take = 0
            if not isTaken:
                take = nums[i] + solve(i + 1, True)

            skip = solve(i + 1, False)

            val = 0 if isTaken else 1
            memo[i][val] = max(take, skip)

            return memo[i][val]

        n = len(nums)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        return solve(0, False)
