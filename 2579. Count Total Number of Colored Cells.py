class Solution:
    def coloredCells(self, n: int) -> int:

        if n == 1:
            return 1

        ans = 1
        i = 1

        while n > 1:
            ans += 4 * i
            n -= 1
            i += 1
        
        return ans