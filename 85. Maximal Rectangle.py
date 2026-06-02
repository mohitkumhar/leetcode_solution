class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maximum_histogram_area(nums):
            n = len(nums)
            stack = []
            left_smaller_element = []

            for i in range(n):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if not stack:
                    left_smaller_element.append(-1)
                else:
                    left_smaller_element.append(stack[-1])
                stack.append(i)


            stack = []
            right_smaller_element = []

            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if not stack:
                    right_smaller_element.append(n)
                else:
                    right_smaller_element.append(stack[-1])
                stack.append(i)

            right_smaller_element = right_smaller_element[::-1]

            max_area = 0
            for i in range(n):
                curr_area = nums[i] * (right_smaller_element[i] - left_smaller_element[i] - 1)
                max_area = max(max_area, curr_area)

            return max_area

        m = len(matrix)
        n = len(matrix[0])
        heights = [0 for _ in range(n)]

        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            curr_area = maximum_histogram_area(heights)
            max_area = max(max_area, curr_area)

        return max_area
