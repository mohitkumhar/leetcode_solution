class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        currStr = ""

        for char in s:
            if char == "(":
                if balance > 0:
                    currStr += char
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    currStr += char

        return currStr
