class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s) % 2 == 1:
            return False
            
        opening_stack = []
        closing_stack = []
        flexible = []

        for i in range(len(s)):
            if locked[i] == '1':
                
                if s[i] == '(':
                    opening_stack.append(i)
                
                else:
                    if opening_stack:
                        opening_stack.pop()
                    
                    elif flexible:
                        flexible.pop()
                    
                    else:
                        return False
                
            else:
                flexible.append(i)
            
        
        opening_stack.clear()
        closing_stack.clear()
        flexible.clear()

        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    closing_stack.append(s[i])
                
                else:
                    if closing_stack:
                        closing_stack.pop()
                    
                    elif flexible:
                        flexible.pop()
                    
                    else:
                        return False
            
            else:
                flexible.append(i)
            
        
        return True
