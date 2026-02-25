class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        min_sum = 0

        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)

        return 1 - min_sum
