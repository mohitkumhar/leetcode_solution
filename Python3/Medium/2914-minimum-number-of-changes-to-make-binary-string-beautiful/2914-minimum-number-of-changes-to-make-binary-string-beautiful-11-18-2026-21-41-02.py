class Solution:
    def minChanges(self, s: str) -> int:
        return sum(a != b for a, b in batched(s, 2))