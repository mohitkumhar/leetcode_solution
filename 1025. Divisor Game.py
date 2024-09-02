class Solution:
    def divisorGame(self, n: int) -> bool:
        chance = 1

        for i in range(n):
            if n > 1:
                n -= 1
                chance += 1
        
        
        return True if chance % 2 == 0 else False