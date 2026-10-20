class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] < k:
                # curr char will not be in answer
                # array might be on left or right side

                leftSideArray = self.longestSubstring(s[:i], k)
                rightSideArray = self.longestSubstring(s[i + 1 :], k)

                return max(leftSideArray, rightSideArray)

        return len(s)
