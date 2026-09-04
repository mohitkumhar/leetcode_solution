class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()

            ans = max(ans, len(stack))

        return ans
