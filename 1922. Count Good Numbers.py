class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        even_choice = 5     # 0, 2, 4, 6, 8
        prime_choice = 4    # 1, 3, 5, 7
        even_count = (n + 1) // 2
        odd_count = n // 2

        result = (pow(even_choice, even_count, MOD) * pow(prime_choice, odd_count, MOD)) % MOD
        return result