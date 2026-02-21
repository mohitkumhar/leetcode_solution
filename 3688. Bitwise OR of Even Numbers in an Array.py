class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            if num % 2 == 0:
                ans = ans | num

        return ans
