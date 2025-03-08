class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = right + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        primes = [num for num in range(left, right + 1) if is_prime[num]]
        if len(primes) < 2:
            return [-1, -1]
        closest_pair = [primes[0], primes[1]]
        min_diff = primes[1] - primes[0]

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair
