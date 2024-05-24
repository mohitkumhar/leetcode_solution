class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def isPrime(num):
            if num == 1:
                return False

            i = 2
            while i < num:
                if num % i == 0:
                    return False
                i += 1
            return True

        prime_count = 0
        for i in range(left, right + 1):
            
            bins_count = bin(i)

            ones_count = 0
            
            for j in bins_count:
                if j == '1':
                    ones_count += 1

            if isPrime(ones_count):
                prime_count += 1

        return prime_count