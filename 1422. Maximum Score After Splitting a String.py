class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        max_count = 0
        for i in range(len(s) - 1):
            left = s[:i+1]
            right = s[i+1:]
            max_count = max(max_count, left.count('0') + right.count('1'))
            print(left, right)

        return max_count
