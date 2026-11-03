class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        def solve(i, currSum):

            if i >= n or currSum > targetSum:
                return False
            if currSum == targetSum:
                return True

            key = str(i) + "_" + str(currSum)
            if key in memo:
                return memo[key]

            take = solve(i + 1, currSum + nums[i])
            skip = solve(i + 1, currSum)

            memo[key] = take or skip
            return memo[key]

        n = len(nums)
        targetSum = sum(nums) // 2

        if sum(nums) % 2 == 1:
            return False

        memo = {}
        return solve(0, 0)
