class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split('*')
        p1 = p[0]
        p2 = p[1]

        for i in range(len(s)):
            if s[i:].startswith(p1):
                start = i + len(p1)

                if p2 in s[start:]:
                    return True
        return False
