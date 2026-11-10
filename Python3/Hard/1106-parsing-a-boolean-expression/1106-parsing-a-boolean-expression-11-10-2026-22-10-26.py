class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for exp in expression:

            if exp == ",":
                continue

            elif exp != ")":
                stack.append(exp)

            # exp == ')'
            else:
                values = []

                while stack[-1] != "(":
                    values.append(stack.pop())

                stack.pop()  # '('

                op = stack.pop()

                if op == "|":
                    result = any(val == "t" for val in values)

                elif op == "&":
                    result = all(val == "t" for val in values)

                else:
                    result = values[0] == "f"

                stack.append("t" if result == True else "f")

        return stack[-1] == "t"
