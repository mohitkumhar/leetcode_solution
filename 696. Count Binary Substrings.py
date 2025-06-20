class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        prev = 0
        current = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            
            else:
                result += min(prev, current)
                prev = current
                current = 1
        result += min(prev, current)

        return result