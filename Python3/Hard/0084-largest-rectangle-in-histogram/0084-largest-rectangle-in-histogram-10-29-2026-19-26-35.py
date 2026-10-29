class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)

        stack = []
        leftSmallerValue = []

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                leftSmallerValue.append(-1)
            else:
                leftSmallerValue.append(stack[-1])
            stack.append(i)

        stack.clear()

        rightSmallerValue = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                rightSmallerValue.append(n)
            else:
                rightSmallerValue.append(stack[-1])
            stack.append(i)

        rightSmallerValue.reverse()
        ans = 0

        for i in range(n):
            left = leftSmallerValue[i]
            right = rightSmallerValue[i]

            width = right - left - 1

            area = width * heights[i]

            ans = max(ans, area)
        return ans
