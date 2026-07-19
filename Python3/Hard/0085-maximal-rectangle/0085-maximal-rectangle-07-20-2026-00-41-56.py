class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def find_histpgram(heights: List[int]) -> int:

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
            max_area = 0

            for i in range(n):
                width = right_smaller_element[i] - left_smaller_element[i] - 1
                curr_area = heights[i] * width
                max_area = max(max_area, curr_area)

            return max_area

        m = len(matrix)
        n = len(matrix[0])

        heights = [0] * n
        curr_max = 0
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                elif matrix[i][j] == "0":
                    heights[j] = 0

            curr_max = find_histpgram(heights)
            print(curr_max)
            max_area = max(max_area, curr_max)

        return max_area
