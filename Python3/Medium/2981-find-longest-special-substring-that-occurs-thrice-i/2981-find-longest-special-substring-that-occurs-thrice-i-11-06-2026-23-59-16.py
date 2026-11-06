class Solution:
    def maximumLength(self, s: str) -> int:
        freq = {}
        n = len(s)

        for i in range(n):
            currStr = ""

            for j in range(i, n):
                if not currStr or currStr[-1] == s[j]:
                    currStr += s[j]
                    freq[currStr] = freq.get(currStr, 0) + 1
                else:
                    break

        ans = -1
        for key, value in freq.items():
            if value >= 3:
                ans = max(ans, len(key))

        return ans
