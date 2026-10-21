class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack and (
                    (char == ")" and stack[-1] != "(")
                    or (char == "]" and stack[-1] != "[")
                    or (char == "}" and stack[-1] != "{")
                ):
                    return False
                stack.pop()

        return True if not stack else False
