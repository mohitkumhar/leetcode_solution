class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))

            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "/":
                    stack.append(int(num2 / num1))
                elif token == "*":
                    stack.append(num1 * num2)

        return stack[0]
