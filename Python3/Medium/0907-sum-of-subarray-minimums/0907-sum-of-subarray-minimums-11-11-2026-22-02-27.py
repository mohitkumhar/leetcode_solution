class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        MOD = 10**9 + 7
        n = len(arr)

        leftSmallerVal = []
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if not stack:
                leftSmallerVal.append(-1)
            else:
                leftSmallerVal.append(stack[-1])
            stack.append(i)

        rightSmallerVal = []
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if not stack:
                rightSmallerVal.append(n)
            else:
                rightSmallerVal.append(stack[-1])
            stack.append(i)
        rightSmallerVal = rightSmallerVal[::-1]

        count = 0
        for i in range(n):

            leftCount = i - leftSmallerVal[i]
            rightCount = rightSmallerVal[i] - i

            count = count + (arr[i] * leftCount * rightCount) % MOD

        return count % MOD
