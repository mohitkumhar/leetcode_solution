class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        next_prev = 1
        prev = 2
        ans = 0

        for i in range(3, n + 1):
            ans = next_prev + prev
            next_prev = prev
            prev = ans

        return ans