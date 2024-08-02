class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalpha():
                start += 1

            if not s[end].isalpha():
                end -= 1

            if s[start].isalpha() and s[end].isalpha():
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        return ''.join(s)
