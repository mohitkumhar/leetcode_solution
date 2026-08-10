class Solution:

    def makeLargestSpecial(self, s: str) -> str:

        def solve(s):
            special = []
            currSum = 0
            start = 0

            for i in range(len(s)):
                currSum += 1 if s[i] == "1" else -1

                if currSum == 0:
                    special.append("1" + solve(s[start + 1 : i]) + "0")
                    start = i + 1

            special.sort(reverse=True)
            return "".join(special)

        return solve(s)
