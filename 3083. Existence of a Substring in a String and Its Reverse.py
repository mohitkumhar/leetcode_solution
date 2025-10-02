class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s = list(s)
        rev = list(reversed(s))

        for i in range(len(s)):
            sub_str = s[i: i+2]
            if len(sub_str) == 2:
                if ''.join(sub_str) in ''.join(rev):
                    return True

        return Falsegit status