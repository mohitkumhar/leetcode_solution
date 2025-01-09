class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:

            if stack and stack[-1] == 'b' and char == 'c':
                if len(stack) > 1 and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
            
            else:
                stack.append(char)
        
        
        return False if stack else True
