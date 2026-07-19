class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        left_smaller_element = []
        stack = []

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                left_smaller_element.append(-1)
            elif heights[stack[-1]] < heights[i]:
                left_smaller_element.append(stack[-1])

            stack.append(i)

        right_smaller_element = []
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                right_smaller_element.append(n)
            elif heights[stack[-1]] < heights[i]:
                right_smaller_element.append(stack[-1])

            stack.append(i)

        right_smaller_element.reverse()

        max_height = 0
        curr_height = 0

        for i in range(n):
            width = right_smaller_element[i] - left_smaller_element[i] - 1
            curr_height = heights[i] * width
            max_height = max(max_height, curr_height)

        return max_height
