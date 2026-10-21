class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:

        def helper(count, i):
            if count == 0:
                return 0
            if i >= len(subArray):
                return float("-inf")

            if memo[i][count] != -1:
                return memo[i][count]

            take = subArray[i] + helper(count - 1, i + k)
            skip = helper(count, i + 1)

            memo[i][count] = max(take, skip)

            return memo[i][count]

        def solve(count, i):
            if count == 0:
                return

            if i >= len(subArray):
                return

            takeFromi = subArray[i] + helper(count - 1, i + k)
            skipFromi = helper(count, i + 1)

            if takeFromi >= skipFromi:
                result.append(i)
                solve(count - 1, i + k)
            else:
                solve(count, i + 1)

        subArray = []
        i = 0
        j = 0
        n = len(nums)
        currSum = 0
        result = []

        while j < n:
            currSum += nums[j]
            if j - i + 1 == k:
                subArray.append(currSum)
                currSum -= nums[i]
                i += 1
            j += 1

        memo = [[-1 for _ in range(4)] for _ in range(len(subArray) + 1)]
        solve(3, 0)

        return result
