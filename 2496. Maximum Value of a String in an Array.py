class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            if s.isnumeric():
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))
        return ans