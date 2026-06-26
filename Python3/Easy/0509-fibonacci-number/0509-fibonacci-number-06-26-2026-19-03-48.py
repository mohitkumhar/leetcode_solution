class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        next_prev = 0
        prev = 1
        ans = 0

        for i in range(2, n + 1):
            ans = next_prev + prev
            next_prev = prev
            prev = ans

        return ans
