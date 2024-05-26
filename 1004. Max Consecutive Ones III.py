class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        flipped_zeros = 0
        start = 0
        max_ones = 0

        for end in range(0, len(nums)):

            if nums[end] == 0:
                flipped_zeros += 1

            while flipped_zeros > k:
                if nums[start] == 0:
                    flipped_zeros -= 1
                start += 1

            max_ones = max(max_ones, end - start + 1)

        return max_ones
