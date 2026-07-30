class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            ans += (i // 8)+ 1

        return ans
