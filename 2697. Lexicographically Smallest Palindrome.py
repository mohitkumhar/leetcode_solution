class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            char = min(s[i], s[j])
            s[i] = char
            s[j] = char
            i += 1
            j -= 1
        return ''.join(s)