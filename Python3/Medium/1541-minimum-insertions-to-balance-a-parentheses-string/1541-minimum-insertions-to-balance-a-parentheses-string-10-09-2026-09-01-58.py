class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        ans = 0
        i = 0
        n = len(s)

        while i < len(s):

            if s[i] == "(":
                open += 1

            else:
                # check double closing ))
                if i + 1 < n and s[i + 1] == ")":
                    i += 1
                else:
                    ans += 1

                # check if open exists
                if open > 0:
                    open -= 1
                else:
                    ans += 1

            i += 1

        ans += open * 2

        return ans
