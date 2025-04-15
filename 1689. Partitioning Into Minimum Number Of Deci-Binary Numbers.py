class Solution:
    def minPartitions(self, n: str) -> int:
        maxi = 0

        for char in n:
            maxi = max(maxi, int(char))
        
        return maxi