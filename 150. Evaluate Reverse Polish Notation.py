class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in set("+-/*"):
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num2 - num1)
                if token == '/':
                    stack.append(int(num2 / num1))
                if token == '*':
                    stack.append(num1 * num2)
                pass
            
            else:
                stack.append(int(token))

        return stack[0]
