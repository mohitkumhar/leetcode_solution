class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_str = s[i:j]
                if sub_str.count('1') <= k or sub_str.count('0') <= k:
                    count += 1
        return count
