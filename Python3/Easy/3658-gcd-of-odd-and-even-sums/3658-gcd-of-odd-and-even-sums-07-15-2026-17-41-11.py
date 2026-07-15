class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = 0
        odd_sum = 0

        for i in range(n * 2 + 1):
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i

        return math.gcd(even_sum, odd_sum)
