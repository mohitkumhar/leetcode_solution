class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice(word):
            map = {}

            for char in word:
                if char == char.lower():
                    if char.upper() not in word:
                        return False
                elif char == char.upper():
                    if char.lower() not in word:
                        return False
            return True

        longest = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if nice(s[i:j+1]) and len(s[i:j+1]) > len(longest) :
                    longest = s[i:j+1]
        return longest
