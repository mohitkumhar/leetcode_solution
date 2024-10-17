class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        max_pop = 0

        for i in s:
            
            max_pop = max(max_pop, len(stack))

            if i == '(':
                stack.append(i)
            
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()

        
        return max_pop 