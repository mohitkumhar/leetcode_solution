import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for _ in range(k):
            maximum = max(gifts)

            index = gifts.index(maximum)
            gifts[index] = int(math.sqrt(maximum))

        
        return sum(gifts)
        