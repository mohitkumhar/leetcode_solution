class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s = list(s)
        prefix = s[:k][::-1]
        return "".join(prefix + s[k:])
