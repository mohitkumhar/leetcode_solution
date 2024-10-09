class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        ans = 0

        for i in range(1, n + 1):
            ans += (day + (i % 7 if i % 7 != 0 else 7) )
            
            if i % 7 == 0:
                day += 1
            
        return ans
