class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        def findMethod(start, target):
            j = bisect_left(nums, target, start)

            if j < n and nums[j] == target:
                return j

            return -1

        def solve(i, inc):
            currVal = nums[i] + inc
            length = 1

            if memo[i][inc] != -1:
                return memo[i][inc]

            # option 1- find (currVal + 1)
            j = findMethod(i + 1, currVal + 1)
            if j != -1:
                length = max(length, 1 + solve(j, 0))

            # option 2 - find(currVal)
            j = findMethod(i + 1, currVal)
            if j != -1:
                length = max(length, 1 + solve(j, 1))

            memo[i][inc] = length
            return length

        n = len(nums)

        nums.sort()

        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        result = 1
        for i in range(n):
            result = max(result, solve(i, 0), solve(i, 1))

        return result
