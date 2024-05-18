class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        conti = 0

        for i in arr:
            if i % 2 != 0:
                conti += 1

            else:
                conti = 0

            if conti >= 3:
                break

        return conti >= 3
