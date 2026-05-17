class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []

        for num in arr:
            if stack and ((num >= 0 and stack[-1] < 0) or (num < 0 and stack[-1] >= 0)):
                stack.pop()
            else:
                stack.append(num)

        return stack
