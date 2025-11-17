class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        temp = 0

        for char in s:
            if char == '1':
                temp += 1
            else:
                temp = 0
            ans += temp

        return ans % MOD
