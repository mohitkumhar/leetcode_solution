class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign = 1
        result = 0

        stack = []

        for char in s:
            # brackets
            if char == "(":
                stack.append(result)
                stack.append(sign)

                number = 0
                result = 0
                sign = 1

            elif char == ")":
                result = result + (number * sign)
                number = 0

                prevSign = stack.pop()
                prevResult = stack.pop()

                result = (prevSign * result) + prevResult

            # sign
            elif char == "+" or char == "-":
                result = result + (number * sign)
                sign = 1 if char == "+" else -1
                number = 0

            elif char == " ":
                continue

            # char is number
            else:
                number = (number * 10) + int(char)

        return result + (number * sign)
