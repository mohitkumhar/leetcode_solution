class Solution:
    def maxArea(self, mat):
        
        def maximum_histogram_area(nums):
            n = len(nums)
            stack = []
            left_smaller_area = []
            
            for i in range(n):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                
                if not stack:
                    left_smaller_area.append(-1)
                else:
                    left_smaller_area.append(stack[-1])
                
                stack.append(i)


            stack = []
            right_smaller_area = []

            for i in range(n-1, -1, -1):
                
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if not stack:
                    right_smaller_area.append(n)
                else:
                    right_smaller_area.append(stack[-1])
                
                stack.append(i)
            
            right_smaller_area = right_smaller_area[::-1]
            
            max_area = 0
            for i in range(n):
                curr_area = nums[i] * (right_smaller_area[i] - left_smaller_area[i] - 1)
                max_area = max(max_area, curr_area)
            
            return max_area
        
        
        m = len(mat)
        n = len(mat[0])

        heights = [0 for _ in range(n)]
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            curr_area = maximum_histogram_area(heights)
            max_area = max(max_area, curr_area)
        
        return max_area
