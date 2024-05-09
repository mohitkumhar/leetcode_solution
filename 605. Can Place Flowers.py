class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i]+=1
                    count += 1

                    if count == n:
                        return True
                
        return count >= n
