class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def solve(i, count, curr):
            nonlocal maxLen, st

            if count < 0:
                return

            if i == n:
                if count == 0:
                    if len(curr) > maxLen:
                        maxLen = len(curr)
                        st = {"".join(curr)}
                    elif len(curr) == maxLen:
                        st.add("".join(curr))

                return

            if s[i] != "(" and s[i] != ")":
                curr.append(s[i])
                solve(i + 1, count, curr)
                curr.pop()
                return

            curr.append(s[i])
            old_count = count

            if s[i] == "(":
                count += 1
            else:
                count -= 1

            solve(i + 1, count, curr)

            curr.pop()

            solve(i + 1, old_count, curr)

        maxLen = 0
        st = set()
        n = len(s)

        solve(0, 0, [])

        return list(st)
