class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = bin(n)[2:]

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return False
        return True
