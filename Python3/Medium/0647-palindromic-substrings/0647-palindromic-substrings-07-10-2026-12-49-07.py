class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(a: str) -> bool:
            return a == a[::-1]
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if check(s[i:j + 1]):
                    count += 1
        return count
