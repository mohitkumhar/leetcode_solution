class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            curr = []
            if char == ")":
                while stack[-1] != "(":
                    curr.append(stack.pop())
                stack.pop()
                stack.extend(curr)
                continue

            stack.append(char)

        return "".join(stack)
