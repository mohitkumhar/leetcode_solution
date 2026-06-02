class Solution:
    def calculateSpan(self, arr):
        stack_for_next_greater_element_to_left = []
        left_greater_element = []
        ans = []

        for i in range(len(arr)):
            
            while stack_for_next_greater_element_to_left and arr[stack_for_next_greater_element_to_left[-1]] <= arr[i]:
                stack_for_next_greater_element_to_left.pop()
            
            if not stack_for_next_greater_element_to_left:
                left_greater_element.append(-1)
            
            elif arr[stack_for_next_greater_element_to_left[-1]] > arr[i]:
                left_greater_element.append(stack_for_next_greater_element_to_left[-1])
                
            stack_for_next_greater_element_to_left.append(i)

            ans.append(i - left_greater_element[i])


        return ans

