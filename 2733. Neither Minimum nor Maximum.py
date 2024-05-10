class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(set(nums)) < 3:
            return -1

        sort_set_nums = sorted(set(nums))

        return sort_set_nums[1]