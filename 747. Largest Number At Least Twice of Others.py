class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_num = max(nums)
        max_index = nums.index(max_num)

        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1

        return max_index
