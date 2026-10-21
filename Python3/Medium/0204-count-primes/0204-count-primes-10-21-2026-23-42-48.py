class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        # if n <= 2:
        #     return 0

        for i in range(2, n):
            isPrime = True

            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime:
                count += 1

        return count
