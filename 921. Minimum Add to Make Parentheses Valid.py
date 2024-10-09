class Solution:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not len(self.stack) == 0:
            self.stack.pop()
    
    def peek(self):
        if not len(self.stack) == 0:
            return self.stack[-1]


    def minAddToMakeValid(self, s: str) -> int:
        ans = 0

        for char in s:
            if char == '(':
                self.push(char)
            
            elif char == ')':
                if self.peek() == '(':
                    self.pop()
                else:
                    ans += 1
        
        while self.stack:
            self.stack.pop()
            ans += 1
        
        return ans
        