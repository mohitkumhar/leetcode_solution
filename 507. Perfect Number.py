class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        sum_of_divisors = 0

        nums = int(num ** 0.5)

        for i in range(1, nums + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i * i != num:
                    sum_of_divisors += num // i
            
        return sum_of_divisors - num == num
            
        