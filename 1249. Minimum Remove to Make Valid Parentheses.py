class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        brackets = []
        i = 0

        for char in s:
            if char == '(':
                brackets.append(i)
            
            elif char == ')':
                
                if brackets and s[brackets[-1]] == '(':
                    brackets.pop()
                
                elif not stack:
                    brackets.append(i)

            i += 1

        s = list(s)
        brackets.sort(reverse=True)

        for ind in brackets:
            s.pop(ind)

        return ''.join(s)