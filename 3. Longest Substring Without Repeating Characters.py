class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return 0

        start = 0
        end = 1

        longest_length = 1

        while end < n:
            while end < n and s[end] not in s[start:end]:
                end += 1

            longest_length = max(longest_length, end - start)
            start += 1
        return longest_length
