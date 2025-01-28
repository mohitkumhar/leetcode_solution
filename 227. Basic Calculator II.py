class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operation = '+'
        current_number = 0

        for i, char in enumerate(s):
            
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)

                if operation == '-':
                    stack.append(-current_number)
                
                if operation == '*':
                    stack.append(stack.pop() * current_number)
                
                if operation == '/':
                    stack.append(int(stack.pop() / current_number))
                
                operation = char
                current_number = 0
            
            
        return sum(stack)
        
        