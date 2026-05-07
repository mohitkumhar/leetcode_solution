class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(num):
            if num <= 1:
                return False

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        for value in counter.values():
            if isPrime(value):
                return True
        return False
