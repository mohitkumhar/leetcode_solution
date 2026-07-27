class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def backtrack(i, curr_sum):
            nonlocal result

            if curr_sum == target:
                return 1
            if i >= len(nums) or curr_sum > target:
                return 0
            if memo[i][curr_sum] != -1:
                return memo[i][curr_sum]

            take_idx = backtrack(0, curr_sum + nums[i])
            ignore_idx = backtrack(i + 1, curr_sum)

            memo[i][curr_sum] = take_idx + ignore_idx
            return memo[i][curr_sum]

        n = len(nums)
        memo = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        result = backtrack(0, 0)

        return result
