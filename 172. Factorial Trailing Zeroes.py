class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n <= 4:
            return 0
        
        count = 0
        for i in range(5, n + 1):
            
            x = i
            while (x % 5 == 0):
                if x % 5 == 0:
                    count += 1
                    x = x // 5

        return count 
