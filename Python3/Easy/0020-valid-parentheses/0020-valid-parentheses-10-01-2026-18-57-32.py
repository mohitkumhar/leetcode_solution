class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            else:
                if not stack:
                    return False
                popedVal = stack.pop()

                if (
                    (char == ")" and popedVal != "(")
                    or (char == "}" and popedVal != "{")
                    or (char == "]" and popedVal != "[")
                ):
                    return False

        return True if not stack else False
