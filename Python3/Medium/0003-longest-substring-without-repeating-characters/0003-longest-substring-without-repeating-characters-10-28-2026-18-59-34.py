class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        i = 0
        j = 0

        seen = set()
        ans = 0

        while j < n:

            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            if s[j] not in seen:
                seen.add(s[j])

            ans = max(ans, j - i + 1)
            j += 1

        return ans
