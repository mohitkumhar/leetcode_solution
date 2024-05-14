class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 1
        max_count = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current_count += 1
                max_count = max(current_count, max_count)
            
            else:
                current_count = 1

        return max_count