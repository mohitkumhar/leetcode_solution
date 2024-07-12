class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                temp = []

                while stack and stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop() # removing opening parenthesis

                stack.extend(temp)

            
            else:
                stack.append(char)

        return ''.join(stack)

        