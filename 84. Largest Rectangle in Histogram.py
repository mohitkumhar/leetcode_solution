class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left_smaller_element = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                left_smaller_element.append(-1)
            elif heights[stack[-1]] < heights[i]:
                left_smaller_element.append(stack[-1])

            stack.append(i)


        stack = []
        right_smaller_element = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                right_smaller_element.append(n)
            elif heights[stack[-1]] < heights[i]:
                right_smaller_element.append(stack[-1])

            stack.append(i)

        right_smaller_element = right_smaller_element[::-1]        
        max_area = 0

        for i in range(n):
            curr_area = heights[i] * (right_smaller_element[i] - left_smaller_element[i] - 1)
            max_area = max(max_area, curr_area)

        return max_area
