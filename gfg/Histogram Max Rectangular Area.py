class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        
        stack = []
        left_smaller_element = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if not stack:
                left_smaller_element.append(-1)
            
            else:
                left_smaller_element.append(stack[-1])
            stack.append(i)
        
        
        stack = []
        right_smaller_element = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if not stack:
                right_smaller_element.append(n)
            else:
                right_smaller_element.append(stack[-1])
            
            stack.append(i)
        
        right_smaller_element = right_smaller_element[::-1]
        
        max_area = 0
        for i in range(n):
            curr_area = arr[i] * (right_smaller_element[i] - left_smaller_element[i] - 1)
            max_area = max(max_area, curr_area)
            
        return max_area
