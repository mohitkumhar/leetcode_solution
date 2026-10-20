class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)

        i = 0
        j = 0

        k = n // 4

        ans = float("inf")
        currFreq = {}

        for char in s:
            currFreq[char] = currFreq.get(char, 0) + 1

        while j < n:
            currFreq[s[j]] -= 1

            while i < n and all(currFreq[char] <= k for char in currFreq):
                ans = min(ans, j - i + 1)
                currFreq[s[i]] += 1
                i += 1
            j += 1

        return ans
