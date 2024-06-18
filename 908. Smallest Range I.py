class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        minimum = min(nums) + k

        maximum = max(nums) - k

        return max(0, maximum - minimum)
