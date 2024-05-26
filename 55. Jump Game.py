class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        final_position = len(nums) - 1

        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= final_position:
                final_position = index

        return final_position == 0
