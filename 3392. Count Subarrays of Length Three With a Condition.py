class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for left in range(len(nums) - 2):
            if (nums[left] + nums[left + 2]) == (nums[left + 1] / 2.0):
                count += 1

        return count