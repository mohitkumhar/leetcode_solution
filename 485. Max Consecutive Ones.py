class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        conti_ones = 0
        max_ones = 0

        for i in nums:
            if i == 1:
                conti_ones += 1
                max_ones = max(conti_ones, max_ones)
            else:
                conti_ones = 0
        
        return max_ones
            
        