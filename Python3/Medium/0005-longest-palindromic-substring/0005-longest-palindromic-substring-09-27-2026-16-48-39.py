class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(s):
            return s == s[::-1]
        
        n = len(s)
        ans = ""
        maxLen = 0

        for i in range(n):
            for j in range(i, n):
                if isPal(s[i:j+1]):
                    if maxLen < (j - i + 1):
                        maxLen = j - i + 1
                        ans = s[i : j + 1]
        return ans
