class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            
            elif char == '*':
                star_stack.append(i)
            
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                star_stack.pop()
                open_stack.pop()
            
            else:
                return False
            
        return not open_stack


