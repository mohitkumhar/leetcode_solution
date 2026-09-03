class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        ans = ""
        balance = 0

        for char in s:
            if char == "(":
                if balance > 0:
                    ans += char
                balance += 1

            else:
                if balance > 1:
                    ans += char
                balance -= 1
        return ans
