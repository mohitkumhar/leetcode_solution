class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                ans += 1
        return ans