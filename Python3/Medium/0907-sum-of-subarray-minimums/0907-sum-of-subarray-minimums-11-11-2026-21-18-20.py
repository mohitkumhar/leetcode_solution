class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        prevLeastVal = []
        stack = []

        MOD = 10**9 + 7

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if not stack:
                prevLeastVal.append(-1)
            else:
                prevLeastVal.append(stack[-1])
            stack.append(i)

        nextSmallerVal = []
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if not stack:
                nextSmallerVal.append(n)
            else:
                nextSmallerVal.append(stack[-1])

            stack.append(i)

        nextSmallerVal = nextSmallerVal[::-1]

        count = 0
        for i in range(n):
            leftCount = i - prevLeastVal[i]
            rightCount = nextSmallerVal[i] - i

            count = count + (arr[i] * leftCount * rightCount) % MOD

        return count % MOD
