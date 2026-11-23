class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        def solve(i, prevChar):
            if i >= n:
                return 0

            key = f"{i}_{prevChar}"

            if key in counter:
                return counter[key]

            flip = float("inf")
            notFlip = float("inf")

            if s[i] == "0":
                # if prev char is 1 then flip is necessary
                if prevChar == "1":
                    flip = 1 + solve(i + 1, "1")

                # if prev char is not 1 then flip may not necessary
                else:
                    flip = 1 + solve(i + 1, "1")
                    notFlip = solve(i + 1, s[i])

            elif s[i] == "1":
                # if prev char is 0 then flip may req
                if prevChar == "0":
                    flip = 1 + solve(i + 1, "0")
                    notFlip = solve(i + 1, s[i])

                # if prev char is 1 then no flip is req
                else:
                    notFlip = solve(i + 1, s[i])

            counter[key] = min(flip, notFlip)
            return counter[key]

        n = len(s)
        counter = {}

        return solve(0, "0")
