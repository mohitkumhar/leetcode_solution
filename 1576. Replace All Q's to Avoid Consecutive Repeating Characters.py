class Solution:
    def modifyString(self, s: str) -> str:

        s = list(s)

        
        for i in range(len(s)):
            if s[i] == '?':
                for j in range(ord('a'), ord('z') + 1):
                    char = chr(j)

                    if (i > 0 and s[i - 1] == char) or (i < len(s) - 1 and s[i + 1] == char):
                        continue
                    s[i] = char
        return ''.join(s)
