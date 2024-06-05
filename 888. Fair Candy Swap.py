class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """

        a_sum = sum(aliceSizes)
        b_sum = sum(bobSizes)

        diff = (a_sum - b_sum) // 2

        set_b = set(bobSizes)

        for i in aliceSizes:
            b = i - diff

            if b in set_b:
                return [i, b]
