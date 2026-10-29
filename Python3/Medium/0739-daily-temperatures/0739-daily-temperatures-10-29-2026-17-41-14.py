class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = []
        stack = []

        n = len(temperatures)

        for i in range(n - 1, -1, -1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if not stack:
                result.append(0)
            else:
                result.append(stack[-1] - i)

            stack.append(i)

        return result[::-1]
