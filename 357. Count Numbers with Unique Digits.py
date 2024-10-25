class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int: 

        if n == 0:
            return 1
        

        unique_number = 9

        available_digit = 9

        count = 10

        for i in range(1, n):
            unique_number *= available_digit
            count += unique_number
            available_digit -= 1
        
        return count
