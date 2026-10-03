class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        nextPrev = 1
        prev = 2

        for i in range(3, n + 1):
            curr = prev + nextPrev

            nextPrev = prev
            prev = curr

        return curr
