class Solution:
    def maximumLength(self, s: str) -> int:
        freq = {}
        n = len(s)

        for i in range(n):
            currStrLen = 0
            currChar = ""

            for j in range(i, n):
                if not currChar or currChar == s[j]:
                    currStrLen += 1
                    currChar = s[j]
                    freq[(currChar, currStrLen)] = (
                        freq.get((currChar, currStrLen), 0) + 1
                    )
                else:
                    break

        ans = -1
        for key, value in freq.items():
            if value >= 3:
                ans = max(ans, key[1])

        return ans
