class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        leftSmallerIdx = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                leftSmallerIdx[i] = stack[-1] + 1
            else:
                leftSmallerIdx[i] = 0

            stack.append(i)

        rightSmallerIdx = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                rightSmallerIdx[i] = stack[-1] - 1
            else:
                rightSmallerIdx[i] = n - 1

            stack.append(i)

        prefixSum = [0]

        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        ans = 0
        for i in range(n):

            currVal = nums[i] * (
                prefixSum[rightSmallerIdx[i] + 1] - prefixSum[leftSmallerIdx[i]]
            )

            ans = max(ans, currVal)

        return ans % MOD
