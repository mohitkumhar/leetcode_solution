class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for i in range(len(s)):
            if s[i].isupper():
                if not stack or stack[-1] != s[i].lower():
                    stack.append(s[i])
                else:
                    stack.pop()
            
            
            if s[i].islower():
                if not stack or stack[-1] != s[i].upper():
                    stack.append(s[i])
                else:
                    stack.pop()

        return ''.join(stack)
