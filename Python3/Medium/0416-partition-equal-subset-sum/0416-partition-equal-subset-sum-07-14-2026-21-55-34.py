class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def solve(i: int, curr_sum: int) -> bool:

            if i >= n:
                return False
            elif curr_sum == target:
                return True
            elif memo[i][curr_sum] != -1:
                return memo[i][curr_sum]

            take = 0
            if (curr_sum + nums[i]) <= target:
                take = solve(i + 1, curr_sum + nums[i])
            skip = solve(i + 1, curr_sum)

            memo[i][curr_sum] = take or skip
            return memo[i][curr_sum]

        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        n = len(nums)
        memo = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        return solve(0, 0)
