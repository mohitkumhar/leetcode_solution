class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = str(n)

        prod = 1
        sum = 0

        for i in num:
            prod *= int(i)
            sum += int(i)

        return n % (sum + prod) == 0
