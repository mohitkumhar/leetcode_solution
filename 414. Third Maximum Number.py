class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(set(nums)) < 3:
            return max(nums)
        

        sort_set_nums = sorted(set(nums))

        length = len(sort_set_nums)

        return sort_set_nums[length-3]

        